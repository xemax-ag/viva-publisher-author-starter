#!/usr/bin/env python3
r"""Pre-check the Markdown files of a viva publisher document against the rules of COMMANDS.md.

    python3 check_commands.py <document folder | _main_.md | chapter.md> [more files …]

Given a document folder (or any file in it) it finds the manifest `_main_.md`, follows its calls to the cover,
imprint, management summary, chapters, glossar and sources files and checks them together: call syntax and
arguments, where each command may stand, the files it names, and over the whole document the uuids, anchors,
ref() targets and cite() keys. Without a manifest only the given files are checked (no cross-file checks).

A pre-check, not the render step: it does not run Jinja and does not convert LaTeX (it only checks braces and
\begin/\end). Calibrated against the converter's md_render: `error` = the render step rejects it, `warning` = the
render step accepts it but COMMANDS.md advises against it or the result is likely not what was meant, `info` =
open items. Output `file:line: level: message`; exit code 1 if any error.
"""
from __future__ import annotations

import ast
import re
import sys
import warnings
from bisect import bisect_right
from dataclasses import dataclass, field
from pathlib import Path


# --------------------------------------------------------------------------- command table (COMMANDS.md overview)

@dataclass(frozen=True)
class Spec:
    params: tuple[str, ...] = ()      # in positional order
    required: tuple[str, ...] = ()
    varargs: str | None = None        # *widths of table(), *keys of link_lo()
    kwonly: tuple[str, ...] = ()
    where: str = 'chapter'            # 'manifest' | 'both' | 'chapter'
    forms: str = 'expr'               # 'expr' ({{ }}) | 'call' ({% call %}) | 'both'
    own_line: bool = False


IMAGE_PARAMS = ('src', 'width', 'height', 'scale', 'align', 'border', 'crop', 'wrap', 'title', 'numbered',
                'anchor', 'alt_text', 'rotate')

SPECS: dict[str, Spec] = {
    'title': Spec(('text',), ('text',), where='manifest'),
    'logo': Spec(('name',), ('name',), where='manifest'),
    'watermark': Spec(('text', 'color'), ('text',), where='manifest'),
    'cover': Spec(('src', 'image'), where='manifest'),
    'imprint': Spec(('src', 'top'), where='manifest'),
    'management_summary': Spec(('src',), where='manifest'),
    'table_of_contents': Spec(where='manifest'),
    'chapter': Spec(('src', 'image'), ('src',), where='manifest'),
    'list_of_illustrations': Spec(('unnumbered',), where='manifest'),
    'list_of_tables': Spec(('unnumbered',), where='manifest'),
    'glossar': Spec(('src',), where='manifest'),
    'bibliography': Spec(('src', 'title'), where='manifest'),
    'keyword_index': Spec(where='manifest'),
    'image': Spec(IMAGE_PARAMS, ('src',), where='both', own_line=True),
    'page_break': Spec(where='both', own_line=True),
    'index': Spec(('entry', 'sub'), ('entry',)),
    'link': Spec(('url', 'text'), ('url',)),
    'color': Spec(('text', 'color'), ('text',)),
    'footnote': Spec(('text',), ('text',)),
    'anchor': Spec(('name',), ('name',)),
    'ref': Spec(('name', 'show'), ('name',)),
    'cite': Spec(('key', 'page'), ('key',)),
    'formula': Spec(('tex', 'align'), ('tex',)),
    'table': Spec(varargs='widths', kwonly=('type', 'anchor', 'numbered'), forms='both', own_line=True),
    'learning_objectives': Spec(varargs='widths', forms='both', own_line=True),
    'link_lo': Spec(varargs='keys'),
    'qr_code': Spec(('text', 'size', 'color', 'alignment'), own_line=True),
    'grid': Spec(('spacing', 'n_width', 'n_height', 'thickness', 'color', 'alignment'), own_line=True),
    'label': Spec(('text', 'icon', 'link', 'offset_x', 'offset_y'), ('text',), own_line=True),
    'list': Spec(forms='call', own_line=True),
    'note': Spec(forms='both', own_line=True),
    'frame': Spec(('color', 'background', 'thickness'), forms='both', own_line=True),
    'content': Spec(('uuid',), ('uuid',), forms='call'),
    'uuid': Spec(('uuid',), ('uuid',)),
}
ONCE = {'title', 'logo', 'watermark', 'bibliography'}
BLOCK_CALLS = {'image', 'page_break', 'table', 'learning_objectives', 'qr_code', 'grid', 'label', 'note',
               'frame', 'list'}
ICONS = {'learning_objective', 'bell', 'magnifying_glass', 'arrow_right', 'summary'}  # reference/template/icons/
KNOWN_CALLOUTS = {'HINWEIS', 'NOTE', 'TIP', 'IMPORTANT', 'WARNING', 'CAUTION', 'MERKSATZ', 'LERNZIEL', 'AUFGABE',
                  'LOESUNG', 'LÖSUNG', 'SOLUTION', 'SELBSTKONTROLLE', 'KOMMENTAR', 'COMMENT'}
TEXT_WIDTH_CM = 16.0

UUID4_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.I)
GUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.I)
NAME_RE = re.compile(r'^[A-Za-z][A-Za-z0-9_-]{0,39}$')
COLOR_RE = re.compile(r'^#[0-9A-Fa-f]{6}$')
URL_RE = re.compile(r'^(https?://|mailto:)\S+$')
LEN_RE = re.compile(r'^\s*(\d+(?:[.,]\d+)?)\s*(cm|mm|pt|in|px|%)\s*$')
UNIT_CM = {'cm': 1.0, 'mm': 0.1, 'pt': 2.54 / 72, 'in': 2.54, 'px': 2.54 / 96}
ALIGNS = ('left', 'center', 'right')

