# Text und Struktur {{ anchor('kap_text', uuid='837709d0-6103-414f-8c47-c014602b5137') }} {{ uuid('5cf944f3-63a6-4de5-ad9e-a282051746e3') }}

Dieses Kapitel zeigt, wie Sie Fliesstext, Überschriften, Listen und Verweise im {{ index('Markdown', uuid='922b2aef-1c5b-470e-8d52-f34f5a1aa499') }}Markdown schreiben. Jeder Abschnitt zeigt zuerst das Ergebnis und darunter den Markdown-Code, der es erzeugt. Die Befehle in doppelten geschweiften Klammern prüft das Rendern; ein Fehler nennt Datei und Zeile. {{ uuid('f4185260-c1dd-47e8-8413-652be648fc0d') }}

## Überschriften {{ anchor('ueberschriften', uuid='efeac783-6637-4920-ba5f-0d48dcd3509e') }} {{ uuid('1b833f17-1097-4d16-8658-4283540570da') }}

Ein Kapitel beginnt mit genau einer Überschrift `#`: Sie steht im Farbband der Kapitelseite. Darunter gliedern `##` und `###` den Text, nummeriert wie 1.1 und 1.1.1. Eine Überschrift `####` ist eine Zwischenüberschrift ohne Nummer. Mit `anchor()` am Ende der Überschrift erhält sie einen Namen, auf den Sie verweisen können. {{ uuid('ff604825-a753-44e8-89e8-8e025b25401f') }}

### Eine Überschrift der dritten Ebene {{ uuid('95ed5b6c-9d86-4dc3-aa39-2e309d228619') }}

Text unter einer Überschrift der dritten Ebene. {{ uuid('eba9f414-d7fa-4814-b8eb-43cb27b50b0b') }}

#### Eine Zwischenüberschrift ohne Nummer {{ uuid('24f4e156-ccb8-4c3d-88e7-b968a226da24') }}

Text unter einer Zwischenüberschrift. {{ uuid('e9293ab7-c494-4a3c-a64e-7d6c766dbd7f') }}

{% raw %}
```markdown
# Text und Struktur {{ anchor('kap_text') }}
## Überschriften {{ anchor('ueberschriften') }}
### Eine Überschrift der dritten Ebene
#### Eine Zwischenüberschrift ohne Nummer
```
{% endraw %}

## Auszeichnungen im Text {{ uuid('703c11ca-9980-4246-bd6f-3eb768ef0f51') }}

Text kann **fett** oder *kursiv* sein; zwischen Backticks bleibt er, wie er ist: `**nicht fett**`. Farbiger Text steht in `color()`: {{ color('Lebensgefahr!', uuid='1a0bfd61-a054-4f3a-b95e-d5ee16c3ece3') }} erscheint in Signalrot, {{ color('**grün und fett**', '#00B050', uuid='4a4f391a-513f-4286-aa65-7da720ed77ba') }} in einer eigenen Farbe. Innerhalb von fettem Text bleibt die Farbe fett: **Warnung: {{ color('Starkstrom', uuid='d40eb3b4-1387-4dbd-bde9-ee97db43efce') }}**. {{ uuid('b13890e1-9882-4c55-b0e3-0bbbbac8ae22') }}

Ein Zeilenumbruch innerhalb eines Absatzes entsteht mit `<br>`:<br>Diese Zeile beginnt neu, gehört aber zum selben Absatz. {{ uuid('d1d70a6f-3af8-4640-9f64-1cd92213a0d9') }}

Ein Backslash vor einem Satzzeichen macht es zu gewöhnlichem Text: {{ uuid('fc752b49-16c5-4d1e-bfbb-d52e4a5da8f5') }}

3\. Schritt: Diese Zeile beginnt mit Zahl und Punkt, ist aber keine Liste. {{ uuid('ae9399ea-166d-487f-97bb-16ac1fbec4af') }}

\# Diese Zeile beginnt mit einem Rautezeichen, ist aber keine Überschrift. {{ uuid('ddfff0a8-c231-4d56-a58b-dafbb18d31d6') }}

Das Produkt 2\*3\*4 ergibt 24, ohne dass ein Teil kursiv wird. {{ uuid('fd10d0f2-a0bb-4d0e-a98a-6f417b8b2874') }}

{% raw %}
```markdown
Text kann **fett** oder *kursiv* sein; zwischen Backticks bleibt er, wie er ist: `**nicht fett**`.
{{ color('Lebensgefahr!') }}  {{ color('**grün und fett**', '#00B050') }}  **Warnung: {{ color('Starkstrom') }}**
Ein Zeilenumbruch mit `<br>`:<br>Diese Zeile beginnt neu.
3\. Schritt …   \# Diese Zeile …   2\*3\*4
```
{% endraw %}

## Listen {{ uuid('0ee2a61e-ac5b-459b-844b-1cebe6e3bd3b') }}

