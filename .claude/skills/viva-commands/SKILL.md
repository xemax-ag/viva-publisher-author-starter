---
name: viva-commands
description: Format, write, convert and check the Markdown content of a viva publisher document (textbook template textbook_2026_V02 → Word → PDF) with the render-step commands of COMMANDS.md — {{ image() }}, {{ table() }}, {{ formula() }}, {{ ref() }}/{{ anchor() }}, {{ cite() }}, {{ footnote() }}, {{ index() }}, {{ label() }}, {{ note() }}, {{ frame() }}, {{ learning_objectives() }}, {{ uuid() }} and the manifest _main_.md. Use this skill whenever the user wants to create or edit a manifest, chapter, cover, impressum, management summary, glossar or quellen file (e.g. under 2_md_content/), turn plain Markdown, Word-exported or pasted text into this format, add pictures, tables, formulas, learning objectives, Hinweis/Beispiel/Aufgabe boxes or cross references, or find and fix render-step problems — even if they don't mention COMMANDS.md or "commands".
---

# viva-commands: Markdown for the viva publisher converter

A document is a folder of Markdown files. Its manifest `_main_.md` lists the cover, the chapters and the
directories in order. The files contain Jinja calls `{{ name(…) }}`. The render step checks every call. **A single
failing call stops the whole conversion.** That is why exactness matters more than anything else here: a
nicely worded chapter with one wrong argument produces no Word document at all.

The pipeline of an author project: `content/1_docx_source/` (Word sources) →
**`content/2_md_content/<document>/`** (what you edit) → `content/3_md_rendered/` (render output, markers
`⟦name {…}⟧`) → `content/4_docx_pdf_result/`. Edit only the `2_md_content` files. The other folders are produced by
the converter, so changes there are overwritten.

## This skill's files

Everything this skill needs is in its own folder, written `<skill>` below (the base directory shown when the skill
is loaded):

| Path | What it is |
| --- | --- |
| `<skill>/references/COMMANDS.md` | the reference of every command |
| `<skill>/assets/demo_starter/` | a complete example document that passes the checker and uses every command |
| `<skill>/scripts/check_commands.py` | the checker (step 3 of the workflow) |
| `<skill>/scripts/calibrate.py` | for maintainers: compares the checker with the converter's render step |

The files in `<skill>` are reference material. Don't edit them while working on a user's document. Copy what you
need into the document instead. A `demo_starter` document in the user's project is a separate copy that the user
may edit.

## Sources of truth

1. **`<skill>/references/COMMANDS.md`** is the authoritative description of every command: arguments, defaults,
   where it may stand, and what counts as a problem. When this skill and COMMANDS.md disagree, COMMANDS.md wins.
   Read its *Writing a call* section and the *Overview* table once per session. Then read the section of each
   command you use before you write it, because the details (units, allowed values, combinations) live there.
   Each command has a heading of its own (`grep -n '^### image' <skill>/references/COMMANDS.md`). The file is a
   copy of the converter's `viva_publisher_converter/md_render/COMMANDS.md`. If a converter checkout is at hand
   (see step 4) and its copy differs, the converter's copy is newer.
2. **`<skill>/assets/demo_starter/`** is a complete document that passes the checker and uses every command. Copy
   its patterns:

   | Demo file | Shows |
   | --- | --- |
   | `_main_.md` | manifest: title, watermark, cover with picture, imprint, management summary, TOC, chapters with opener pictures, lists of figures/tables, glossar, bibliography, keyword index |
   | `cover.md`, `impressum.md`, `management_summary.md`, `glossar.md`, `quellen.md` | the formats of these files |
   | `_1_text_und_struktur.md` | headings + `anchor()`, bold/italic, `color()`, `<br>`, escapes, lists, `{% call list() %}`, `link()`, `ref()`, `footnote()`, `cite()`, `index()`, `uuid()`, comments, code blocks, `page_break()` |
   | `_2_bilder.md` | `image()` with every option, Markdown picture, placeholder `((…))`, `qr_code()`, `grid()` |
   | `_3_tabellen.md` | pipe and HTML tables, `Tabelle:` captions, `table()` widths/anchor/`numbered`, colspan/rowspan, `type='pictures'`, `type='layout'`, `content()` |
   | `_4_formeln.md` | `formula()` inline, on its own line, `align`, LaTeX examples |
   | `_5_didaktik.md` | `label()` + icons, `learning_objectives()` + `link_lo()`, `note()`, `frame()`, boxes `> [!AUFGABE]` etc., Selbstkontrolle |

   Each demo section shows its source again in a `{% raw %}` code block. That is only there to teach the commands.
   Do not copy those code blocks into real content.

## Workflow

1. **Orient.** Find the document folder and read its `_main_.md`. Before adding `ref()` or `cite()`, collect what
   already exists: the anchors (`grep -rn "anchor" <folder>`) and the keys in the sources file. If the user gives
   a single loose file, ask which document it belongs to, or check it on its own.
2. **Format.** Use the mapping table below. Change markup, not content. Keep the author's wording, language and
   spelling (the demo is Swiss German: «ss» instead of «ß», «…» quotes). New text you have to write yourself, such as
   captions and label texts, follows the document's style.