RAW_RE = re.compile(r'\{%-?\s*raw\s*-?%\}.*?\{%-?\s*endraw\s*-?%\}', re.S)
MD_COMMENT_RE = re.compile(r'^\[//\]: #(?: *\(.*\)| *".*"| *\'.*\')?[ \t]*$')
FENCE_RE = re.compile(r'^\s*(```|~~~)')
HEADING_RE = re.compile(r'^(#{1,6})\s')
LIST_ITEM_RE = re.compile(r'^\s*([-*+]|\d+[.)])\s')
PLACEHOLDER_RE = re.compile(r'\(\(([^()\s]+\.[A-Za-z0-9]+)\)\)')
MD_IMAGE_RE = re.compile(r'!\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
CALLOUT_RE = re.compile(r'^\s*>\s*\[!([A-Za-z_]+)\]')


# --------------------------------------------------------------------------- reporting

@dataclass
class Report:
    items: list[tuple[str, int, str, str]] = field(default_factory=list)

    def add(self, level: str, path: Path, line: int, msg: str) -> None:
        self.items.append((str(rel(path)), line, level, msg))

    def error(self, path, line, msg):
        self.add('error', path, line, msg)

    def warn(self, path, line, msg):
        self.add('warning', path, line, msg)

    def info(self, path, line, msg):
        self.add('info', path, line, msg)


def rel(path: Path) -> Path:
    try:
        return path.resolve().relative_to(Path.cwd().resolve())
    except ValueError:
        return path


# --------------------------------------------------------------------------- scanning

def find_close(text: str, pos: int, close: str) -> int:
    """Index of `close` after pos, skipping quoted strings (with backslash escapes, as Jinja reads them)."""
    quote = None
    i = pos
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == '\\':
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in '\'"':
            quote = ch
        elif text.startswith(close, i):
            return i
        i += 1
    return -1


def blank(text: str, start: int, end: int) -> str:
    """text with [start, end) replaced by spaces, newlines kept (line numbers stay)."""
    return text[:start] + re.sub(r'[^\n]', ' ', text[start:end]) + text[end:]


def rawify(expr: str) -> str:
    """Prefix every string literal with r, so LaTeX like '\\frac' or '\\xi' parses as written."""
    out, quote, i = [], None, 0
    while i < len(expr):
        ch = expr[i]
        if quote:
            if ch == '\\' and i + 1 < len(expr):
                out.append(expr[i:i + 2])
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in '\'"':
            quote = ch
            prev = expr[i - 1] if i else ''
            if not (prev.isalnum() or prev == '_'):
                out.append('r')
        out.append(ch)
        i += 1
    return ''.join(out)


_CONSTS = {'true': True, 'false': False, 'none': None, 'True': True, 'False': False, 'None': None}


def literal(node: ast.AST):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name) and node.id in _CONSTS:
        return _CONSTS[node.id]
    if (isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd))
            and isinstance(node.operand, ast.Constant) and isinstance(node.operand.value, (int, float))):
        return -node.operand.value if isinstance(node.op, ast.USub) else node.operand.value
    raise ValueError(ast.dump(node))


def parse_call(expr: str):
    """('name', [positional], [(key, value)]) or an error string."""
    expr = expr.strip().strip('-').strip()
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            tree = ast.parse(rawify(expr), mode='eval')
    except SyntaxError as e:
        return f'cannot read the call `{expr[:60]}`: {e.msg}'
    node = tree.body
    if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)):
        return f'`{expr[:60]}` is no command call `name(…)`'
    try:
        pos = []
        for a in node.args:
            if isinstance(a, ast.Starred):
                raise ValueError
            pos.append(literal(a))
        kws = []
        for k in node.keywords:
            if k.arg is None:
                raise ValueError
            kws.append((k.arg, literal(k.value)))
    except ValueError:
        return f'arguments of `{node.func.id}()` must be literals (\'text\', "text", numbers, True/False/None)'
    return node.func.id, pos, kws


# --------------------------------------------------------------------------- per-file model

@dataclass
class Call:
    name: str
    args: dict
    form: str            # 'expr' | 'call'
    line: int            # 0-based line of the tag start
    end_line: int        # 0-based line of the tag end
    start: int
    end: int
    alone: bool
    parents: tuple[str, ...]
    in_fence: bool
    in_code_span: bool
    close_line: int | None = None    # line of its {% endcall %}
    close_alone: bool = True