Aufzählungen beginnen mit `-`, nummerierte Listen mit `1.`; eingerückte Einträge bilden eine zweite Ebene: {{ uuid('13145f23-0755-4556-b1b7-18e6bb0b484c') }}

{% call list(uuid='bba3e786-1968-4ef3-8b4d-17d2045c59c6') %}
- Manuskript in Markdown schreiben
- Befehle einfügen
    - Bilder mit `image()`
    - Formeln mit `formula()`
- Dokument rendern und prüfen
{% endcall %}

{% call list(uuid='54f352c3-0928-4c28-aa7d-dc9723c00897') %}
1. Ordner `demo_starter` kopieren
1. Texte und Bilder ersetzen
1. Word-Dokument und PDF erstellen
{% endcall %}

Eine nummerierte Liste beginnt mit der Nummer ihres ersten Eintrags: {{ uuid('738e565a-a17e-4651-8143-eed7af35d095') }}

{% call list(uuid='73d25d3f-0e4f-4a4c-a793-db0366cad1a1') %}
3. dritter Schritt
4. vierter Schritt
{% endcall %}

Mit `{% raw %}{% call list() %}{% endraw %}` erhält eine Liste einen Identifikator, wie ihn die Word-Importe schreiben: {{ uuid('539e983b-308a-4c5e-9c04-cf27b8c1aef3') }}

{% call list(uuid='ae418e6b-e421-4904-bf04-9d67c638237c') %}
- Vorgehensweise
- benötigtes Material
- Wahl der Messinstrumente
{% endcall %}

{% raw %}
```markdown
- Manuskript in Markdown schreiben
- Befehle einfügen
    - Bilder mit `image()`
1. Ordner `demo_starter` kopieren
3. dritter Schritt

{% call list(uuid='ae418e6b-e421-4904-bf04-9d67c638237c') %}
- Vorgehensweise
{% endcall %}
```
{% endraw %}

## Links und Verweise {{ uuid('e5884472-9459-46ef-a442-223e9d81405d') }}