3. **Check.** Run the checker and fix every error:
   ```bash
   python3 <skill>/scripts/check_commands.py <document folder | any file in it>
   ```
   It finds `_main_.md` and checks the whole document together: call syntax and arguments, where each command may
   stand, the files it names, table widths against columns, uuids, anchors, `ref()` targets and `cite()` keys. It
   was calibrated against the real render step. `error` means the render step rejects it. `warning` means the render
   step accepts it, but the result is probably not what was meant (e.g. a `Tabelle:` line that is not directly
   above its table loses its caption number). `info` lists placeholders for pictures that are still missing.
   Unlike the render step, which stops at the first Jinja syntax error, the checker lists every problem in one
   pass, so fix them all and then run it again.
4. **Confirm with the real render step** if the converter is available, because it also checks the LaTeX of
   `formula()`, which the checker cannot. The converter reads `content/<document>/` in the folder it runs in, so
   render a temporary copy:
   ```bash
   tmp=$(mktemp -d) && mkdir "$tmp/content" && cp -r <document folder> "$tmp/content/" && \
     (cd "$tmp" && PYTHONDONTWRITEBYTECODE=1 uv run --project <env> --no-sync \
       python -m viva_publisher_converter.md_render --document <document name>); echo "exit $?"; rm -rf "$tmp"
   ```
   `<env>` is a project whose environment has the converter: the user's project if `uv run python -c "import
   viva_publisher_converter"` works there, otherwise a converter checkout (e.g. `~/viva-publisher-converter`).
   It prints the problems with their file and line, or exits with 0. If no converter is available, say so.
   A Jinja syntax error (e.g. `expected token ',', got 'Entwurf'`: a `'` inside a `'…'` string) makes the render
   step drop that whole file, and with it its anchors: every `ref()` to them, also in other files, then reports
   «no anchor». Fix the syntax error first; those messages go away with it.
5. **Report.** Say what you changed and what is still open: placeholders, refs to targets that don't exist yet,
   pictures that look wrong, anything you couldn't decide, and whether the real render step ran.

## From source text to commands

Much stays plain Markdown: `**bold**`, `*italic*`, `` `code` ``, `<br>` (line break inside a paragraph), lists
`-` / `1.` (nested with 4 spaces; a numbered list starts at its first number), `[text](url)`, code fences and
escapes (`3\. Schritt`, `\# kein Titel`, `2\*3`). For everything else:

