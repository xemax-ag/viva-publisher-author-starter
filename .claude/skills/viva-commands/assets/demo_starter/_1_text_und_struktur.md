# Text und Struktur {{ anchor('kap_text') }}

Dieses Kapitel zeigt, wie Sie Fliesstext, Überschriften, Listen und Verweise im {{ index('Markdown') }}Markdown schreiben. Jeder Abschnitt zeigt zuerst das Ergebnis und darunter den Markdown-Code, der es erzeugt. Die Befehle in doppelten geschweiften Klammern prüft das Rendern; ein Fehler nennt Datei und Zeile.

## Überschriften {{ anchor('ueberschriften') }}

Ein Kapitel beginnt mit genau einer Überschrift `#`: Sie steht im Farbband der Kapitelseite. Darunter gliedern `##` und `###` den Text, nummeriert wie 1.1 und 1.1.1. Eine Überschrift `####` ist eine Zwischenüberschrift ohne Nummer. Mit `anchor()` am Ende der Überschrift erhält sie einen Namen, auf den Sie verweisen können.

### Eine Überschrift der dritten Ebene

Text unter einer Überschrift der dritten Ebene.

#### Eine Zwischenüberschrift ohne Nummer

Text unter einer Zwischenüberschrift.

{% raw %}
```markdown
# Text und Struktur {{ anchor('kap_text') }}
## Überschriften {{ anchor('ueberschriften') }}
### Eine Überschrift der dritten Ebene
#### Eine Zwischenüberschrift ohne Nummer
```
{% endraw %}

## Auszeichnungen im Text

Text kann **fett** oder *kursiv* sein; zwischen Backticks bleibt er, wie er ist: `**nicht fett**`. Farbiger Text steht in `color()`: {{ color('Lebensgefahr!') }} erscheint in Signalrot, {{ color('**grün und fett**', '#00B050') }} in einer eigenen Farbe. Innerhalb von fettem Text bleibt die Farbe fett: **Warnung: {{ color('Starkstrom') }}**.

Ein Zeilenumbruch innerhalb eines Absatzes entsteht mit `<br>`:<br>Diese Zeile beginnt neu, gehört aber zum selben Absatz.

Ein Backslash vor einem Satzzeichen macht es zu gewöhnlichem Text:

3\. Schritt: Diese Zeile beginnt mit Zahl und Punkt, ist aber keine Liste.

\# Diese Zeile beginnt mit einem Rautezeichen, ist aber keine Überschrift.

Das Produkt 2\*3\*4 ergibt 24, ohne dass ein Teil kursiv wird.

{% raw %}
```markdown
Text kann **fett** oder *kursiv* sein; zwischen Backticks bleibt er, wie er ist: `**nicht fett**`.
{{ color('Lebensgefahr!') }}  {{ color('**grün und fett**', '#00B050') }}  **Warnung: {{ color('Starkstrom') }}**
Ein Zeilenumbruch mit `<br>`:<br>Diese Zeile beginnt neu.
3\. Schritt …   \# Diese Zeile …   2\*3\*4
```
{% endraw %}

## Listen

Aufzählungen beginnen mit `-`, nummerierte Listen mit `1.`; eingerückte Einträge bilden eine zweite Ebene:

- Manuskript in Markdown schreiben
- Befehle einfügen
    - Bilder mit `image()`
    - Formeln mit `formula()`
- Dokument rendern und prüfen

1. Ordner `demo_starter` kopieren
1. Texte und Bilder ersetzen
1. Word-Dokument und PDF erstellen

Eine nummerierte Liste beginnt mit der Nummer ihres ersten Eintrags:

3. dritter Schritt
4. vierter Schritt

Mit `{% raw %}{% call list() %}{% endraw %}` erhält eine Liste einen Identifikator, wie ihn die Word-Importe schreiben:

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

## Links und Verweise

Ein Link führt zu einer Webseite: {{ link('https://commonmark.org', 'CommonMark') }} oder, als Markdown-Link, [Jinja](https://jinja.palletsprojects.com/). Ohne Text zeigt der Link seine Adresse: {{ link('mailto:redaktion@example.org') }}.

Ein Verweis mit `ref()` nennt die Nummer, den Titel oder die Seite seines Ziels und ist im PDF anklickbar. Der Abschnitt {{ ref('ueberschriften') }} heisst «{{ ref('ueberschriften', 'title') }}» und steht auf Seite {{ ref('ueberschriften', 'page') }}. {{ ref('abb_workflow') }} zeigt den Weg vom Manuskript zum PDF, {{ ref('tab_einheiten') }} auf Seite {{ ref('tab_einheiten', 'page') }} die SI-Basiseinheiten. Das Ziel darf auch in einem späteren Kapitel stehen.

{% raw %}
```markdown
{{ link('https://commonmark.org', 'CommonMark') }}   [Jinja](https://jinja.palletsprojects.com/)
{{ link('mailto:redaktion@example.org') }}
Der Abschnitt {{ ref('ueberschriften') }} heisst «{{ ref('ueberschriften', 'title') }}»
und steht auf Seite {{ ref('ueberschriften', 'page') }}.
{{ ref('abb_workflow') }} zeigt …   {{ ref('tab_einheiten') }} auf Seite {{ ref('tab_einheiten', 'page') }}
```
{% endraw %}

## Fussnoten, Quellen und Stichwörter

Eine Fussnote{{ footnote('Der Text einer Fussnote steht unten auf der Seite; er darf **fett**, *kursiv* oder ein [Link](https://commonmark.org) sein.') }} setzt ihre Nummer an die Stelle im Text. Die Nummern beginnen in jedem Kapitel bei 1{{ footnote('Die zweite Fussnote dieses Kapitels.') }}.

Quellen zitieren Sie mit `cite()`: Die Syntax von Markdown ist in der CommonMark-Spezifikation festgelegt {{ cite('commonmark') }}, die Formeln folgen der Schreibweise von LaTeX {{ cite('lamport1994', '23–25') }}. Die Nummern zählen in der Reihenfolge der ersten Zitate; das Quellenverzeichnis am Ende listet nur die zitierten Einträge.

Ein {{ index('Stichwort') }}Stichwort für das Stichwortverzeichnis setzen Sie mit `index()` direkt vor das Wort, ein Unterstichwort mit einem zweiten Argument: die {{ index('Fussnote', 'Nummerierung') }}Nummerierung der Fussnoten, der {{ index('Verweis', 'auf Abschnitte') }}Verweis auf einen Abschnitt.

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

## Kommentare und Code

Was nicht ins Dokument gehört, schreiben Sie als Kommentar. {% raw %}`{# … #}`{% endraw %} und `[//]: # (…)` entfernt das Rendern ganz: Nach diesem Absatz stehen zwei solche Kommentare, sichtbar ist keiner.

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