Ein Link führt zu einer Webseite: {{ link('https://commonmark.org', 'CommonMark', uuid='d31406dd-aba7-42d6-8bcb-8776b0114faa') }} oder, als Markdown-Link, [Jinja](https://jinja.palletsprojects.com/). Ohne Text zeigt der Link seine Adresse: {{ link('mailto:redaktion@example.org', uuid='f51fc360-67b4-4d44-9f56-ac73b196ba79') }}. {{ uuid('f8bde6e4-5ae3-4d10-93ba-7d0975458522') }}

Ein Verweis mit `ref()` nennt die Nummer, den Titel oder die Seite seines Ziels und ist im PDF anklickbar. Der Abschnitt {{ ref('ueberschriften', uuid='74ef8c25-eeb6-4481-a875-d2108fb2931e') }} heisst «{{ ref('ueberschriften', 'title', uuid='c4a6584d-b81f-4028-92f4-1cc412e4aa9b') }}» und steht auf Seite {{ ref('ueberschriften', 'page', uuid='cd737490-7cae-4050-bcc4-7dd5625c59ad') }}. {{ ref('abb_workflow', uuid='1b8d5b6c-5143-48ff-b4c0-c05548d304f0') }} zeigt den Weg vom Manuskript zum PDF, {{ ref('tab_einheiten', uuid='43b50fd0-6055-45b3-b437-c7e13fde66e9') }} auf Seite {{ ref('tab_einheiten', 'page', uuid='0aa1647e-d4b6-4af3-808c-53aa365babef') }} die SI-Basiseinheiten. Das Ziel darf auch in einem späteren Kapitel stehen. {{ uuid('861279c1-925b-476a-963f-d188a696ea1a') }}

{% raw %}
```markdown
{{ link('https://commonmark.org', 'CommonMark') }}   [Jinja](https://jinja.palletsprojects.com/)
{{ link('mailto:redaktion@example.org') }}
Der Abschnitt {{ ref('ueberschriften') }} heisst «{{ ref('ueberschriften', 'title') }}»
und steht auf Seite {{ ref('ueberschriften', 'page') }}.
{{ ref('abb_workflow') }} zeigt …   {{ ref('tab_einheiten') }} auf Seite {{ ref('tab_einheiten', 'page') }}
```
{% endraw %}

## Fussnoten, Quellen und Stichwörter {{ uuid('d66bcfdb-0147-4a5b-96e8-bf74ad4ed60b') }}

Eine Fussnote{{ footnote('Der Text einer Fussnote steht unten auf der Seite; er darf **fett**, *kursiv* oder ein [Link](https://commonmark.org) sein.', uuid='5aabf3b7-9851-4dc3-88e7-63f7c19ab3b1') }} setzt ihre Nummer an die Stelle im Text. Die Nummern beginnen in jedem Kapitel bei 1{{ footnote('Die zweite Fussnote dieses Kapitels.', uuid='acbe0c4c-4fb2-4904-a772-5e30a359ed39') }}. {{ uuid('4b6f4abd-4520-4b5c-8ed0-651362b707e6') }}

Quellen zitieren Sie mit `cite()`: Die Syntax von Markdown ist in der CommonMark-Spezifikation festgelegt {{ cite('commonmark', uuid='c895c3e3-a3c3-4c52-84c0-d978a337814d') }}, die Formeln folgen der Schreibweise von LaTeX {{ cite('lamport1994', '23–25', uuid='09f4d33d-005e-4161-93e3-ad27fb278632') }}. Die Nummern zählen in der Reihenfolge der ersten Zitate; das Quellenverzeichnis am Ende listet nur die zitierten Einträge. {{ uuid('477b55ef-b74b-464d-a5db-b13c2b390a67') }}

Ein {{ index('Stichwort', uuid='31abe318-1749-4995-b0d4-f6209c846bfd') }}Stichwort für das Stichwortverzeichnis setzen Sie mit `index()` direkt vor das Wort, ein Unterstichwort mit einem zweiten Argument: die {{ index('Fussnote', 'Nummerierung', uuid='b70d4a71-e807-4b99-ba66-a8a7ecea93bd') }}Nummerierung der Fussnoten, der {{ index('Verweis', 'auf Abschnitte', uuid='12e83124-8fe0-4033-80fd-de453351cef9') }}Verweis auf einen Abschnitt. {{ uuid('92a90e8f-ad05-4371-8089-a19cedabfaa8') }}

{% raw %}
```markdown
Eine Fussnote{{ footnote('Der Text einer Fussnote steht unten auf der Seite.') }} setzt …
… festgelegt {{ cite('commonmark') }} … LaTeX {{ cite('lamport1994', '23–25') }}.
Ein {{ index('Stichwort') }}Stichwort …  die {{ index('Fussnote', 'Nummerierung') }}Nummerierung …
```
{% endraw %}

## Identifikatoren {{ uuid('c554c85c-8452-4021-84a0-0100423e7444') }}

Jede Überschrift und jeder Absatz kann am Ende einen Identifikator `uuid()` tragen; jeder Befehl nimmt ihn als Argument `uuid=`. Im Word-Dokument steht der Block dann in einem Inhaltssteuerelement mit diesem Identifikator. Die Word-Importe schreiben ihn an jeden Block, damit Änderungen in Word ihrem Block im Markdown zugeordnet werden können. Dieser Absatz trägt einen. {{ uuid('ccde7461-61cd-4e2f-918a-5677649eccad') }}

{% raw %}
```markdown
## Identifikatoren {{ uuid('c554c85c-8452-4021-84a0-0100423e7444') }}
… Dieser Absatz trägt einen. {{ uuid('ccde7461-61cd-4e2f-918a-5677649eccad') }}
{{ image('images/bauteil.png', width='6cm', uuid='3082ec75-46da-4614-b452-1f4f9b1ad77a') }}
```
{% endraw %}

## Kommentare und Code {{ uuid('5c344d44-2e88-4a82-8c8a-6b00337b424d') }}

Was nicht ins Dokument gehört, schreiben Sie als Kommentar. {% raw %}`{# … #}`{% endraw %} und `[//]: # (…)` entfernt das Rendern ganz: Nach diesem Absatz stehen zwei solche Kommentare, sichtbar ist keiner. {{ uuid('2de197c6-342c-4472-b5e8-2cb0b6415954') }}

{# Ein Jinja-Kommentar: für Notizen im Markdown. #}
[//]: # (Ein Markdown-Kommentar: verschwindet ebenfalls.)

Ein HTML-Kommentar dagegen wird ein Autorenkommentar in der Formatvorlage Author Comment, eine Notiz an Lektorat oder Satz:

<!-- Autorenkommentar: Bitte das Foto der Druckmaschine noch nachliefern. -->

Ein Codeblock zwischen drei Backticks erscheint eingerückt, Zeile für Zeile, so wie die Beispiele in diesem Dokument:

```python
def flaeche(breite: float, hoehe: float) -> float:
    return breite * hoehe
```

{% raw %}
```markdown
{# Ein Jinja-Kommentar #}
[//]: # (Ein Markdown-Kommentar)
<!-- Autorenkommentar: Bitte das Foto der Druckmaschine noch nachliefern. -->
```
{% endraw %}

## Seitenumbruch

Mit `page_break()` auf einer eigenen Zeile beginnt der nächste Block auf einer neuen Seite. Setzen Sie ihn sparsam ein: Die Formatvorlagen übernehmen das Layout.

{{ page_break() }}

Dieser Absatz steht nach `{% raw %}{{ page_break() }}{% endraw %}` oben auf einer neuen Seite.