| In the source | Write |
| --- | --- |
| chapter title | exactly one `# Title {{ anchor('kap_…') }}` as the first line; `##`/`###` are numbered (1.1, 1.1.1), `####` is an unnumbered subheading. Do not type the numbers yourself. |
| picture + «Abbildung 3: Aufbau» | `{{ image('images/aufbau.png', title='Aufbau', anchor='abb_aufbau') }}` on its own line. Drop «Abbildung n:» because the converter numbers the caption. Leave out `width` unless the picture should be smaller: without it the picture keeps its native size (pixels ÷ dpi, at most the text column), and a larger `width` blows it up and blurs it. |
| picture not yet available | `((aufbau.png))` placeholder. An `image()` pointing to a missing file is a problem. |
| «siehe Abbildung 3 / Tabelle 2 / Abschnitt 1.2» | `{{ ref('abb_aufbau') }}` (`'title'`, `'page'` for title or page) + an anchor on the target. Never hard-code numbers. |
| table + «Tabelle 2: Werte» | `Tabelle: Werte` directly above the table (no blank line), `{{ table(…widths…) }}` or `{% call table(…) %}` around it |
| merged cells, multi-line cells, `\|` in a cell | an HTML `<table>` (pipe tables cannot do these) |
| a solution in a table cell (red), an aligned or turned cell | on a `<td>`/`<th>` of an HTML table: `solution` without a value (`<td solution>X</td>`: the cell's text in the style Solutions, red by the template), `align="center"`/`"right"`, `valign="middle"`/`"bottom"`, `vertical="up"`/`"down"` |
| pictures side by side / text beside a picture | `{% call table(…, type='pictures') %}` / `type='layout'` |
| formula (`$…$`, Word equation) | `{{ formula('U = R \cdot I') }}`: inline in the sentence, or on its own line for a display formula. `$…$` stays text. |
| footnote `[^1]` | `{{ footnote('Text') }}` right after the word, no space before it |
| literature reference «[1]», «(Meier 1999, S. 23)» | `{{ cite('meier1999', '23') }}` + `meier1999: …` line in the sources file + `bibliography()` in the manifest |
| keyword for the index | `{{ index('Motor') }}Motor` directly before its word, inline only |
| learning objectives | `{{ label('Lernziele', icon='learning_objective') }}`, blank line, `{% call learning_objectives() %}` with rows `\| LZ_0101 \| Sie erklären … \|` |
| «Hinweis» box | `{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}`, blank line, `{{ note() }}` directly above the paragraph/list, or `{% call note() %}` … `{% endcall %}` for several blocks |
| «Hinweis» label above a normal paragraph (no box) | `{{ label('Hinweis', icon='bell', offset_x='4mm') }}`, blank line, the paragraph. No `offset_y`: it reaches into a `note()` box and is a problem without one. |
| example / summary / link to a quiz | `label('Beispiel', icon='magnifying_glass')`, `label('Zusammenfassung', icon='summary')`, `label('Selbstkontrolle', icon='arrow_right', link='https://…')` + `{{ qr_code('https://…') }}` |
| exercise, solution, other boxes | `> [!AUFGABE] Aufgabe 1: Titel` then `> text` lines; also `LOESUNG`, `HINWEIS`, `MERKSATZ`, `LERNZIEL`, `SELBSTKONTROLLE`, `KOMMENTAR` (an unknown kind becomes a Hinweis) |
| definition that should stand out | `{{ frame() }}` directly above the paragraph (`color=`, `background=`, `thickness=`) |
| coloured warning text | `{{ color('Lebensgefahr!') }}` (default signal red) |
| note for the editor, visible in Word | `<!-- … -->` becomes an author comment in Word (style Author Comment) |
| note that must not appear anywhere | `{# … #}` or `[//]: # (…)` |
| forced page break | `{{ page_break() }}`, sparingly; the styles do the layout |

## Rules that the render step enforces

These are the mistakes the render step most often rejects. The full lists are in COMMANDS.md.

- **Syntax.** Write `{{ name(…) }}` with spaces inside the braces. Strings go in `'…'`; a text containing `'` goes
  in `"…"`. Positional arguments only in the documented order. Unknown, missing or doubled arguments are problems.
- **LaTeX is written as is**, with single backslashes: `formula('\frac{U}{R}')`, decimal comma `0{,}5`, units
  `5\,\text{m}`.
- **Placement.** Block commands stand on a line of their own with blank lines around them: `image`, `label`,
  `qr_code`, `grid`, `page_break`. `image()` may also sit in a table cell. There are two exceptions:
  `note()`/`frame()` stand *directly* above their paragraph or list, and the line form of `table()`/
  `learning_objectives()` stands *directly* above the table (or its `Tabelle:` line). `index`, `link`, `color`,
  `footnote`, `ref`, `cite` are inline. `anchor()` goes at the end of a heading. `uuid()` goes at the very end of
  its heading or paragraph.
- **`note()` takes no text.** Its paragraph is the next line: `{{ note('Text') }}` is a problem («takes 0
  positional arguments»). A `label()` with `offset_y` needs a `note()` as the next block.
- **Enclosing calls.** `{% call x() %}` and `{% endcall %}` each stand on a line of their own. The only
  exception is `content()` inside a cell. A `note`/`frame` call holds only paragraphs, lists and `formula()`
  lines. A `table` call holds only the `Tabelle:` line and the table. `list()` and `content()` exist only as calls.
- **Tables.** Give one width per column, either `cm`/`mm`/`pt`/`%` or `*` (the `*` columns share the rest). The
  fixed widths add up to at most the 16 cm text column. `anchor=` and `numbered=False` need the `Tabelle:` line.
  Tables with `type='pictures'` or `type='layout'` have no `Tabelle:` line.
- **Pictures.** Paths are relative to the calling file (a leading `/` means relative to the manifest folder) and
  the file must exist. `scale` cannot be combined with `width`/`height`. `numbered`/`anchor` only work with
  `title`. In a table cell, `wrap`/`title` are not allowed, except `title` inside `type='layout'`.
- **Names.** An anchor name or citation key is a letter followed by letters, digits, `-` or `_`, at most 40
  characters, and is unique across the whole document. Follow the demo's prefixes: `kap_`, `abb_`, `tab_`.
- **uuids.** `uuid=` / `uuid()` are optional and identify a block in Word. The Word imports write them. **Keep
  existing uuids exactly where they are**, because they connect later Word edits back to the Markdown. Never
  invent a uuid by hand or copy one. Each must be a version-4 UUID and unique per document. Don't add new ones
  unless asked. When fixing a duplicate or an invalid uuid, give the copy a fresh one:
  `python3 -c "import uuid; print(uuid.uuid4())"`.
- **Showing a command as text.** Jinja also runs calls inside code fences and code spans. To show a call
  literally, wrap it in `{% raw %}` … `{% endraw %}`, as the demo does.
- **Manifest.** It holds only calls, one per line, plus `{# … #}` comments. `title()`, `logo()`, `watermark()` and
  `bibliography()` appear at most once. Each chapter file must appear in a `chapter()` call, otherwise it is not
  part of the document; the checker warns about such orphans.

## Starting a new document

Mirror `<skill>/assets/demo_starter/`: create a document folder (in an author project
`content/2_md_content/<name>/`) with `_main_.md`, `cover.md` (and `impressum.md` if the cover has a picture), one
file per chapter (`_1_….md`, `_2_….md`), an `images/` folder, and `glossar.md`/`quellen.md` if they are needed.
Start from a copy of the demo's `_main_.md` and remove the entries you don't need. Don't copy whole demo chapters:
they carry the demo's uuids, and a copied uuid connects the new document to the wrong Word blocks. Then run the
checker on the new folder.