class Doc:
    """One Markdown file: masked text (raw, comments removed) and its calls."""

    def __init__(self, path: Path, text: str, report: Report):
        self.path, self.report = path, report
        self.text = text
        masked = text
        for m in RAW_RE.finditer(text):
            masked = blank(masked, m.start(), m.end())
        lines = masked.split('\n')
        fence = False
        self.fence_lines: set[int] = set()
        for i, ln in enumerate(lines):
            if FENCE_RE.match(ln):
                self.fence_lines.add(i)
                fence = not fence
                continue
            if fence:
                self.fence_lines.add(i)
            elif MD_COMMENT_RE.match(ln):
                lines[i] = ' ' * len(ln)
        masked = '\n'.join(lines)
        self.line_starts = [0]
        for m in re.finditer('\n', masked):
            self.line_starts.append(m.end())

        self.calls: list[Call] = []
        self.endcalls: list[tuple[int, bool, str]] = []   # line, alone, name of its call
        flat = masked
        stack: list[Call] = []
        i = 0
        open_re = re.compile(r'\{\{|\{%|\{#')
        tags = []
        while True:
            m = open_re.search(masked, i)
            if not m:
                break
            s = m.start()
            if m.group() == '{#':
                e = masked.find('#}', s + 2)
                e = len(masked) if e < 0 else e + 2
                tags.append(('comment', s, e, ''))
                i = e
                continue
            close = '}}' if m.group() == '{{' else '%}'
            e = find_close(masked, s + 2, close)
            if e < 0:
                report.error(path, self.lineno(s) + 1, f'`{m.group()}` without its closing `{close}`')
                break
            tags.append(('expr' if close == '}}' else 'stmt', s, e + 2, masked[s + 2:e]))
            i = e + 2
        for kind, s, e, _ in tags:
            if kind == 'comment':
                masked = blank(masked, s, e)
        for kind, s, e, _ in tags:
            flat = blank(flat, s, e) if kind == 'comment' else flat[:s] + re.sub(r'[^\n]', 'x', flat[s:e]) + flat[e:]
        self.masked = masked
        self.lines = masked.split('\n')
        self.flat_lines = flat.split('\n')
        self.html_lines = self._html_regions()

        for kind, s, e, inner in tags:
            if kind == 'comment':
                continue
            ln, eln = self.lineno(s), self.lineno(e - 1)
            alone = self._alone(s, e)
            in_fence = ln in self.fence_lines
            in_span = self.flat_lines[ln][:s - self.line_starts[ln]].count('`') % 2 == 1
            if kind == 'stmt':
                body = inner.strip().strip('-').strip()
                if body == 'endcall':
                    if not stack:
                        report.error(path, ln + 1, '`{% endcall %}` without its `{% call … %}`')
                    else:
                        c = stack.pop()
                        self.endcalls.append((ln, alone, c.name))
                        c.close_line, c.close_alone = ln, alone
                    continue
                if body in ('raw', 'endraw'):
                    report.error(path, ln + 1, f'`{{% {body} %}}` without its partner')
                    continue
                m = re.match(r'call\s+(\w+\s*\(.*)$', body, re.S)
                if not m:
                    report.warn(path, ln + 1, f'Jinja statement `{{% {body[:40]} %}}` is none of the commands')
                    continue
                form, expr = 'call', m.group(1)
            else:
                form, expr = 'expr', inner
            parsed = parse_call(expr)
            if isinstance(parsed, str):
                report.error(path, ln + 1, parsed + (' (in code, too: Jinja reads it; use {% raw %})'
                                                     if in_fence or in_span else ''))
                continue
            name, pos, kws = parsed
            spec = SPECS.get(name)
            if spec is None:
                report.error(path, ln + 1, f'unknown command `{name}()` (see the overview in COMMANDS.md)')
                continue
            args = self._bind(name, spec, pos, kws, ln)
            call = Call(name, args, form, ln, eln, s, e, alone, tuple(c.name for c in stack), in_fence, in_span)
            self.calls.append(call)
            if form == 'call':
                stack.append(call)
        for c in stack:
            report.error(path, c.line + 1, f'`{{% call {c.name}() %}}` without its `{{% endcall %}}`')

    # ---- helpers
    def lineno(self, offset: int) -> int:
        return bisect_right(self.line_starts, offset) - 1

    def _alone(self, s: int, e: int) -> bool:
        """The tag is the only thing on its line(s) (a leading `>` of a box line does not count)."""
        ls, le = self.lineno(s), self.lineno(e - 1)
        line_end = self.line_starts[le + 1] - 1 if le + 1 < len(self.line_starts) else len(self.masked)
        before, after = self.masked[self.line_starts[ls]:s], self.masked[e:line_end]
        return before.strip(' \t>') == '' and after.strip() == ''

    def _bind(self, name: str, spec: Spec, pos: list, kws: list, ln: int) -> dict:
        args: dict = {}
        if spec.varargs:
            args[spec.varargs] = list(pos)
            allowed = set(spec.kwonly) | {'uuid'}
        else:
            if len(pos) > len(spec.params):
                self.report.error(self.path, ln + 1, f'`{name}()` takes at most {len(spec.params)} positional '
                                                     f'argument(s) ({", ".join(spec.params) or "none"})')
            args.update(zip(spec.params, pos))
            allowed = set(spec.params) | {'uuid'}
        for k, v in kws:
            if k not in allowed:
                self.report.error(self.path, ln + 1, f'`{name}()` has no argument `{k}=`'
                                  + (' (the keys go by position)' if name == 'link_lo' else ''))
            elif k in args:
                self.report.error(self.path, ln + 1, f'`{name}()`: argument `{k}` given twice')
            else:
                args[k] = v
        for r in spec.required:
            if r not in args:
                self.report.error(self.path, ln + 1, f'`{name}()` needs `{r}`')
        return args

    def _html_regions(self) -> set[int]:
        out, start = set(), None
        for i, ln in enumerate(self.lines):
            if start is None and ln.lstrip().startswith('<table'):
                start = i
            if start is not None:
                out.add(i)
                if '</table>' in ln:
                    start = None
        if start is not None:
            self.report.error(self.path, start + 1, '`<table` without `</table>`')
        return out

    def is_pipe(self, i: int) -> bool:
        return 0 <= i < len(self.lines) and self.lines[i].lstrip().startswith('|')

    def in_cell(self, i: int) -> bool:
        return self.is_pipe(i) or i in self.html_lines

    def is_blank(self, i: int) -> bool:
        return not (0 <= i < len(self.lines)) or self.lines[i].strip() == ''

    def next_nonblank(self, i: int) -> int:
        j = i + 1
        while j < len(self.lines) and self.lines[j].strip() == '':
            j += 1
        return j

    def lone_call_at(self, i: int) -> Call | None:
        for c in self.calls:
            if c.line == i and c.alone:
                return c
        return None

    def table_at(self, i: int):
        """Table starting at line i (optionally after its `Tabelle:` line): (caption, kind, first, last, ncols)."""
        caption = False
        if 0 <= i < len(self.lines) and self.lines[i].lstrip().startswith('Tabelle:'):
            caption, i = True, i + 1
        if self.is_pipe(i):
            j = i
            while self.is_pipe(j + 1):
                j += 1
            row = re.sub(r'`[^`]*`', 'x', self.flat_lines[i].replace('\\|', 'x')).strip()
            return caption, 'pipe', i, j, len(row.strip('|').split('|'))
        if 0 <= i < len(self.lines) and self.lines[i].lstrip().startswith('<table'):
            j = i
            while j < len(self.lines) - 1 and '</table>' not in self.lines[j]:
                j += 1
            return caption, 'html', i, j, self._html_cols('\n'.join(self.flat_lines[i:j + 1]), i)
        return caption, None, i, i, 0

    def _html_cols(self, html: str, ln: int) -> int:
        occupied: set[tuple[int, int]] = set()
        width = 0
        for r, row in enumerate(re.findall(r'<tr\b[^>]*>(.*?)</tr>', html, re.S | re.I)):
            c = 0
            for attrs in re.findall(r'<t[dh]\b([^>]*)>', row, re.I):
                while (r, c) in occupied:
                    c += 1
                spans = []
                for att in ('colspan', 'rowspan'):
                    m = re.search(att + r'\s*=\s*["\']?([^"\'\s>]+)', attrs)
                    val = m.group(1) if m else '1'
                    if not val.isdigit() or int(val) < 1:
                        self.report.error(self.path, ln + 1, f'`{att}="{val}"` is no whole number from 1')
                        val = '1'
                    spans.append(int(val))
                for dr in range(spans[1]):
                    for dc in range(spans[0]):
                        occupied.add((r + dr, c + dc))
                c += spans[0]
            width = max(width, c, max((cc + 1 for rr, cc in occupied if rr == r), default=0))
        return width


