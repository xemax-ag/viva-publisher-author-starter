# Tabellen {{ anchor('kap_tabellen') }}

Eine Tabelle schreiben Sie als Pipe-Tabelle, eine Zeile pro Tabellenzeile, oder als HTML-Tabelle, wenn Zellen über mehrere Zeilen oder Spalten reichen. Eine Zeile `Tabelle: Titel` direkt davor wird die nummerierte Tabellenüberschrift, die das Tabellenverzeichnis aufführt. `table()` davor legt die Spaltenbreiten fest.

## Einfache Tabelle

Die Trennzeile `| --- |` macht die erste Zeile zur Kopfzeile, die auf jeder Seite wiederholt wird. Ohne `table()` teilen sich die Spalten die Textspalte gleichmässig.

Tabelle: Dateien eines Dokuments
| Datei | Inhalt |
| --- | --- |
| `_main_.md` | das Manifest: Titelseite, Kapitel und Verzeichnisse |
| `cover.md` | die Zeilen im Farbband der Titelseite |
| `_1_text_und_struktur.md` | ein Kapitel |
| `images` | die Bilder der Kapitel |

{% raw %}
```markdown
Tabelle: Dateien eines Dokuments
| Datei | Inhalt |
| --- | --- |
| `_main_.md` | das Manifest: Titelseite, Kapitel und Verzeichnisse |
```
{% endraw %}

## Spaltenbreiten und Verweis

Eine Breite pro Spalte, in cm, mm, pt oder Prozent; die Spalten mit `*` teilen sich den Rest. `anchor` macht die Tabelle zum Ziel eines Verweises: {{ ref('tab_einheiten') }} nennt die sieben Basiseinheiten des Internationalen Einheitensystems {{ cite('iso80000') }}.

{% call table('5.5cm', '3cm', '*', anchor='tab_einheiten') %}
Tabelle: SI-Basiseinheiten
| Grösse | Einheit | Zeichen |
| --- | --- | --- |
| Länge | Meter | m |
| Masse | Kilogramm | kg |
| Zeit | Sekunde | s |
| elektrische Stromstärke | Ampere | A |
| thermodynamische Temperatur | Kelvin | K |
| Stoffmenge | Mol | mol |
| Lichtstärke | Candela | cd |
{% endcall %}

{% raw %}
```markdown
{% call table('5.5cm', '3cm', '*', anchor='tab_einheiten') %}
Tabelle: SI-Basiseinheiten
| Grösse | Einheit | Zeichen |
| --- | --- | --- |
| Länge | Meter | m |
{% endcall %}
```
{% endraw %}

## Ohne Kopfzeile, ohne Nummer

Ohne Trennzeile ist jede Zeile eine normale Zeile. Hier steht `table()` als einzelne Zeile direkt vor der Tabelle; zwei feste Breiten unter 16 cm ergeben eine schmalere Tabelle:

{{ table('4cm', '6cm') }}
| Format | A4 hoch |
| Textspalte | 16 cm |
| Schrift | Roboto |

Mit `numbered=False` steht nur der Titel über der Tabelle, ohne «Tabelle n:»:

{% call table('4cm', '*', numbered=False) %}
Tabelle: Seitenränder der Vorlage
| oben | 35,2 mm |
| unten | 23,7 mm |
{% endcall %}

{% raw %}
```markdown
{{ table('4cm', '6cm') }}
| Format | A4 hoch |
| Textspalte | 16 cm |

{% call table('4cm', '*', numbered=False) %}
Tabelle: Seitenränder der Vorlage
| oben | 35,2 mm |
{% endcall %}
```
{% endraw %}

## HTML-Tabelle mit verbundenen Zellen

`colspan` verbindet Zellen nebeneinander, `rowspan` untereinander. Die Zeilen in `<thead>` sind Kopfzeilen. In einer Zelle stehen Text mit Markdown, Listen nach `<br>`, Formeln und Bilder:

{% call table('2.4cm', '2.4cm', '2.4cm', '*', anchor='tab_bildformate') %}
Tabelle: Bildformate im Vergleich
<table>
  <thead>
    <tr>
      <th rowspan="2">Format</th>
      <th colspan="2">Eigenschaften</th>
      <th rowspan="2">Geeignet für</th>
    </tr>
    <tr><th>Vektor</th><th>Transparenz</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>SVG</strong></td><td>ja</td><td>ja</td>
      <td>Geeignet für:<br>- Diagramme<br>- technische Zeichnungen<br>{{ image('images/workflow.svg', width='5cm') }}</td>
    </tr>
    <tr>
      <td><strong>PNG</strong></td><td>nein</td><td>ja</td>
      <td>Bildschirmfotos und Raster mit mindestens 150 dpi, also {{ formula('\frac{1800\,\text{px}}{300\,\text{dpi}} = 6\,\text{in}') }}</td>
    </tr>
    <tr>
      <td><strong>JPG</strong></td><td colspan="2"><em>weder noch</em></td><td>Fotos</td>
    </tr>
  </tbody>
</table>
{% endcall %}

