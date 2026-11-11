#!/usr/bin/env python3
"""Calibrate the viva-commands checker against the converter's real render step.

    python3 scripts/calibrate.py [case …]   all cases, or only the named ones (from the skill folder)

Each case puts one snippet into a temporary copy of the demo document (as an extra chapter, or edits the manifest
or another file) and records whether md_render fails and what level the checker gives it. A line starting with
`!!` is a mismatch: the checker should say `error` exactly when the render step fails. Run it after the converter
changed. The converter checkout: $VIVA_CONVERTER, default ~/viva-publisher-converter (run with `uv run --project`).
"""
import os
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]   # the viva-commands skill folder
DEMO = SKILL / 'assets/demo_starter'
CHECKER = SKILL / 'scripts/check_commands.py'
CONVERTER = Path(os.environ.get('VIVA_CONVERTER', Path.home() / 'viva-publisher-converter'))
U = lambda: str(uuid.uuid4())  # noqa: E731
DUP = 'c554c85c-8452-4021-84a0-0100423e7444'   # used in the demo's chapter 1
LO = "{% call learning_objectives() %}\n| LZ_1 | Sie können es. |\n{% endcall %}"

CASES = {
    # name: snippet for the extra chapter (or (target, function) for other files)
    'ok_baseline': 'Ein Absatz.',
    'ok_heading_anchor_uuid': f"## Abschnitt {{{{ anchor('abs_x') }}}} {{{{ uuid('{U()}') }}}}",
    'ok_layout_cell_title': "{% call table('8cm', '8cm', type='layout') %}\n| Text | {{ image('images/bauteil.png', width='7cm', title='T') }} |\n{% endcall %}",
    'ok_table_then_caption': "{{ table('4cm', '*') }}\nTabelle: Titel\n| a | b |\n| --- | --- |\n| 1 | 2 |",
    'index_alone': "{{ index('Motor') }}\nMotor dreht.",
    'uuid_before_anchor': f"## Abschnitt {{{{ uuid('{U()}') }}}} {{{{ anchor('abs_y') }}}}",
    'heading_text_after_uuid': f"## Abschnitt {{{{ uuid('{U()}') }}}} mehr",
    'caption_blank_before_table': "Tabelle: Titel\n\n| a | b |\n| --- | --- |\n| 1 | 2 |",
    'caption_then_table_cmd': "Tabelle: Titel\n{{ table('4cm', '*') }}\n| a | b |\n| --- | --- |\n| 1 | 2 |",
    'caption_empty': "Tabelle:\n| a | b |",
    'image_inline': "Text {{ image('images/bauteil.png') }} inline.",
    'note_blank_line': "{{ note() }}\n\nText.",
    'note_eof': "{{ note() }}",
    'frame_before_heading': "{{ frame() }}\n## Titel",
    'widths_over_16': "{{ table('10cm', '10cm') }}\n| a | b |",
    'widths_count': "{{ table('4cm', '4cm') }}\n| a | b | c |",
    'widths_count_html': "{{ table('4cm', '4cm') }}\n<table>\n<tr><td>a</td><td>b</td><td>c</td></tr>\n</table>",
    'widths_bad_unit': "{{ table('4in', '*') }}\n| a | b |",
    'table_nothing_after': "{{ table('4cm', '*') }}\n\nText.",
    'lo_widths_count': "{% call learning_objectives('2cm', '2cm', '2cm') %}\n| LZ_1 | Sie können es. |\n{% endcall %}",
    'lo_with_caption': "{{ learning_objectives() }}\nTabelle: X\n| LZ_1 | Sie können es. |",
    'uuid_v1': "Absatz. {{ uuid('e4eaaaf2-d142-11d4-a3c4-9c2e5e2e7d10') }}",
    'uuid_dup': f"Absatz. {{{{ uuid('{DUP}') }}}}",
    'uuid_alone': f"Absatz.\n\n{{{{ uuid('{U()}') }}}}",
    'uuid_before_text': f"{{{{ uuid('{U()}') }}}} Absatz.",
    'uuid_in_cell': f"| a {{{{ uuid('{U()}') }}}} | b |",
    'uuid_twice': f"Absatz. {{{{ uuid('{U()}') }}}} {{{{ uuid('{U()}') }}}}",
    'uuid_text_after_para': f"Absatz. {{{{ uuid('{U()}') }}}} mehr Text.",
    'uuid_arg_bad': "{{ page_break(uuid='abc') }}",
    'anchor_dup': "## X {{ anchor('ueberschriften') }}",
    'anchor_in_para': "Absatz {{ anchor('abs_z') }}.",
    'anchor_bad_name': "## X {{ anchor('1abc') }}",
    'ref_missing': "Siehe {{ ref('gibtsnicht') }}.",
    'ref_bad_show': "Siehe {{ ref('ueberschriften', 'nummer') }}.",
    'cite_missing': "Text {{ cite('gibtsnicht') }}.",
    'image_missing': "{{ image('images/fehlt.png') }}",
    'image_scale_width': "{{ image('images/bauteil.png', width='5cm', scale='50%') }}",
    'image_wrap_center': "{{ image('images/bauteil.png', wrap=True, align='center') }}",
    'image_numbered_no_title': "{{ image('images/bauteil.png', numbered=False) }}",
    'image_anchor_no_title': "{{ image('images/bauteil.png', anchor='abb_q') }}",
    'image_rotate_45': "{{ image('images/bauteil.png', rotate=45) }}",
    'image_crop_bad': "{{ image('images/bauteil.png', crop='a b') }}",
    'image_width_bad': "{{ image('images/bauteil.png', width='5') }}",
    'image_title_normal_cell': "| a | {{ image('images/bauteil.png', title='T') }} |",
    'image_wrap_cell': "| a | {{ image('images/bauteil.png', wrap=True) }} |",
    'md_image_missing': "![x](images/fehlt.png)",
    'color_name': "Text {{ color('rot', 'red') }}.",
    'color_empty': "Text {{ color('') }}.",
    'link_no_scheme': "Text {{ link('www.example.org') }}.",
    'link_empty_text': "Text {{ link('https://example.org', '') }}.",
    'grid_zero': "{{ grid(n_width=0) }}",
    'grid_inline': "Text {{ grid() }}",
    'qr_inline': "Text {{ qr_code('x') }}",
    'qr_bad_size': "{{ qr_code('x', size='2') }}",
    'label_offset_y_no_note': "{{ label('Hinweis', icon='bell', offset_y='50%') }}\n\nText.",
    'label_unknown_icon': "{{ label('Hinweis', icon='glocke') }}",
    'label_empty': "{{ label('') }}",
    'list_expr': "{{ list() }}\n- a",
    'list_with_para': "{% call list() %}\n- a\n- b\n\nAbsatz.\n{% endcall %}",
    'note_call_heading': "{% call note() %}\n## Titel\n{% endcall %}",
    'note_call_empty': "{% call note() %}\n{% endcall %}",
    'note_call_image': "{% call note() %}\nText.\n\n{{ image('images/bauteil.png') }}\n{% endcall %}",
    'frame_thick': "{{ frame(thickness='10pt') }}\nText.",
    'frame_color_bad': "{{ frame(color='blue') }}\nText.",
    'endcall_inline': "{% call note() %}\nText {% endcall %}",
    'endcall_missing': "{% call note() %}\nText.",
    'table_layout_caption': "{% call table('4cm', '*', type='layout') %}\nTabelle: T\n| x | y |\n{% endcall %}",
    'table_anchor_no_caption': "{% call table('4cm', '*', anchor='tab_q') %}\n| a | b |\n{% endcall %}",
    'table_type_bad': "{% call table('4cm', '*', type='bilder') %}\n| a | b |\n{% endcall %}",
    'table_call_extra_text': "{% call table('4cm', '*') %}\n| a | b |\n\nText.\n{% endcall %}",
    'html_colspan_bad': "<table>\n<tr><td colspan=\"x\">a</td></tr>\n</table>",
    'html_unclosed': "<table>\n<tr><td>a</td></tr>",
    'link_lo_outside': "{{ link_lo('51620B64-F785-4D0C-B5B3-EEFF051576CA') }}",
    'link_lo_not_first_cell': "{% call learning_objectives() %}\n| LZ_1 | Text {{ link_lo('51620B64-F785-4D0C-B5B3-EEFF051576CA') }} |\n{% endcall %}",
    'link_lo_bad_key': "{% call learning_objectives() %}\n| LZ_1 {{ link_lo('abc') }} | Text |\n{% endcall %}",
    'content_outside_cell': f"{{% call content(uuid='{U()}') %}}Text{{% endcall %}}",
    'content_expr': f"| a | {{{{ content(uuid='{U()}') }}}} |",
    'index_colon': "Ein {{ index('a:b') }}Wort.",
    'index_empty': "Ein {{ index('') }}Wort.",
    'unknown_cmd': "{{ unbekannt() }}",
    'unknown_arg': "{{ page_break(foo=1) }}",
    'too_many_pos': "Text {{ footnote('a', 'b') }}.",
    'missing_required': "Text {{ footnote() }}.",
    'quote_error': "Text {{ footnote('it's') }}.",
    'manifest_cmd_in_chapter': "{{ keyword_index() }}",
    'formula_align_inline': "Text {{ formula('a', align='center') }} mehr.",
    'formula_bad_align': "{{ formula('a', align='mitte') }}",
    'formula_bad_latex': "{{ formula('\\frac{a}') }}",
    'formula_xi': "Text {{ formula('\\xi + \\underline{x}') }}.",
    'call_in_code_fence': "```markdown\n{{ image('images/fehlt.png') }}\n```",
    'callout_unknown': "> [!FOO] Titel\n> Text",
    'jinja_if': "{% if true %}Text{% endif %}",
    'jinja_var': "Text {{ foo }}.",
    'placeholder': "((fehlt.png))",
    'chapter_two_h1': "# Zweiter Titel",
    # other files: (file, mode, text) — mode 'append' or 'replace:<old>'
    'man_chapter_only_cmd': ('_main_.md', 'append', "{{ note() }}"),
    'man_text_line': ('_main_.md', 'append', "Ein Satz."),
    'man_title_twice': ('_main_.md', 'append', "{{ title('Nochmal') }}"),
    'man_toc_twice': ('_main_.md', 'append', "{{ table_of_contents() }}"),
    'man_page_break_text': ('_main_.md', 'append', "{{ page_break() }} x"),
    'man_call_form': ('_main_.md', 'append', "{% call note() %}\n{% endcall %}"),
    'man_missing_chapter': ('_main_.md', 'append', "{{ chapter('fehlt.md') }}"),
    'man_imprint_top_range': ('_main_.md', 'replace:top=\'190mm\'', "top='300mm'"),
    'man_logo_bad': ('_main_.md', 'append', "{{ logo('a b') }}"),
    'man_watermark_color': ('_main_.md', 'replace:{{ watermark(\'MUSTER\') }}', "{{ watermark('MUSTER', color='grau') }}"),
    'cover_image_with_imprint': ('cover.md', 'append', "\n#### Impressum\nTitel: X"),
    'glossar_no_colon': ('glossar.md', 'append', "Ein Begriff ohne Doppelpunkt"),
    'sources_dup_key': ('quellen.md', 'append', "jinja: Doppelt."),
    'sources_bad_key': ('quellen.md', 'append', "1abc: Eintrag."),
}