# --------------------------------------------------------------------------- value checks

def length_cm(value, units: tuple[str, ...]):
    if not isinstance(value, str):
        return None
    m = LEN_RE.match(value)
    if not m or m.group(2) not in units:
        return None
    n = float(m.group(1).replace(',', '.'))
    return n if m.group(2) == '%' else n * UNIT_CM[m.group(2)]


class Checker:
    def __init__(self, report: Report):
        self.r = report
        self.uuids: dict[str, tuple[Path, int]] = {}
        self.anchors: dict[str, tuple[Path, int]] = {}
        self.refs: list[tuple[str, Path, int]] = []
        self.cites: list[tuple[str, Path, int]] = []
        self.once: dict[str, tuple[Path, int]] = {}
        self.manifest: Path | None = None
        self.bibliography: Path | None = None
        self.table_ctx: dict[int, Call] = {}   # line of a table row -> its table()/learning_objectives() call
        self.table_caption: dict[int, bool] = {}

    # ---- small validators
    def need(self, cond, doc, c, msg):
        if not cond:
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: {msg}')
        return cond

    def text_arg(self, doc, c, key, required=True):
        v = c.args.get(key)
        if v is None and not required:
            return
        self.need(isinstance(v, str) and v.strip() != '', doc, c, f'`{key}` must be a non-empty string')

    def color_arg(self, doc, c, key):
        v = c.args.get(key)
        if v is not None:
            self.need(isinstance(v, str) and COLOR_RE.match(v), doc, c, f'`{key}={v!r}` is no colour `#RRGGBB`')

    def choice_arg(self, doc, c, key, choices):
        v = c.args.get(key)
        if v is not None:
            self.need(v in choices, doc, c, f'`{key}={v!r}`: one of {", ".join(map(repr, choices))}')

    def len_arg(self, doc, c, key, units, lo=None, hi=None):
        v = c.args.get(key)
        if v is None:
            return None
        n = length_cm(v, units)
        if not self.need(n is not None, doc, c, f'`{key}={v!r}`: a length in {", ".join(units)}'):
            return None
        if lo is not None and n < lo - 1e-9 or hi is not None and n > hi + 1e-9:
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: `{key}={v!r}` out of range')
        return n

    def url_arg(self, doc, c, key):
        v = c.args.get(key)
        if v is not None:
            self.need(isinstance(v, str) and URL_RE.match(v), doc, c,
                      f'`{key}={v!r}`: `https://…`, `http://…` or `mailto:…` without spaces')

    def bool_arg(self, doc, c, key):
        v = c.args.get(key)
        if v is not None:
            self.need(isinstance(v, bool), doc, c, f'`{key}` is True or False')

    def file_arg(self, doc, c, key, default=None) -> Path | None:
        v = c.args.get(key, default)
        if v is None:
            return None
        if not self.need(isinstance(v, str) and v.strip(), doc, c, f'`{key}` must be a file name'):
            return None
        base = self.manifest.parent if (v.startswith('/') and self.manifest) else doc.path.parent
        p = (base / v.lstrip('/')).resolve()
        if not p.is_file():
            hint = ' (a planned picture is the placeholder `((name))`)' if c.name == 'image' else ''
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: file `{v}` does not exist{hint}')
            return None
        return p

    def register_uuid(self, doc, c, value):
        if value is None:
            return
        if not (isinstance(value, str) and UUID4_RE.match(value)):
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: uuid {value!r} is no UUID of version 4')
            return
        key = value.lower()
        if key in self.uuids:
            fp, fl = self.uuids[key]
            self.r.error(doc.path, c.line + 1, f'uuid {value} used twice; first at {rel(fp)}:{fl} '
                                               '(give a copy new uuids)')
        else:
            self.uuids[key] = (doc.path, c.line + 1)

    def register_anchor(self, doc, c, name):
        if not (isinstance(name, str) and NAME_RE.match(name)):
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: anchor name {name!r}: a letter, then letters, '
                                               'digits, `-` or `_` (at most 40)')
            return
        if name in self.anchors:
            fp, fl = self.anchors[name]
            self.r.error(doc.path, c.line + 1, f'anchor `{name}` used twice; first at {rel(fp)}:{fl}')
        else:
            self.anchors[name] = (doc.path, c.line + 1)

    def widths(self, doc, c) -> list[float | None]:
        out = []
        for w in c.args.get('widths', []):
            if w == '*':
                out.append(None)
                continue
            n = length_cm(w, ('cm', 'mm', 'pt', '%'))
            if n is None:
                self.r.error(doc.path, c.line + 1, f'`{c.name}()`: width {w!r}: cm, mm, pt, % or `*`')
                continue
            out.append(n * TEXT_WIDTH_CM / 100 if w.strip().endswith('%') else n)
        fixed = sum(x for x in out if x is not None)
        if fixed > TEXT_WIDTH_CM + 1e-6:
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: fixed widths {fixed:.2f} cm over the 16 cm text column')
        return out

    # ---- files
    def check_document(self, manifest: Path):
        self.manifest = manifest.resolve()
        doc = self.load(manifest)
        if doc is None:
            return
        self.check_manifest(doc)
        seen = {self.manifest}
        for c in doc.calls:
            for key, default, kind in self.manifest_files(c):
                p = self.file_arg(doc, c, key, default)
                if p is None or (p in seen and kind != 'image'):
                    continue
                seen.add(p)
                if kind == 'image':
                    continue
                d = self.load(p)
                if d is None:
                    continue
                if kind == 'sources':
                    self.bibliography = p
                    self.check_sources(d)
                elif kind == 'glossar':
                    self.check_glossar(d)
                self.check_content(d, kind)
                if kind == 'cover' and c.args.get('image'):
                    for i, ln in enumerate(d.lines):
                        if ln.strip() and not re.match(r'^#{1,3}\s', ln):
                            self.r.error(d.path, i + 1, 'with `cover(image=…)` the cover file holds only its '
                                                        '`#`, `##`, `###` band lines; the imprint goes to `imprint()`')
                            break
        self.check_orphans(seen)
        self.resolve(cross_file=True)

    @staticmethod
    def manifest_files(c: Call):
        defaults = {'cover': ('cover.md', 'cover'), 'imprint': ('impressum.md', 'imprint'),
                    'management_summary': ('management_summary.md', 'summary'), 'chapter': (None, 'chapter'),
                    'glossar': ('glossar.md', 'glossar'), 'bibliography': ('quellen.md', 'sources')}
        if c.name in defaults:
            default, kind = defaults[c.name]
            yield 'src', default, kind
        if c.name in ('cover', 'chapter') and c.args.get('image') is not None:
            yield 'image', None, 'image'

    def check_orphans(self, seen: set[Path]):
        folder = self.manifest.parent
        for p in sorted(folder.rglob('*.md')):
            if p.resolve() not in seen and p.name not in ('CONVERT.md', 'README.md'):
                self.r.warn(p, 1, 'Markdown file not named in the manifest (not part of the document)')

    def load(self, path: Path) -> Doc | None:
        try:
            text = path.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError) as e:
            self.r.error(path, 1, f'cannot read: {e}')
            return None
        return Doc(path, text, self.r)

    def check_manifest(self, doc: Doc):
        for i, ln in enumerate(doc.lines):
            if ln.strip() and not doc.lone_call_at(i) and not any(c.line < i <= c.end_line for c in doc.calls):
                self.r.error(doc.path, i + 1, 'the manifest holds only calls, one per line, and `{# … #}` comments')
        for c in doc.calls:
            self.check_call(doc, c, 'manifest')
            if c.name in ONCE or SPECS[c.name].where == 'manifest' and c.name != 'chapter':
                if c.name in self.once:
                    fp, fl = self.once[c.name]
                    (self.r.error if c.name in ONCE else self.r.warn)(
                        doc.path, c.line + 1, f'`{c.name}()` a second time (first at line {fl})')
                else:
                    self.once[c.name] = (doc.path, c.line + 1)
            if c.form == 'call':
                self.r.error(doc.path, c.line + 1, 'no `{% call %}` in the manifest')

    def check_content(self, doc: Doc, kind: str):
        for c in doc.calls:
            self.check_call(doc, c, kind)
        for ln, alone, name in doc.endcalls:
            if not alone and name != 'content':
                self.r.error(doc.path, ln + 1, '`{% endcall %}` stands on a line of its own')
        self.check_lines(doc, kind)

    def check_lines(self, doc: Doc, kind: str):
        headings = [i for i, ln in enumerate(doc.lines) if i not in doc.fence_lines and HEADING_RE.match(ln)]
        if kind == 'chapter':
            tops = [i for i in headings if doc.lines[i].startswith('# ')]
            first = doc.next_nonblank(-1)
            if not tops or tops[0] != first:
                self.r.warn(doc.path, first + 1, 'a chapter starts with its one `#` heading')
            for i in tops[1:]:
                self.r.warn(doc.path, i + 1, 'a second `#` heading in a chapter file (a chapter has exactly one)')
        for i, ln in enumerate(doc.lines):
            if ln.lstrip().startswith('<table') and i not in doc.fence_lines and i not in self.table_ctx:
                doc.table_at(i)   # checks colspan/rowspan of a table without table()
        for i, ln in enumerate(doc.lines):
            if i in doc.fence_lines:
                continue
            s = ln.strip()
            if s.startswith('Tabelle:'):
                if not s[len('Tabelle:'):].strip():
                    self.r.warn(doc.path, i + 1, '`Tabelle:` line without a title')
                if not (doc.is_pipe(i + 1) or doc.lines[i + 1].lstrip().startswith('<table')
                        if i + 1 < len(doc.lines) else False):
                    self.r.warn(doc.path, i + 1, 'a `Tabelle: …` line not directly above its table becomes body text: '
                                                 'no «Tabelle n:» caption, no entry in the list of tables')
            m = CALLOUT_RE.match(ln)
            if m and m.group(1) not in KNOWN_CALLOUTS:
                self.r.warn(doc.path, i + 1, f'box `[!{m.group(1)}]` is unknown and becomes a Hinweis; known: '
                                             f'{", ".join(sorted(KNOWN_CALLOUTS))}')
            for m in PLACEHOLDER_RE.finditer(ln):
                self.r.info(doc.path, i + 1, f'placeholder for a planned picture: {m.group(1)}')
            for m in MD_IMAGE_RE.finditer(doc.flat_lines[i]):
                src = ln[m.start(1):m.end(1)]
                if not re.match(r'^[a-z]+://', src) and not (doc.path.parent / src).is_file():
                    self.r.error(doc.path, i + 1, f'picture `{src}` does not exist')

    def check_glossar(self, doc: Doc):
        for i, ln in self.data_lines(doc):
            if not re.match(r'^[^:]+:\s*\S', ln):
                self.r.warn(doc.path, i + 1, 'glossar line is not `Begriff: Definition`, so it is no entry')

    def check_sources(self, doc: Doc):
        self.source_keys: dict[str, int] = {}
        for i, ln in self.data_lines(doc):
            m = re.match(r'^([^:\s]+):\s*(\S.*)$', ln)
            if not m or not NAME_RE.match(m.group(1)):
                self.r.error(doc.path, i + 1, 'sources line is not `key: entry` (key: a letter, then letters, '
                                              'digits, `-` or `_`, at most 40)')
                continue
            if m.group(1) in self.source_keys:
                self.r.error(doc.path, i + 1, f'key `{m.group(1)}` twice (first at line {self.source_keys[m.group(1)]})')
            else:
                self.source_keys[m.group(1)] = i + 1

    @staticmethod
    def data_lines(doc: Doc):
        text = re.sub(r'<!--.*?-->', lambda m: re.sub(r'[^\n]', ' ', m.group()), doc.masked, flags=re.S)
        for i, ln in enumerate(text.split('\n')):
            if ln.strip() and not HEADING_RE.match(ln):
                yield i, ln.strip()

    # ---- one call
    def check_call(self, doc: Doc, c: Call, kind: str):
        spec = SPECS[c.name]
        if c.in_fence or c.in_code_span:
            where = 'a code block' if c.in_fence else 'a code span'
            self.r.warn(doc.path, c.line + 1, f'`{c.name}()` in {where} is run by Jinja; to show it as text put it '
                                              'between `{% raw %}` and `{% endraw %}`')
            if c.name in ('image', 'chapter', 'cover'):   # its file is still read
                self.file_arg(doc, c, 'src')
            return
        if kind == 'manifest' and spec.where == 'chapter':
            self.r.error(doc.path, c.line + 1, f'`{c.name}()` stands in a chapter file, not in the manifest')
            return
        if kind != 'manifest' and spec.where == 'manifest':
            self.r.error(doc.path, c.line + 1, f'`{c.name}()` stands only in the manifest')
            return
        if c.form == 'expr' and spec.forms == 'call':
            self.r.error(doc.path, c.line + 1, f'`{c.name}()` only as `{{% call {c.name}(…) %}}` … `{{% endcall %}}`')
        if c.form == 'call' and spec.forms == 'expr':
            self.r.error(doc.path, c.line + 1, f'`{c.name}()` encloses nothing; write `{{{{ {c.name}(…) }}}}`')
        in_cell = doc.in_cell(c.line)
        if spec.own_line and not c.alone and not (c.name == 'image' and in_cell):
            self.r.error(doc.path, c.line + 1, f'`{c.name}()` stands on a line of its own')
        if c.name != 'uuid' and c.name != 'content':
            self.register_uuid(doc, c, c.args.get('uuid'))
        if c.parents and c.parents[-1] in ('note', 'frame') and (
                c.name in BLOCK_CALLS - {'list'} or c.name == 'list' and c.parents[-1] == 'frame'):
            self.r.error(doc.path, c.line + 1, f'`{c.name}()` inside `{{% call {c.parents[-1]}() %}}`: only '
                                               'paragraphs, lists and `formula()` lines')
        getattr(self, 'c_' + c.name, lambda *_: None)(doc, c)

    # ---- manifest commands
    def c_title(self, doc, c):
        self.text_arg(doc, c, 'text')

    def c_logo(self, doc, c):
        v = c.args.get('name')
        self.need(isinstance(v, str) and re.match(r'^[A-Za-z0-9_-]+$', v), doc, c,
                  '`name` is a file prefix of letters, digits, `-`, `_`')

    def c_watermark(self, doc, c):
        self.text_arg(doc, c, 'text')
        self.need('\n' not in str(c.args.get('text', '')), doc, c, '`text` is one line')
        self.color_arg(doc, c, 'color')

    def c_imprint(self, doc, c):
        self.len_arg(doc, c, 'top', ('mm', 'cm', 'pt'), 3.52, 27.33)

    def c_list_of_illustrations(self, doc, c):
        self.bool_arg(doc, c, 'unnumbered')

    c_list_of_tables = c_list_of_illustrations

    def c_bibliography(self, doc, c):
        self.text_arg(doc, c, 'title', required=False)

    # ---- pictures and blocks
    def c_image(self, doc, c):
        a = c.args
        self.file_arg(doc, c, 'src')
        self.len_arg(doc, c, 'width', ('cm', 'mm', 'pt', '%'))
        self.len_arg(doc, c, 'height', ('cm', 'mm', 'pt'))
        self.len_arg(doc, c, 'scale', ('%',))
        self.choice_arg(doc, c, 'align', ALIGNS)
        for b in ('border', 'wrap', 'numbered'):
            self.bool_arg(doc, c, b)
        if a.get('scale') is not None:
            self.need(a.get('width') is None and a.get('height') is None, doc, c, '`scale` not with `width`/`height`')
        if a.get('wrap'):
            self.need(a.get('align') != 'center', doc, c, '`wrap=True` not with `align=\'center\'`')
        if not a.get('title'):
            self.need('numbered' not in a and a.get('anchor') is None, doc, c, '`numbered` and `anchor` only with `title`')
        if a.get('crop') is not None:
            self.need(isinstance(a['crop'], str) and re.match(r'^\s*\d+(\.\d+)?%?(\s+\d+(\.\d+)?%?){0,3}\s*$', a['crop']),
                      doc, c, '`crop`: 1 to 4 values in % (top right bottom left)')
        if a.get('rotate') is not None:
            self.need(a['rotate'] in (90, 180, 270, -90, -180, -270), doc, c, '`rotate`: ±90, ±180 or ±270')
        if a.get('anchor') is not None:
            self.register_anchor(doc, c, a['anchor'])
        if doc.in_cell(c.line):
            table = self.table_ctx.get(c.line)
            layout = table is not None and table.args.get('type') == 'layout'
            self.need(not a.get('wrap'), doc, c, '`wrap` in a table cell')
            if not layout:
                self.need(not a.get('title') and 'numbered' not in a, doc, c,
                          '`title`/`numbered` in a table cell only in a `table(type=\'layout\')`')

    def c_page_break(self, doc, c):
        pass

    def c_qr_code(self, doc, c):
        if c.args.get('text') is None:
            self.r.warn(doc.path, c.line + 1, '`qr_code()` without text: a warning sign «QR-CODE FAILURE»')
        self.len_arg(doc, c, 'size', ('cm', 'mm', 'in', 'pt'))
        self.color_arg(doc, c, 'color')
        self.choice_arg(doc, c, 'alignment', ALIGNS)

    def c_grid(self, doc, c):
        for k in ('spacing', 'thickness'):
            n = self.len_arg(doc, c, k, ('cm', 'mm', 'in', 'pt', 'px'))
            if n is not None:
                self.need(n > 0, doc, c, f'`{k}` above zero')
        for k in ('n_width', 'n_height'):
            v = c.args.get(k)
            if v is not None:
                self.need(isinstance(v, int) and not isinstance(v, bool) and v > 0, doc, c, f'`{k}` a whole number from 1')
        self.color_arg(doc, c, 'color')
        self.choice_arg(doc, c, 'alignment', ALIGNS)

    def c_label(self, doc, c):
        self.text_arg(doc, c, 'text')
        icon = c.args.get('icon')
        if icon is not None:
            self.need(isinstance(icon, str) and icon in ICONS, doc, c,
                      f'icon {icon!r} is not in the template; one of {", ".join(sorted(ICONS))}')
        self.url_arg(doc, c, 'link')
        self.len_arg(doc, c, 'offset_x', ('cm', 'mm', 'pt', '%'))
        if self.len_arg(doc, c, 'offset_y', ('cm', 'mm', 'pt', '%')) is not None:
            nxt = doc.lone_call_at(doc.next_nonblank(c.end_line))
            self.need(nxt is not None and nxt.name == 'note', doc, c, '`offset_y` needs a `note()` as the next block')

    def block_below(self, doc, c, what):
        """note()/frame() in line form: a paragraph or list directly below (no empty line)."""
        i = c.end_line + 1
        nxt = doc.lone_call_at(i)
        bad = (doc.is_blank(i) or HEADING_RE.match(doc.lines[i]) or doc.in_cell(i)
               or doc.lines[i].lstrip().startswith(('{%', 'Tabelle:'))
               or nxt is not None and nxt.name in BLOCK_CALLS)
        self.need(not bad, doc, c, f'needs {what} directly below it (no empty line between)')

    @staticmethod
    def enclosed(doc, c):
        """Lines between `{% call %}` and `{% endcall %}` (its line too if text stands before it)."""
        if c.close_line is None:
            return range(0)
        return range(c.end_line + 1, c.close_line + (0 if c.close_alone else 1))

    def c_note(self, doc, c):
        if c.form == 'expr':
            self.block_below(doc, c, 'a paragraph or a list')
            return
        lines = self.enclosed(doc, c)
        if not any(not doc.is_blank(i) for i in lines):
            self.r.error(doc.path, c.line + 1, f'`{{% call {c.name}() %}}` with nothing inside')
        for i in lines:
            ln = doc.lines[i]
            if HEADING_RE.match(ln) or doc.in_cell(i) or ln.lstrip().startswith('Tabelle:'):
                self.r.error(doc.path, i + 1, f'inside `{{% call {c.name}() %}}`: only paragraphs, lists and '
                                              '`formula()` lines')

    def c_frame(self, doc, c):
        self.color_arg(doc, c, 'color')
        self.color_arg(doc, c, 'background')
        self.len_arg(doc, c, 'thickness', ('pt', 'mm', 'cm'), 0.25 * UNIT_CM['pt'], 6 * UNIT_CM['pt'])
        self.c_note(doc, c)

    def c_list(self, doc, c):
        if c.form != 'call':
            return
        rows = [i for i in self.enclosed(doc, c) if not doc.is_blank(i)]
        if not rows or not LIST_ITEM_RE.match(doc.lines[rows[0]]):
            self.r.error(doc.path, c.line + 1, '`{% call list() %}` holds one list, nothing else')
            return
        for i in rows:
            ln = doc.lines[i]
            if not LIST_ITEM_RE.match(ln) and not ln.startswith((' ', '\t')) and doc.is_blank(i - 1):
                self.r.error(doc.path, i + 1, 'inside `{% call list() %}`: only the one list')
                break

    # ---- tables
    def c_table(self, doc, c):
        widths = self.widths(doc, c)
        a = c.args
        lo = c.name == 'learning_objectives'
        if not lo:
            self.choice_arg(doc, c, 'type', ('default', 'pictures', 'layout'))
            self.bool_arg(doc, c, 'numbered')
        start = c.end_line + 1 if c.form == 'expr' else doc.next_nonblank(c.end_line)
        caption, kind, first, last, ncols = doc.table_at(start)
        if kind is None:
            what = 'a pipe table or an HTML table' + ('' if lo else ' (or its `Tabelle: …` line)')
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: no table directly after it; it needs {what}')
            return
        for i in range(first, last + 1):
            self.table_ctx[i] = c
        if lo:
            self.need(not caption, doc, c, 'the learning objectives have no `Tabelle: …` line')
            expected = len(widths) if widths else 2
        else:
            expected = len(widths)
            if a.get('type') in ('pictures', 'layout'):
                self.need(not caption, doc, c, f'a `type=\'{a["type"]}\'` table has no `Tabelle: …` line')
            if a.get('anchor') is not None or a.get('numbered') is False:
                self.need(caption, doc, c, '`anchor`/`numbered=False` need the `Tabelle: …` line')
            if a.get('anchor') is not None:
                self.register_anchor(doc, c, a['anchor'])
        if expected and ncols and expected != ncols:
            self.r.error(doc.path, c.line + 1, f'`{c.name}()`: {expected} width(s) for a table of {ncols} column(s)')
        if c.form == 'call':
            for i in self.enclosed(doc, c):
                if not doc.is_blank(i) and not (first - (1 if caption else 0) <= i <= last):
                    self.r.error(doc.path, i + 1, f'inside `{{% call {c.name}() %}}` only '
                                                  + ('the table' if lo else 'the `Tabelle: …` line and the table'))
                    break

    c_learning_objectives = c_table

    def c_link_lo(self, doc, c):
        keys = c.args.get('keys', [])
        self.need(keys, doc, c, 'at least one key')
        for k in keys:
            self.need(isinstance(k, str) and GUID_RE.match(k), doc, c, f'key {k!r} is no GUID 8-4-4-4-12')
        table = self.table_ctx.get(c.line)
        if not self.need(table is not None and table.name == 'learning_objectives', doc, c,
                         'only in the first cell of a `learning_objectives()` row, after the number'):
            return
        if doc.is_pipe(c.line):
            line = doc.flat_lines[c.line]
            off = c.start - doc.line_starts[c.line]
            before = re.sub(r'x{5,}', '', line[:off])
            self.need(re.match(r'^\s*\|\s*[^\s|]+\s*$', before), doc, c,
                      'right after the number of the objective, in its first cell')

    def c_content(self, doc, c):
        self.need(doc.in_cell(c.line), doc, c, 'only inside a table cell')
        self.register_uuid(doc, c, c.args.get('uuid'))

    # ---- inline
    def c_index(self, doc, c):
        if c.alone:
            self.r.warn(doc.path, c.line + 1, '`index()` belongs inline, directly before its word (`Der {{ index(\'Motor\') '
                                              '}}Motor …`), not on a line of its own (COMMANDS.md: inline only)')
        for k in ('entry', 'sub'):
            v = c.args.get(k)
            if v is not None or k == 'entry':
                self.need(isinstance(v, str) and v.strip() and '"' not in v and ':' not in v, doc, c,
                          f'`{k}` non-empty, without `"` or `:`')

    def c_link(self, doc, c):
        self.url_arg(doc, c, 'url')
        self.text_arg(doc, c, 'text', required=False)

    def c_color(self, doc, c):
        self.text_arg(doc, c, 'text')
        self.color_arg(doc, c, 'color')

    def c_footnote(self, doc, c):
        self.text_arg(doc, c, 'text')

    def c_anchor(self, doc, c):
        self.need(HEADING_RE.match(doc.lines[c.line]), doc, c, 'only in a heading, at its end '
                  '(figures: `image(anchor=…)`, tables: `table(anchor=…)`)')
        self.register_anchor(doc, c, c.args.get('name'))

    def c_ref(self, doc, c):
        self.choice_arg(doc, c, 'show', ('number', 'title', 'page'))
        if isinstance(c.args.get('name'), str):
            self.refs.append((c.args['name'], doc.path, c.line + 1))

    def c_cite(self, doc, c):
        if isinstance(c.args.get('key'), str):
            self.cites.append((c.args['key'], doc.path, c.line + 1))

    def c_formula(self, doc, c):
        self.text_arg(doc, c, 'tex')
        tex = c.args.get('tex')
        if isinstance(tex, str):
            depth = 0
            for m in re.finditer(r'\\.|[{}]', tex):
                if m.group() == '{':
                    depth += 1
                elif m.group() == '}':
                    depth -= 1
                    if depth < 0:
                        break
            self.need(depth == 0, doc, c, f'unbalanced braces in the LaTeX {tex!r}')
            self.need(re.findall(r'\\begin\{(\w+\*?)\}', tex) == re.findall(r'\\end\{(\w+\*?)\}', tex)[::-1]
                      or len(re.findall(r'\\begin\{', tex)) == len(re.findall(r'\\end\{', tex)), doc, c,
                      '`\\begin{…}` without its `\\end{…}` in the LaTeX')
        self.choice_arg(doc, c, 'align', ALIGNS)
        if c.args.get('align') is not None and not c.alone:
            self.r.warn(doc.path, c.line + 1, '`formula(align=…)` only aligns a formula on a line of its own')

    def c_uuid(self, doc, c):
        self.register_uuid(doc, c, c.args.get('uuid'))
        line = doc.flat_lines[c.line]
        off = c.start - doc.line_starts[c.line]
        before = re.sub(r'^\s*(#{1,6}\s+|>\s*|([-*+]|\d+[.)])\s+)*', '', line[:off])
        after = line[c.end - doc.line_starts[c.line]:] if c.end_line == c.line else ''
        after = re.sub(r'x{5,}', '', after)   # other calls after it (e.g. anchor()) are fine
        if c.alone or not before.strip():
            self.r.error(doc.path, c.line + 1, '`uuid()` goes after the text it identifies (end of a heading or '
                                               'of a paragraph), not alone or before it')
        elif doc.in_cell(c.line):
            self.r.error(doc.path, c.line + 1, '`uuid()` in a table cell is lost; use `{% call content(uuid=…) %}`')
        elif after.strip():
            heading = HEADING_RE.match(doc.lines[c.line])
            (self.r.error if heading else self.r.warn)(doc.path, c.line + 1, '`uuid()` stands at the end of its '
                                                       + ('heading' if heading else 'paragraph'))
        if sum(1 for o in doc.calls if o.name == 'uuid' and o.line == c.line) > 1 and \
                min(o.start for o in doc.calls if o.name == 'uuid' and o.line == c.line) != c.start:
            self.r.error(doc.path, c.line + 1, 'a second `uuid()` for the same heading or paragraph')

    # ---- after all files
    def resolve(self, cross_file: bool):
        report = self.r.error if cross_file else self.r.warn
        for name, p, ln in self.refs:
            if name not in self.anchors:
                report(p, ln, f'`ref({name!r})`: no heading, figure or table has this anchor')
        if self.cites:
            if cross_file and self.bibliography is None:
                p, ln = self.cites[0][1:]
                self.r.error(p, ln, '`cite()` without `bibliography()` in the manifest')
            keys = getattr(self, 'source_keys', None)
            if keys is not None:
                for key, p, ln in self.cites:
                    if key not in keys:
                        self.r.error(p, ln, f'`cite({key!r})`: no entry with this key in {rel(self.bibliography)}')


