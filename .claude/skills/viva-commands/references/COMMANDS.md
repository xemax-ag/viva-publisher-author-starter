# The commands of the render step

A command is a Jinja function call `{{ name(…) }}` in a document's manifest `content/<document>/_main_.md` or in one
of its chapter files (`content/` and `rendered/` are those of the folder the program runs in, `core/paths.py`; a script
points them elsewhere with `set_folders`). The render step (`python -m viva_publisher_converter.md_render --document
<document>`, in Python `md_render(MdRenderArgs(…))`) checks every call (`md_render/commands/<name>.py`) and turns it
into a marker `⟦name {JSON}⟧` in `rendered/<document>/`; the conversion (`python -m viva_publisher_converter.md_to_docx
--source rendered/<document>/_main_.md`, in Python `md_to_docx.build.build`; each command
`viva_publisher_converter/md_to_docx/commands/<name>.py`) writes it into the Word document. The validation scripts
(`validations/<name>/<name>_v.py`) run the steps one after another: import, render, convert, PDF. A call that fails
its check is a problem with its file and line; then nothing is converted.

## Writing a call

- **Manifest:** one call per line, in document order; nothing else but `{# … #}` comments.
- **Comments:** `{# … #}` (Jinja's) and the Markdown comment `[//]: # (…)` on a line of its own (also with `"…"`,
  `'…'` or nothing after the `#`); the render step removes both, a Markdown comment before Jinja reads the file (a call
  in it is not run) and as an empty line (between the lines of a paragraph it ends the paragraph). In a code block
  (```) and in `{% raw %}` … `{% endraw %}` it stays text.
- **Chapter file:** a call stands on a line of its own; `index()`, `link()` and `formula()` also inside the text,
  `image()` in the cells of a pipe table or an [HTML table](#table).
- **Escapes:** in text a backslash before ASCII punctuation is that character, never markup (as in CommonMark):
  `3\. Schritt` is no list, `\# kein Titel` no heading, `2\*3\*4` no emphasis — the Word import (`docx_to_md`)
  writes such text so. Not in code (a code span, a code block) and not in the LaTeX of `formula()`.
- **Arguments:** by name, e.g. `image('bild.png', width='8cm')`; the ones listed as *positional* also by position,
  in that order. An unknown or a missing argument is a problem. Strings in `'…'` or `"…"`.
- **Files:** relative to the calling file (in the manifest: the manifest folder); a leading `/` is relative to the
  manifest folder. The file arguments named below must exist.
- **Once:** `title()` and `logo()` at most once per document.
- **Enclosing:** `note()`, `frame()`, `table()` and `learning_objectives()` also as `{% call note() %}` …
  `{% endcall %}`, `list()` only so, each on a line of its own: the blocks between them are its content.
  `content()` only so, inside a table cell. Inside, only what the command names below (e.g. `formula()` lines in a
  note, `image()` and `content()` in a table's cells); another block command in `{% call %}` is a problem.
- **uuid:** every command also takes `uuid=None`, by name only, e.g.
  `{{ page_break(uuid='0f8fad5b-d9cb-469f-a165-70867728950e') }}`: an identifier of the call, a UUID of version 4
  (another version or no UUID is a problem). Each uuid at most once per document, over all its files (upper and
  lower case are the same uuid): a second use is a problem at its place, naming the first (e.g. code copied from
  another chapter: give the copy new uuids). It goes into the marker, written in lower case; the tables below leave
  it out. A heading or a paragraph gets its identifier from [`uuid()`](#uuid). In the Word document what the call
  writes is in a content control (`w:sdt`) whose tag (`w:tag`) is the identifier: a block's paragraphs or table, an
  inline call's runs (a picture or formula alone in its paragraph: the paragraph). A display formula's control is an
  equation control (Word shows an equation in another one inline, and removes an equation control when the formula is
  edited); a block holding a display formula, e.g. a table with a formula alone in a cell, gets none.

## The Word imports

Two importers write a document's files from a Word document into `content/<document>/`, every call with a `uuid=`,
and list what they could not write as it is in `CONVERT.md` and `CONVERT.json`:

- **The template import** (`viva_publisher_converter/docx_to_md`, `validations/docx_to_md/docx_to_md_v.py`): a Word
  document of the template `textbook_2026_V02.dotx`, e.g. the author guide or a document the conversion wrote. It
  reads back every command the conversion writes into the Word document, with the uuids of its content controls;
  where it reads each: `docx_to_md/convert/structure/commands.py` (`tests/docx_to_md/test_commands.py` converts each
  command and imports it again). Not read back, as the Word document holds nothing of it: the uuid of a manifest call
  and of `ref()`, `anchor()`, `link_lo()` and the management summary's title (the import draws new ones); `alt_text`,
  `border` and `crop` of `image()` (`height` and `scale` come back as its `width`; a turned picture comes back
  turned, without `rotate`); `numbered=False` of `table()`; the
  widths of `learning_objectives()`; `unnumbered` of `list_of_illustrations()` and `list_of_tables()`; another
  `title` of `bibliography()`; `size`, `color` and `alignment` of `qr_code()`.
- **The InDesign import** (`viva_publisher_converter/docx_to_md_from_indesign`,
  `validations/docx_to_md_from_indesign/docx_to_md_from_indesign_v.py`): a Word document of an InDesign book
  (InDesign → PDF → Word), e.g. Antriebstechnik. It writes what it recognises — the labels and notes of a Hinweis, a
  Selbstkontrolle, the learning objectives, tables and groups of pictures, as the commands below name it; what it
  cannot place is an open item in `CONVERT.md`.

## Overview

| Command | Where | Arguments (positional first) | What it writes |
| --- | --- | --- | --- |
| [`title`](#title) | manifest | `text` | the document title |
| [`logo`](#logo) | manifest | `name` | the logos of the colour bands and the page headers |
| [`watermark`](#watermark) | manifest | `text`, `color='#C0C0C0'` | a text watermark on every page, e.g. «ENTWURF» |
| [`cover`](#cover) | manifest | `src='cover.md'`, `image=None` | the title page |
| [`imprint`](#imprint) | manifest | `src='impressum.md'`, `top=None` | the imprint on a page of its own |
| [`management_summary`](#management_summary) | manifest | `src='management_summary.md'` | the Management Summary, not numbered |
| [`table_of_contents`](#table_of_contents) | manifest | – | the table of contents |
| [`chapter`](#chapter) | manifest | `src`, `image=None` | a chapter |
| [`list_of_illustrations`](#list_of_illustrations) | manifest | `unnumbered=True` | the Abbildungsverzeichnis |
| [`list_of_tables`](#list_of_tables) | manifest | `unnumbered=True` | the Tabellenverzeichnis |
| [`glossar`](#glossar) | manifest | `src='glossar.md'` | the Glossar |
| [`bibliography`](#bibliography) | manifest | `src='quellen.md'`, `title='Quellenverzeichnis'` | the list of the sources cited with `cite()` |
| [`keyword_index`](#keyword_index) | manifest | – | the Stichwortverzeichnis |
| [`image`](#image) | manifest, chapter | `src`, `width`, `height`, `scale`, `align`, `border`, `crop`, `wrap`, `title`, `numbered`, `anchor`, `alt_text`, `rotate` | a picture |
| [`page_break`](#page_break) | manifest, chapter | – | a page break |
| [`index`](#index) | chapter, inline | `entry`, `sub=None` | an entry of the Stichwortverzeichnis |
| [`link`](#link) | chapter, inline | `url`, `text=None` | a hyperlink to a URL |
| [`color`](#color) | chapter, inline | `text`, `color='#E30613'` | its text in a colour, e.g. red |
| [`footnote`](#footnote) | chapter, inline | `text` | a numbered footnote: its number here, its text at the bottom of the page |
| [`anchor`](#anchor) | chapter, in a heading | `name` | the name of the heading, a target of `ref()` (figures, tables: `anchor=` of `image()`, `table()`) |
| [`ref`](#ref) | chapter, inline | `name`, `show='number'` | a reference to a heading, figure or table: its number, title or page, a link |
| [`cite`](#cite) | chapter, inline | `key`, `page=None` | a citation of a source: «[1]», «[1, S. 23]», a link to its entry of `bibliography()` |
| [`formula`](#formula) | chapter, inline or own line | `tex`, `align='left'` | a Word equation |
| [`table`](#table) | chapter | `*widths`, `type='default'`, `anchor=None`, `numbered=True` | the column widths of the next table (`type='pictures'`: pictures side by side; `type='layout'`: text and pictures in columns) |
| [`learning_objectives`](#learning_objectives) | chapter | `*widths='2.3cm', '13.7cm'` | the next table as the learning objectives |
| [`link_lo`](#link_lo) | chapter, after the number of a learning objective | `*keys` | its keys in the database futuremem (link learning objective): a Word comment `link_lo: …` on the number |
| [`qr_code`](#qr_code) | chapter | `text=None`, `size='2.5cm'`, `color='#007DB3'`, `alignment='left'` | a QR code (without text a warning sign) |
| [`grid`](#grid) | chapter | `spacing='5mm'`, `n_width=32`, `n_height=47`, `thickness='0.15mm'`, `color='#A8C9CF'`, `alignment='left'` | squared paper: a grid of squares |
| [`label`](#label) | chapter | `text`, `icon=None`, `link=None`, `offset_x=None`, `offset_y=None` | a label with an icon, e.g. «Lernziel», «Selbstkontrolle», «Hinweis» |
| [`list`](#list) | chapter, `{% call %}` only | – | the list inside, as it is (its identifier: `uuid`) |
| [`note`](#note) | chapter | – | the next paragraph or list (or with `{% call %}` the blocks inside) in the style Note, e.g. the text of a «Hinweis» |
| [`frame`](#frame) | chapter, `{% call %}` too | `color='#03A4C0'`, `background=None`, `thickness='1.5pt'` | the next paragraph or list (or with `{% call %}` the blocks inside) in a box with a coloured frame |
| [`content`](#content) | chapter, in a table cell, `{% call %}` only | `uuid` | what it encloses in a table cell, identified by its uuid (several per cell) |
| [`uuid`](#uuid) | chapter, inline | `uuid` | the identifier of a heading or paragraph (the tag of its content control) |

## Manifest

### title

`{{ title('Antriebstechnik') }}` — the document title (header field TITLE), also the title of the cover if the cover
does not set one. `text` must not be empty. At most once.

### logo

`{{ logo('nextecmedia') }}` — the logo of the document, from `reference/template/logos/misc/`:

- `<name>_logo_chapter.svg` (required): the logo of the colour bands (cover, chapter openers);
- `<name>_logo_header.svg` (optional): replaces the logo of the page headers.

`name` is a file prefix: letters, digits, `-` or `_`. Without `logo()` the template's logos stay
(`reference/template/logos/chapter.svg` and `header.svg`). It applies to the
whole document wherever it stands (it runs before the other entries). At most once. A build can set both logos as
settings, any SVG file (`md_to_docx.build.build(chapter_logo=…, header_logo=…)`; the validation scripts' `CHAPTER_LOGO`
and `HEADER_LOGO`); they override `logo()`.

### watermark

`{{ watermark('ENTWURF') }}`, `{{ watermark('VERTRAULICH', color='#E30613') }}` — Word's text watermark on every page of
the document, the cover too: `text` diagonally across the text area (rotated by 315°, as wide as the text column, in
Arial: the PDF step's Roboto would leave holes in the letters), behind the text, filled in `color` (`#RRGGBB`, default
light grey `#C0C0C0`) at 50 % opacity. A picture on the page (the cover's or a chapter opener's picture) covers it. The
converter writes it into every page header (the cover, which shows no header, gets one that holds only the watermark);
Word shows it as its watermark (Design › Watermark changes or removes it), the PDF too. `text` is one line and must not
be empty. It applies to the whole document wherever it stands. At most once. The template import writes Word's text
watermark back as `watermark()` (a picture watermark or a second text is a note in `CONVERT.md`).

### cover

`{{ cover() }}`, `{{ cover('titelseite.md', image='titelbild.png') }}` — the title page, like page 1 of the
Autorenhandbuch. `src` (rendered too) holds:

```
# techLEARN 2.0                     colour band, 30 pt bold (also the document title, if not set)
## Vorstellung Vision xemax ag      colour band, 13 pt bold
### Version 2026                    colour band, 10 pt bold

#### Impressum                      subheading in the lower part of the page
Titel: techLEARN 2.0                rows directly below it: "Titel<Tab>techLEARN 2.0"
Version: 2026, Stand 29. September 2026

Dieses Dokument wurde …             Base Text
```

The colour band starts at the top edge with the logo at the top right; page 1 has no header or footer, the next entry
starts on page 2. `image`: a picture filling page 1 below the band, full width down to the bottom edge; then `src`
holds only the band lines (checked) and the imprint goes onto a page of its own with `imprint()`. Both files must
exist.

### imprint

`{{ imprint() }}`, `{{ imprint(top='120mm') }}` — the imprint on a page of its own, e.g. page 2 after
`cover(image=…)`. `src` (default `impressum.md`, rendered too) is written like the imprint part of `cover.md`
(`#### Impressum`, `Titel: …` rows, base text), in the lower part of the page, without page title and chapter marks;
the header shows the book title and «Impressum». `top` (mm, cm or pt, e.g. `'120mm'`, `'12cm'`): the distance from the
top edge of the page to the block's first line, from `'35.2mm'` (the top margin) to `'273.3mm'` (the bottom margin); a
block too long for the rest of the page continues on the next one. The next entry starts on a new page.

### management_summary

`{{ management_summary() }}` — the Management Summary on a new page, usually after the cover, before the table of
contents. `src` (default `management_summary.md`, rendered too) is Markdown like a chapter, but nothing is numbered:
the first `#` heading is the page title (default «Management Summary»), all other headings are subheadings. The
chapter counter does not advance.

### table_of_contents

`{{ table_of_contents() }}` — «Inhaltsverzeichnis» on a new page with a table of contents field (levels 1–3). The page
numbers start at 1 on the first page after it; the pages before have none.

### chapter

`{{ chapter('kapitel_1.md') }}`, `{{ chapter('kapitel_1.md', image='opener.png') }}` — a chapter from a Markdown file
(rendered too, so its calls are checked as well). `image`: a picture filling the chapter opener's page below the colour
band, full width down to the bottom edge; the chapter text then starts on the next page. Both files must exist.

### list_of_illustrations

`{{ list_of_illustrations() }}` — the Abbildungsverzeichnis on a new page: the caption of each picture with a
`title`, in the order of the document — numbered «Abbildung 1.2: Titel», with `numbered=False` its title alone — and
its page at the right margin, the whole entry a link to the caption (clickable in Word and in the PDF), in the look of
the table of contents. `unnumbered=False`: only the numbered captions. A picture without `title` has no caption and is
not listed. The list is there if the manifest calls it: without the call (or with the line deleted or commented out,
`{# … #}`) there is none. The converter writes the entries when the whole document is written (so the list may stand
before the chapters); the page numbers are page references that Word and the PDF set. An entry keeps the look of its
title (bold, italic, a formula) but neither its links nor its footnotes or `index()` entries.

### list_of_tables

`{{ list_of_tables() }}` — the Tabellenverzeichnis on a new page, as [`list_of_illustrations()`](#list_of_illustrations)
from the table captions (the `Tabelle: Titel` line before a table): numbered «Tabelle 1.2: Titel», with
`table(numbered=False)` its title alone; `unnumbered=False`: only the numbered ones.

### glossar

`{{ glossar() }}` — the Glossar on a new page, from `src` (default `glossar.md`, rendered too) with one
`Begriff: Definition` per line; headings and `<!-- comments -->` in the file are ignored. The entries are sorted
alphabetically (umlauts like their base letter), the term in bold. In the chapters' body text, the first occurrence of
a term per chapter becomes a link to its entry (as a whole word, also with a German ending: Lernziel → Lernziele).

### bibliography

`{{ bibliography('quellen.md') }}` — the list of the sources cited with [`cite()`](#cite) on a new page, titled
`title` (default «Quellenverzeichnis»), from `src` (default `quellen.md`, rendered too) with one `key: entry` per line:

```
erdmann2023: Erdmann D.; Brönnimann S.: *Humboldts Wetterwerkstatt.* Bern: Haupt, 2023.
meier1999: Meier P.: *Die Einsamkeit des Staatsgefangenen Micheli du Crest.* Zürich: Pendo, 1999.
```

The key: a letter, then letters, digits, `-` or `_` (at most 40); the entry is Markdown (italic, links). Headings and
`<!-- comments -->` in the file are ignored. Only the cited entries are listed, numbered in the order of their first
citation in the document: «[1]» and the entry, with a hanging indent. The converter writes the list when the whole
document is written, so `bibliography()` may also stand before the chapters. Once per document; a line without
`key: entry` or a key twice is a problem.

### keyword_index

`{{ keyword_index() }}` — the Stichwortverzeichnis (two columns) on a new page, from the `index()` entries of the
chapters.

## Manifest and chapter

### image

`{{ image('bild.png', width='8cm', border=True, title='Aufbau') }}` — a picture: PNG, JPG, … or SVG (embedded as
vector graphics with a PNG fallback). In a chapter it stands on a line of its own and its file is relative to the
chapter, like `![…](…)`; in the manifest relative to the manifest folder. The file must exist (a planned picture is
the placeholder `((bild.png))`).

| Option | Example | Meaning |
| --- | --- | --- |
| `width` | `'8cm'` | cm, mm, pt or % of the text column; alone, the height follows from the aspect ratio |
| `height` | `'5cm'` | cm, mm or pt; with `width` too, the picture fits into the box (never distorted) |
| `scale` | `'90%'` | of the native size (pixels / dpi); not with `width` or `height` |
| `align` | `'right'` | `'left'`, `'center'` (default; `'left'` with `wrap`) or `'right'` |
| `border` | `True` | a grey ½ pt line |
| `crop` | `'0 5%'` | top right bottom left in % of the picture, 1 to 4 values like CSS; Word crops, the file stays |
| `wrap` | `True` | floating: picture and caption in a frame on the `align` side, the text flows around; not with `'center'` |
| `title` | `'Aufbau'` | the numbered caption below the picture (listed by `list_of_illustrations()`) |
| `numbered` | `False` | the caption only its `title`, without «Abbildung n:», in the same style and place (on the page of its picture, with `wrap` in its frame); listed by `list_of_illustrations()` with its title alone (not with `unnumbered=False`); only with `title` |
| `anchor` | `'aufbau'` | its name, a target of [`ref()`](#ref): «Abbildung 1.2», its title, its page; only with `title` |
| `rotate` | `-90` | the picture turned by 90, 180 or 270 degrees clockwise (negative: counter-clockwise; anything else is a problem) before the other options: `width`, `height`, `scale`, `crop` and `align` apply to the turned picture (`width='9.9cm', rotate=-90`: a landscape chart 9.9 cm wide and as tall as it is long); the converter turns the picture itself, not the Word shape, the file stays |
| `alt_text` | `'Schaltplan des Motors'` | the picture's alternative text in Word (Alt Text: screen readers, the PDF); `None` (the default; both imports write it so, to be filled in): none; a Markdown picture `![…](…)` takes its `[…]` |

The picture is never wider than the text column. In a cell of a pipe table or an HTML table the call puts the picture
into its cell
(with text around it if wanted): `width`, `height`, `scale`, `crop`, `border` and `align` work there, `wrap` and
`title` are problems (so `numbered=False` too) — but in a `table(type='layout')`, where `title` and `numbered` give the caption below the picture, and the picture is at most as wide as its column.

### page_break

`{{ page_break() }}` — the next entry starts on a new page; in a chapter on a line of its own, e.g. to keep a section
with its figure on one page. Use it sparingly: the styles do the layout.

## Chapter

### index

`Der {{ index('Motor') }}Motor dreht.`, `{{ index('Motor', 'Stellmotor') }}` — an entry (`entry`) or a subentry
(`sub`) of the Stichwortverzeichnis at this place in the text. Inline only, not on a line of its own; neither may be
empty or contain `"` or `:`.

### link

`Siehe {{ link('https://www.swissmem.ch', 'Swissmem') }}.`, `{{ link('mailto:info@example.org') }}` — a hyperlink to
`url` at this place in the text: `text` (without it the URL) in the style Hyperlink, clickable in Word and in the PDF.
Inside a paragraph, a list item, a table cell or a note; a line of only a link is a paragraph. `url` is
`https://…`, `http://…` or `mailto:…` without spaces (as `label(link=…)`); `text` must not be empty. The Markdown
link `[Swissmem](https://www.swissmem.ch)` writes the same.

### color

`Spannung: {{ color('Lebensgefahr!') }}`, `{{ color('**Achtung**', '#00B050') }}` — `text` in a colour at this place
in the text: in a paragraph, a list item, a table cell (pipe or HTML, also in its list items), a `note()` or a
`frame()`; a line of only `color()` is a paragraph. `color` is `#RRGGBB` (default `#E30613`, signal red); `text` must
not be empty. It combines with bold and italic both ways: `text` is Markdown like the text around it
(`{{ color('**fett** und *kursiv*') }}`: all red, «fett» bold, «kursiv» italic), and a `color()` inside `**…**` or
`*…*` is bold or italic too (`**Warnung: {{ color('Starkstrom') }}**`). A text with `'` goes into `"…"`.

### footnote

`Die Norm IEC 60034-7{{ footnote('IEC 60034-7:2023, Drehende elektrische Maschinen – Bauformen.') }} beschreibt …` — a
numbered footnote at this place in the text: its number (superscript, the style «footnote reference») right after the
word before it, its text at the bottom of the page after its number, in the style «footnote text» (8 pt). The numbers
count anew in each chapter (1, 2, 3 …); the converter sets them in the order of the calls (LibreOffice restarts no
footnote numbers per chapter of a Word document), so a new build numbers them anew, but a footnote added later in
Word itself does not renumber them. In a
paragraph, a list item, a table cell, a `note()` or a `frame()`. `text` is Markdown (bold, italic, links like
`[Swissmem](https://www.swissmem.ch)`) and must not be empty; a text with `'` goes into `"…"`.

### anchor

`## Temperaturskalen {{ anchor('temperaturskalen') }}` — the name of the heading it stands in (any level), a target
of [`ref()`](#ref); at the end of the heading like `uuid()`, which may follow it. A figure is named with `anchor=` of
`image()` (with a `title`), a table with `anchor=` of `table()` (with its `Tabelle: …` line). `name`: a letter, then
letters, digits, `-` or `_` (at most 40), once in the document (over all its files). Elsewhere than in a heading, the
same name twice, a figure without `title` or a table without its `Tabelle: …` line is a problem.

### ref

`Siehe Abschnitt {{ ref('temperaturskalen') }}`, `{{ ref('aufbau') }} auf Seite {{ ref('aufbau', 'page') }}` — a
reference to the target `name` at this place in the text, a link to it (clickable in Word and in the PDF). `show`:
`'number'` (default) its number — a heading «1», «1.2», «1.2.3», a figure «Abbildung 1.2», a table «Tabelle 1.2»; a
heading of `####` or a picture with `numbered=False` has none: its title —, `'title'` its title, `'page'` its page (a
page reference, set when the pages are). The converter fills the number and the title when the whole document is
written, so the target may also come later. A name no target has is a problem (the render step checks it after all
files).

### cite

`Humboldt mass die Temperatur täglich {{ cite('erdmann2023', '23') }}.` — a citation of the entry `key` of the
sources file of [`bibliography()`](#bibliography) at this place in the text: «[1]», with `page` «[1, S. 23]» (`page`:
the page or pages as text, e.g. `'23'` or `'23–25'`), a link to its entry (clickable in Word and in the PDF). The
numbers count in the order of the first citation of each entry; the converter sets them when the whole document is
written. Two sources: two calls, `{{ cite('erdmann2023', '23') }} {{ cite('meier1999') }}`. A key without entry in the
sources file, or a `cite()` without `bibliography()` in the manifest, is a problem (the render step checks it after
all files).

### formula

`Die Spannung {{ formula('U') }} steigt.` — a LaTeX formula as a Word equation: inside the text an inline equation, on
a line of its own a display equation (style Formula; inside `> [!AUFGABE]`, a Hinweis or a Lösung box, `note()` and
`frame()` in their style), aligned by `align`: `'left'` at the indent of its style, `'center'` or `'right'`,
`{{ formula('P = F \cdot v', align='center') }}` (the Word import keeps the alignment of a Word math paragraph;
an inline equation has none).
The LaTeX is written as is, `{{ formula('\frac{U}{R}') }}`; a formula with `'` goes into `"…"`. The render step
converts it once to check it: a LaTeX error is a problem.

### table

`{{ table('2.3cm', '3.2cm', '*') }}` — the column widths of the next table, on a line of its own directly
before a pipe table, an HTML table or the table's `Tabelle: …` line. Which kind of table follows is seen by its first
line: `|` a pipe table, `<table` an HTML table. The separator row `| --- |` of the pipe table may be left out: then it
has no header row (every row a normal one, as in an HTML table without `<thead>`), with it its first row is the header
row. One width per column: cm, mm or pt (decimal comma allowed), % of the 16 cm text column, or `*` (the `*` columns
share the rest equally); without widths, `table()`, the columns share the text column equally (as without `table()`;
the InDesign import writes `{% call table() %}` so around every table without column widths of its own, the template
import gives each table the widths of its grid). Problems: an
invalid width, fixed widths over 16 cm, no table after it, a wrong number of widths. All widths fixed and narrower
than 16 cm: a narrower table. `anchor='werte'`: the table's name, a target of [`ref()`](#ref)
(«Tabelle 1.2», its title, its page); it needs the `Tabelle: …` line. `numbered=False`: the caption without
«Tabelle n:», only its title (in the same style and place; listed by [`list_of_tables()`](#list_of_tables) without
number, `ref()` gives its title); it needs the `Tabelle: …` line.

The same around its table (both imports write it so): `{% call table(…) %}` and `{% endcall %}` on lines of
their own, between them the `Tabelle: …` line (if any) and the table, nothing else:

```markdown
{% call table('5.4cm', '7.1cm', '3.5cm') %}
Tabelle: Motorarten
| Motor | Bild | Einsatz |
| --- | --- | --- |
| Asynchronmotor | {{ image('images/0010.png', width='3cm') }} | Förderband |
{% endcall %}
```

An HTML table runs from a line starting with `<table` to the line with `</table>` (empty lines inside are allowed) and
is a table like a pipe table, with or without `table()`, `learning_objectives()` or a
`Tabelle: …` line before it. Its tags: `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`, in the cells
`<strong>` or `<b>`, `<em>` or `<i>`, `<a href="…">`, `<br>` and `<p>` (a line break); white space as in HTML, entities
like `&amp;`, calls like `image()` and Markdown in the cells as in a pipe table:

```markdown
{{ table('13.4cm', '2.6cm') }}
<table>
  <tbody>
    <tr>
      <td><strong>Arbeitsplatz aufräumen</strong><br>→ Abfall korrekt entsorgen.</td>
      <td>{{ image('images/0030.jpg', width='2.4cm') }}</td>
    </tr>
  </tbody>
</table>
```

Its header rows — bold and repeated on every page — are the rows of `<thead>`; without `<thead>` the table has no
header row, its first row looks like the others, also with `<th>` cells (a pipe table's first row is one, with its
separator row `| --- |`). Its widest row gives the number of columns; a row also counts the columns its `colspan`
cells and the `rowspan` cells above it take, so the widths of `table()` are those of the grid.

`colspan="m"` on a `<td>` or `<th>`: the cell and the m − 1 cells beside it are one cell (in Word merged
horizontally); the row's next cell follows after them. `rowspan="n"`: the cell and the n − 1 cells below it are one
cell (in Word merged vertically, its text at the top); the rows below leave its columns out, their cells go to the
next free column. Both together: a block of n rows and m columns. As in HTML a rowspan stays within the header rows
(`<thead>`) or within the rows below them, e.g. a text beside a table of values (four widths: the two columns of the
values, an empty gap column, the text):

```markdown
{{ table('3.6cm', '4.4cm', '0.6cm', '*') }}
<table>
  <tr>
    <td><strong>Reglertyp</strong></td>
    <td><strong>Werte</strong></td>
    <td rowspan="3"></td>
    <td rowspan="3">Der Vorteil dieser praktischen Einstellkriterien besteht darin, …</td>
  </tr>
  <tr><td>P-Regler</td><td>{{ formula('K_p = 0{,}5 \cdot K_{pKR}') }}</td></tr>
  <tr><td>PD-Regler</td><td>{{ formula('K_p = 0{,}8 \cdot K_{pKR}') }}<br>{{ formula('T_D = 0{,}12 \cdot T_{KR}') }}</td></tr>
</table>
```

A head of two rows with groups of columns («Reglertyp» two columns wide and two rows high):

```markdown
{{ table('1cm', '1cm', '3.5cm', '3.5cm', '3.5cm', '3.5cm') }}
<table>
  <tr>
    <td rowspan="2" colspan="2"><strong>Reglertyp</strong></td>
    <td colspan="2"><strong>Aperiodischer Regelvorgang</strong></td>
    <td colspan="2"><strong>Überschwingen von ca. 20%</strong></td>
  </tr>
  <tr><td>Führung</td><td>Störung</td><td>Führung</td><td>Störung</td></tr>
  <tr>
    <td rowspan="2">PI</td><td>{{ formula('K_P') }}</td>
    <td>{{ formula('K_p = 0{,}35 \cdot \frac{T_g}{T_u \cdot K_s}') }}</td> …
  </tr>
  …
</table>
```

Other tags, a `rowspan` or `colspan` that is no whole number from 1, a `rowspan` that goes beyond the header rows or
the last row, a `colspan` that runs into a column of a `rowspan` cell above (the converter shortens them), a table
inside a cell, text outside of a cell and a missing `</table>` are problems.

`type`: the kind of table, `'default'` (the default: a table as above) or `'pictures'`: the table as pictures side by
side, e.g. `{% call table('8.2cm', '7.8cm', type='pictures') %}` (the
InDesign import writes it so for a group of pictures, an HTML table of `<td>` cells; the template import for a table in
the style Picture Table whose cells hold only pictures and captions), without a `Tabelle: …` line (a picture
table has no caption number). The table gets the style Picture Table (no borders, no cell margins, no header row). In
its cells a line (separated by `<br>`) of only `image()` calls is a paragraph in the style Image, consecutive text
lines one paragraph in the style Figure Caption; a picture is at most its column's width; the table stays on one page.

`type='layout'`: text and pictures side by side in columns, e.g. a text beside a picture with its caption, without a
`Tabelle: …` line. The table has no lines and no header row (the style Picture Table), 0.5 cm between its columns and
no margin at its outer edges, so its text lines up with the text column. In its cells the text is the body text
(Base Text): `<br>` is a line break inside a paragraph (no space, as in a normal table), an empty line (`<br><br>`)
or a new `<p>` starts a new paragraph (in a normal table both are line breaks too); a line of only `image()` calls is
a paragraph in the style Image, and each of its pictures with a `title` gets its caption below it: numbered, or with `numbered=False` only the
title (`wrap` stays a problem); a picture is at most its column's width. Its rows may break across pages. The template
import writes it for a table in the style Picture Table with other text in its cells.

```markdown
{% call table('8.2cm', '7.8cm', type='layout') %}
<table>
  <tr>
    <td><p>Die Gleichstrommaschine konnte sich …</p><p>Durch die Frequenzumrichter …</p></td>
    <td>{{ image('images/1020.jpg', width='7.8cm', title='BLDC-Motor mit integrierter Ansteuerschaltung', numbered=False) }}</td>
  </tr>
</table>
{% endcall %}
```

Lists in a cell of a normal table or a `table(type='layout')`: a cell line (after a `<br>`, or a `<p>`) that starts
with `- ` or `1. ` (as a Markdown list item) is a list item without its mark, in the style Bullet List or Numbered
List; the numbers are counted anew in each cell, and after other lines a numbered list starts anew (an empty
line between items does not end it). A numbered list starts at the number of its first item, as in Markdown: a cell
`2. Grössenordnung abschätzen` shows «2.», so the cells of a column can be numbered 1., 2., 3. (as a list in the text
or in `note()` and `frame()`: `3. …` counts 3, 4, …). In a normal table the other lines before, between and after the items each stay
one paragraph with line breaks; a cell without list lines is one paragraph as before. Not in a picture table (its text
lines are captions) or the learning objectives:

```markdown
<td>Die vier klassischen Gleichstrommotoren:<br>1. Reihenschlussmotor<br>1. Fremderregter Motor<br>1. Nebenschlussmotor</td>
```

#### Pipe tables of each kind

Each kind of table can also be written without HTML, as a pipe table: one line per row, the cells between `|`; in a
cell `<br>` is a line break (and an empty line, `<br><br>`, a new paragraph in a layout table), a line starting with
`- ` or `1. ` a list item, and `image()`, `formula()`, `content()` and Markdown work as in an HTML cell. Not possible in
a pipe table: cells over several rows or columns (`rowspan`, `colspan`), a cell over several lines and a `|` in a
cell's text — these need an HTML table.

A normal table with a header row (the separator row `| --- |`), its caption and a name for `ref()`; the header row is
repeated on every page, a list in a cell:

```markdown
{% call table('4cm', '3cm', '*', anchor='motorarten') %}
Tabelle: Motorarten
| Motor | Leistung | Einsatz |
| --- | --- | --- |
| Asynchronmotor | 0,5 – 500 kW | Förderband, Pumpe |
| Servomotor | 0,1 – 15 kW | - Robotik<br>- CNC-Maschinen |
{% endcall %}
```

A normal table without header row (no separator row: every row a normal one), in the line form `{{ table(…) }}`
directly before it:

```markdown
{{ table('4cm', '*') }}
| Spannung | 3 × 400 V AC |
| Frequenz | 50 Hz |
| Schutzart | IP55 |
```

A layout table (`type='layout'`): a text beside a picture with its caption, no lines; in the cell an empty line
`<br><br>` starts a new paragraph; the gap between the columns takes 0.25 cm of each, so the picture is a little
narrower than its column:

```markdown
{% call table('8.2cm', '7.8cm', type='layout') %}
| Die Gleichstrommaschine konnte sich lange behaupten.<br><br>Durch die Frequenzumrichter sind ihre Vorteile aufgehoben worden. | {{ image('images/1020.jpg', width='7.5cm', title='BLDC-Motor', numbered=False) }} |
{% endcall %}
```

A picture table (`type='pictures'`): pictures side by side, below each its caption; the table stays on one page:

```markdown
{% call table('8.2cm', '7.8cm', type='pictures') %}
| {{ image('images/0060.jpg', width='7.8cm') }} | {{ image('images/0070.png', width='7.8cm') }} |
| Keilbahnkupplung | Elastische Kupplung<br>Kann Vibrationen ausgleichen. |
{% endcall %}
```

### frame

`{{ frame(color='#FFC000') }}`, `{{ frame(color='#00B0F0', background='#E6F7FD', thickness='2pt') }}` — on a line of its
own directly before a paragraph or a list (no empty line between): that block in a box with a coloured frame, e.g. a
definition that stands out. Its lines are `color` (`#RRGGBB`, default the accent colour `#03A4C0`) and `thickness` wide
(pt, mm or cm, from 0.25 pt to 6 pt; default `1.5pt`), its background `background` (`#RRGGBB`; without one white). The
box has the indents of a `note()` box; its Markdown as usual (bold, italic, links, `formula()`, `index()`), a list
item with «– » (numbered: «1.», «2.», …) before its text. Each `frame()` is a box of its own (two one after another are
two boxes). A `frame()` without a paragraph or a list directly below it is a problem:

```markdown
{{ frame(color='#FFC000') }}
**Produkt = Inhaltliche Beschreibung des Bauteils (CAD Daten, Handskizze etc.)**

{{ frame(color='#00B0F0') }}
**Artikel = Organisatorische Einheit (Zusammenfassung der Daten), welche im System geführt wird.**
```

Several blocks in one box: `{% call frame(…) %}` and `{% endcall %}` on lines of their own around paragraphs, lists
and `formula()` lines, as with `note()`; nothing inside, another block (a heading, a table, a picture, a label, …) or
a note or frame inside is a problem.

### qr_code

`{{ qr_code('https://example.org/test') }}`, `{{ qr_code('https://example.org/test', '25mm', '#03A4C0', 'center') }}`
— the QR code of `text` on a line of its own, `size` wide and high with its white quiet zone (cm, mm, in or pt), its
modules in `color` (`#RRGGBB`), at the `alignment` of the text column: `'left'` (default), `'center'` or `'right'`. The render step makes it (viva_publisher_converter/toolbox/qr_code_image.py)
and writes it into the rendered folder (`qr_codes/`); without `text` the picture is a warning sign with «QR-CODE
FAILURE», as large, so a missing code shows.

### content

`{% call content(uuid='…') %} … {% endcall %}` — in a table cell (an HTML table's `<td>` or `<th>`, a pipe-table
cell): what it encloses gets the identifier `uuid` (required). A cell may hold several, and text between them:

```markdown
<td>{% call content(uuid='…') %}Motor<br>Typ B3{% endcall %}<br>{% call content(uuid='…') %}- Pumpe{% endcall %}<br>{% call content(uuid='…') %}- Lüfter{% endcall %}</td>
```

or, in an HTML cell, over several lines (line breaks are spaces, as in HTML; a new line of the cell's text needs a
`<br>`, as without the call):

```markdown
<td>
{% call content(uuid='…') %}
Die Gleichstrommaschine konnte sich … behaupten.
{% endcall %}
</td>
```

What a call encloses is written as the cell writes its text (lines, list items, pictures and their captions, formulas)
in paragraphs of its own, which the conversion puts in a content control tagged with the uuid (see **uuid**); the
text between two calls is a paragraph of its own, without one. A picture or formula keeps its own `uuid=` inside. A
numbered list item in a call of its own starts at its written number (number them `1.`, `2.`, `3.`); a call around
nothing visible (an author comment, which a cell drops) leaves the cell empty. Not as `{{ content() }}`; without
`uuid`, outside a table cell or with its `{% endcall %}` in another cell it is a problem; a `uuid()` in a table cell
too (it would be lost): `content()` identifies a cell's text.

### uuid

`# Antriebe aufbauen {{ uuid('ce52bc2d-f681-4a49-9d3b-e150292d042a') }}`,
`Die Spannung steigt. {{ uuid('0f8fad5b-d9cb-469f-a165-70867728950e') }}` — the identifier of a heading or a
paragraph, a UUID of version 4, after the text it identifies: in a heading at its end, in a paragraph after its text
(the end of its last line is the place to aim for). One per heading or paragraph; a list item is a paragraph of its own.
Alone on a line, before the text, inside a heading, a second one in a paragraph or one in a table cell (there:
[`content()`](#content)) is a problem. The conversion drops it with the spaces before it and puts the heading, paragraph or list
item in a content control tagged with it (see **uuid** above); the text shows nothing of it.

### grid

`{{ grid() }}`, `{{ grid(n_height=10) }}`, `{{ grid('4mm', 30, 20, '0.2mm', '#03A4C0', 'center') }}` — squared
paper on a line of its own: a grid of `n_width` × `n_height` squares, each `spacing` wide and high, its lines
`thickness` wide (both cm, mm, in, pt or px, above zero) in `color` (`#RRGGBB`), the background transparent, at the
`alignment` of the text column: `'left'` (default), `'center'` or `'right'`. The picture is `n_width * spacing +
thickness` wide (the outer lines in full); the default, 32 × 47 squares of 5 mm, fills the 16 cm text column and
nearly the height of a page's text. A grid wider than the text column is reduced to it (the default by its 0.15 mm
line). The render step makes it (viva_publisher_converter/toolbox/grid_image.py) and writes it into the rendered folder
(`grids/`).

### learning_objectives

`{{ learning_objectives() }}`, `{{ learning_objectives('2.5cm', '13.5cm') }}` — the next table as the learning
objectives, on a line of its own directly before a pipe table or an HTML table (no `Tabelle: …` line: the learning
objectives have no caption number), one objective per row: `| LZ_1057 | Sie erklären den Aufbau. |`; the separator row `| --- | --- |`
may be left out (the table has no header row). The table gets the style Learning Objectives Table (lines in the accent colour, no header row: its first row is an objective like the others) and
these column widths, given and checked as for `table()`; without widths `'2.3cm', '13.7cm'` (the id, the
text: the 16 cm text column). Both imports write it for an LZ table of the source (a first column of `LZ_…` numbers;
the template import also for a table in the style Learning Objectives Table), without separator row:

```markdown
{{ label('Lernziel', icon='learning_objective') }}

{% call learning_objectives() %}
| LZ_1057 | Sie erklären den Aufbau. |
| LZ_7865 | Sie benennen Geräte. |
{% endcall %}
```

The line form, `{{ learning_objectives() }}` directly before the table, is the same; in `{% call %}` … `{% endcall %}`
only the table may stand. The render step links each objective's id: a first cell of only an id `LZ_…` becomes
`{{ link('https://www.example.com/LZ_1057', 'LZ_1057') }}` (its page; md_render/commands/learning_objectives.py:
`OBJECTIVE_URL`), any other first cell stays; an id with `link_lo()` after it, too (the calls stay after the link).

### link_lo

`{{ link_lo('4DB5AA70-18E2-DC4F-9E3C-8C6650BD5BF9') }}`, `{{ link_lo('4DB5AA70-…', 'D004F129-…') }}` — the keys of a
learning objective in the database futuremem (link learning objective), in the first cell of its row of
`learning_objectives()`, right after the number of the objective; each key a GUID of 8-4-4-4-12 hexadecimal digits,
at least one:

```markdown
{% call learning_objectives() %}
| LZ_1057 {{ link_lo('4DB5AA70-18E2-DC4F-9E3C-8C6650BD5BF9', 'D004F129-989D-18BA-92A8-68F10EB3D8FC') }} | Sie erklären den Aufbau. |
| LZ_7865 {{ link_lo('1566CE6E-5F41-DDCD-81D2-44E2CBF1D575') }} | Sie benennen Geräte. |
{% endcall %}
```

The converter writes the keys as the Word comment `link_lo: <key>; <key>` of the author futuremem on the number, as
the authors write them (author guide, chapter 6.1.3); the PDF shows no comments. Several keys in one call are one
comment; several calls on one number, `| LZ_1057 {{ link_lo('…') }} {{ link_lo('…', '…') }} |`, one comment each. The
template import writes such a comment on the number of a learning objective back as `link_lo()`; a `link_lo:` comment
elsewhere or without a key, and any other comment, it leaves out, each with a note in `CONVERT.md`. Errors: no key, a
key that is no GUID, a keyword argument `keys=`,
a call anywhere else (in a paragraph, another cell, a normal table, before the number or with text after it).

### label

`{{ label('Lernziel', icon='learning_objective') }}`,
`{{ label('Selbstkontrolle', icon='arrow_right', link='https://example.org/test') }}`,
`{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}`,
`{{ label('Beispiel', icon='magnifying_glass') }}` — a label on a line of its own, e.g. above the learning
objectives, for a self-check, above the notes of a Hinweis or above an example: icon and text in a grey box (the style Label, accent
colour on grey) as wide as they are, at the left edge of the text column; the next block follows without an empty
line. `text` must not be empty; `icon` is a file name in `reference/template/icons/` without `.svg` (letters, digits,
`-`, `_`) and must exist; `link` (a URL: `https://…`, `http://…`, `mailto:…`) makes the label a hyperlink, clickable
in Word and in the PDF. `offset_x` (cm, mm, pt or % of the text column) moves the label this far to the right;
`offset_y` (cm, mm, pt or % of the label's height, at most the label's height of 15 pt) lets it reach this far down
into the box of the `note()` directly below it (the note colour behind that part of the label: `'50%'` puts the
label half on the box's top edge); `offset_y` without a `note()` as the next block is a problem. Both default to
`None`: no offset. The InDesign import writes the label of each LZ table, each Selbstkontrolle button (with its
hyperlink, if it has one, and a `qr_code()` below it) and each Hinweis (with `offset_x='4mm'`, the label's left edge
at the note text, and `offset_y='50%'`); the template import a `label()` for each paragraph in the style Label.

### list

`{% call list() %}` … `{% endcall %}` — a list (`- …`, `1. …`, also with its sub-items) between the two lines, each
on a line of its own: the list as it is without them; the call gives it its identifier (`uuid=`, as the imports
write it). Only as such a call (`{{ list() }}` is a problem), with one list inside and nothing else (no list or
another block is a problem); inside `{% call note() %}` its items are notes as without it:

```markdown
{% call list() %}
- Vorgehensweise
- benötigtes Material
- Wahl der Messinstrumente
{% endcall %}
```

### note

`{{ note() }}` — on a line of its own directly before a paragraph or a list (no empty line between): that block in
the style Note (a light blue box), its Markdown as usual (bold, italic, links, `formula()`, `index()`); a list item
gets «– » (numbered: «1.», «2.», …) before its text. Notes one after another form one box, without an empty paragraph
between them. A `note()` without a paragraph or a list directly below it is a problem. A Hinweis box below its label:

```markdown
{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}

{{ note() }}
Vor dem Einschalten die Motordaten prüfen.

{{ note() }}
- falsche Motordaten
- Rampe zu kurz
```

Several blocks in one note: `{% call note() %}` and `{% endcall %}` on lines of their own around paragraphs, lists
and `formula()` lines (empty lines between them as usual). They are written as if a `note()` stood before each of
them: one box, without empty paragraphs. Nothing inside, another block (a heading, a table, a picture, a label, …)
or a note inside is a problem. The InDesign import writes the paragraphs and lists of each Hinweis box so, below its
label; the template import the paragraphs in the style Note:

```markdown
{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}

{% call note() %}
Sicherheit steht auch hier an oberster Stelle.

- Anlage spannungsfrei schalten
- gegen Wiedereinschalten sichern

{{ formula('U = R \cdot I') }}
{% endcall %}
```