{% raw %}
```markdown
{% call table('2.4cm', '2.4cm', '2.4cm', '*', anchor='tab_bildformate') %}
Tabelle: Bildformate im Vergleich
<table>
  <thead>
    <tr><th rowspan="2">Format</th><th colspan="2">Eigenschaften</th><th rowspan="2">Geeignet für</th></tr>
    <tr><th>Vektor</th><th>Transparenz</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>SVG</strong></td><td>ja</td><td>ja</td>
        <td>Geeignet für:<br>- Diagramme<br>{{ image('images/workflow.svg', width='5cm') }}</td></tr>
    <tr><td><strong>JPG</strong></td><td colspan="2"><em>weder noch</em></td><td>Fotos</td></tr>
  </tbody>
</table>
{% endcall %}
```
{% endraw %}

## Ausrichtung, gedrehter Text und Lösungen in Zellen

Auf `<td>` und `<th>` einer HTML-Tabelle legen `align` (`left`, `center`, `right`) und `valign` (`top`, `middle`, `bottom`) fest, wo der Text in der Zelle steht; `vertical` dreht ihn (`up`: von unten nach oben, `down`: von oben nach unten):

{% call table('1.5cm', '5cm', '5cm', '*') %}
<table>
  <thead>
    <tr><th></th><th>Links, oben</th><th align="center">Zentriert, Mitte</th><th align="right">Rechts, unten</th></tr>
  </thead>
  <tr>
    <td vertical="up" align="center" valign="middle">Werte</td>
    <td>Zeile 1<br>Zeile 2<br>Zeile 3</td>
    <td align="center" valign="middle">Mitte</td>
    <td align="right" valign="bottom">unten</td>
  </tr>
</table>
{% endcall %}

`solution` ohne Wert setzt eine Zelle in die Formatvorlage Solutions, rot wie eine Lösung, z. B. die Kreuze einer Selbstkontrolle:

{% call table('1.5cm', '*') %}
<table>
  <tr><td solution align="center">X</td><td>Freiformflächen sind stetig gekrümmt.</td></tr>
  <tr><td align="center">□</td><td>Freiformflächen sind immer eben.</td></tr>
</table>
{% endcall %}

{% raw %}
```markdown
<tr>
  <td vertical="up" align="center" valign="middle">Werte</td>
  <td align="center" valign="middle">Mitte</td>
  <td align="right" valign="bottom">unten</td>
</tr>
<tr><td solution align="center">X</td><td>Freiformflächen sind stetig gekrümmt.</td></tr>
```
{% endraw %}

## Bilder nebeneinander

`type='pictures'` setzt Bilder ohne Linien nebeneinander, unter jedem seine Beschriftung; die Tabelle bleibt auf einer Seite und hat keine Tabellennummer.

{% call table('8cm', '8cm', type='pictures') %}
| {{ image('images/bauteil.png', width='7.5cm') }} | {{ image('images/diagramm.svg', width='7.5cm') }} |
| Flansch<br>technische Zeichnung als PNG | Monatswerte<br>Diagramm als SVG |
{% endcall %}

{% raw %}
```markdown
{% call table('8cm', '8cm', type='pictures') %}
| {{ image('images/bauteil.png', width='7.5cm') }} | {{ image('images/diagramm.svg', width='7.5cm') }} |
| Flansch<br>technische Zeichnung als PNG | Monatswerte<br>Diagramm als SVG |
{% endcall %}
```
{% endraw %}

## Text und Bild in Spalten

`type='layout'` stellt Text und Bilder in Spalten nebeneinander, ohne Linien; der Text bleibt Fliesstext. `<br><br>` beginnt einen neuen Absatz. Ein Bild mit `title` erhält seine Bildunterschrift.

{% call table('8.5cm', '7.5cm', type='layout') %}
| Das Diagramm rechts zeigt Monatswerte als Balken, die Linie darüber ihren Verlauf.<br><br>In einer Layouttabelle steht das Bild neben dem Text, der es beschreibt, statt darunter. So bleibt die Seite ruhig, und Lernende sehen Text und Bild zugleich. | {{ image('images/diagramm.svg', width='7cm', title='Monatswerte als Balkendiagramm') }} |
{% endcall %}

{% raw %}
```markdown
{% call table('8.5cm', '7.5cm', type='layout') %}
| Das Diagramm rechts …<br><br>In einer Layouttabelle … | {{ image('images/diagramm.svg', width='7cm', title='Monatswerte als Balkendiagramm') }} |
{% endcall %}
```
{% endraw %}

## Inhalte in Zellen kennzeichnen

`content()` gibt einem Teil einer Zelle einen Identifikator, so wie `uuid()` einem Absatz; eine Zelle kann mehrere enthalten:

{{ table('4cm', '*') }}
| Bauteil | Prüfung |
| --- | --- |
| Flansch | {% call content(uuid='d4bc4cef-25be-4e21-854b-a6bc4461aa47') %}Sichtprüfung vor der Montage{% endcall %}<br>{% call content(uuid='a62024f9-0f59-409f-8aa5-e3d8f38e9da8') %}- Lochkreis messen{% endcall %}<br>{% call content(uuid='a6bf6cb2-ca71-4aed-9905-bdd636610794') %}- Dichtfläche reinigen{% endcall %} |

{% raw %}
```markdown
| Flansch | {% call content(uuid='d4bc4cef-…') %}Sichtprüfung vor der Montage{% endcall %}<br>{% call content(uuid='a62024f9-…') %}- Lochkreis messen{% endcall %} |
```
{% endraw %}