# --------------------------------------------------------------------------- main

def find_manifest(path: Path) -> Path | None:
    p = path.resolve()
    if p.is_file() and p.name == '_main_.md':
        return p
    folder = p if p.is_dir() else p.parent
    for d in (folder, *list(folder.parents)[:2]):
        if (d / '_main_.md').is_file():
            return d / '_main_.md'
    return None


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__)
        return 0 if argv else 2
    report = Report()
    manifests, singles = [], []
    for a in argv:
        p = Path(a)
        if not p.exists():
            print(f'{a}: not found', file=sys.stderr)
            return 2
        m = find_manifest(p)
        if m is not None:
            if m not in manifests:
                manifests.append(m)
        elif p.is_file():
            singles.append(p)
        else:
            singles.extend(sorted(p.glob('*.md')))
    for m in manifests:
        Checker(report).check_document(m)
    if singles:
        ch = Checker(report)
        for p in singles:
            d = ch.load(p)
            if d is not None:
                ch.check_content(d, 'content')
        ch.resolve(cross_file=False)

    order = {'error': 0, 'warning': 1, 'info': 2}
    seen = set()
    for f, ln, level, msg in sorted(report.items, key=lambda t: (t[0], t[1], order[t[2]])):
        if (f, ln, level, msg) not in seen:
            seen.add((f, ln, level, msg))
            print(f'{f}:{ln}: {level}: {msg}')
    counts = {lv: sum(1 for *_, l, _m in seen if l == lv) for lv in order}
    checked = ', '.join(str(rel(m.parent)) for m in manifests) or ', '.join(str(rel(p)) for p in singles)
    print(f'-- {checked}: {counts["error"]} error(s), {counts["warning"]} warning(s), {counts["info"]} info')
    return 1 if counts['error'] else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