def build(tmp: Path, case):
    doc = tmp / 'content' / 'demo_starter'
    shutil.copytree(DEMO, doc)
    man = doc / '_main_.md'
    if isinstance(case, str):
        (doc / '_9_test.md').write_text("# Test {{ anchor('kap_test9') }}\n\n" + case + "\n", encoding='utf-8')
        s = man.read_text().replace("{{ chapter('_5_didaktik.md', image='images/kapitel_5.svg') }}",
                                    "{{ chapter('_5_didaktik.md', image='images/kapitel_5.svg') }}\n{{ chapter('_9_test.md') }}")
        man.write_text(s)
    else:
        f, mode, text = case
        p = doc / f
        s = p.read_text()
        if mode == 'append':
            s = s.rstrip('\n') + '\n' + text + '\n'
        else:
            old = mode.split(':', 1)[1]
            assert old in s, (f, old)
            s = s.replace(old, text)
        p.write_text(s)
    return doc


def run(name, case):
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        doc = build(tmp, case)
        r = subprocess.run(['uv', 'run', '--project', str(CONVERTER), '--no-sync', 'python', '-m',
                            'viva_publisher_converter.md_render', '--document', 'demo_starter'],
                           cwd=tmp, capture_output=True, text=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
        real = 'FAIL' if r.returncode else 'pass'
        real_msg = ' | '.join(ln for ln in r.stderr.splitlines() if ln.strip())[-300:]
        c = subprocess.run([sys.executable, '-B', str(CHECKER), str(doc)], capture_output=True, text=True)
        lines = [ln for ln in c.stdout.splitlines() if ': ' in ln and not ln.startswith('--')]
        # ignore the demo's own known findings
        lines = [ln for ln in lines if not (ln.startswith(('_2_bilder.md:92:', '_2_bilder.md:109:')) or '_2_bilder.md:92' in ln or '_2_bilder.md:109' in ln)]
        level = 'error' if any(': error: ' in ln for ln in lines) else 'warning' if any(': warning: ' in ln for ln in lines) else 'ok'
        return real, real_msg, level, lines


def main():
    only = sys.argv[1:]
    mismatches = total = 0
    for name, case in CASES.items():
        if only and name not in only:
            continue
        real, msg, level, lines = run(name, case)
        total += 1
        agree = (real == 'FAIL') == (level == 'error')
        mismatches += not agree
        flag = '  ' if agree else '!!'
        print(f"{flag} {name:28} real={real:4} checker={level:7} {('| ' + msg[-140:]) if real == 'FAIL' else ''}")
        if not agree:
            for ln in lines[:3]:
                print(f"       checker: {ln[-150:]}")
    print(f'-- {total - mismatches} of {total} cases agree with the render step')


if __name__ == '__main__':
    main()
