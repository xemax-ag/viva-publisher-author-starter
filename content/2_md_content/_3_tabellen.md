# Tabellen {{ anchor('kap_tabellen', uuid='60a8fbdc-33c2-4f5b-92b6-de0037e76cf8') }} {{ uuid('d9c3ed9a-71fc-40d7-811f-02830086fff3') }}

Eine Tabelle schreiben Sie als Pipe-Tabelle, eine Zeile pro Tabellenzeile, oder als HTML-Tabelle, wenn Zellen über mehrere Zeilen oder Spalten reichen. Eine Zeile `Tabelle: Titel` direkt davor wird die nummerierte Tabellenüberschrift, die das Tabellenverzeichnis aufführt. `table()` davor legt die Spaltenbreiten fest. {{ uuid('7feddcb7-13a8-498c-bf0a-a9b6cbf58fc3') }}

## Einfache Tabelle {{ uuid('82804fe9-e41e-4c12-8a2f-3a2b08968275') }}

Die Trennzeile `| --- |` macht die erste Zeile zur Kopfzeile, die auf jeder Seite wiederholt wird. Ohne `table()` teilen sich die Spalten die Textspalte gleichmässig. {{ uuid('3a248cc8-fa8a-4dc1-848e-ee357cd381d7') }}

{{ table(uuid='8e4dcc33-ce21-48d0-9fac-10d9a96d3a7c') }}
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

## Spaltenbreiten und Verweis {{ uuid('3939bb96-451d-46a4-8dfd-9462fbcc2504') }}

Eine Breite pro Spalte, in cm, mm, pt oder Prozent; die Spalten mit `*` teilen sich den Rest. `anchor` macht die Tabelle zum Ziel eines Verweises: {{ ref('tab_einheiten', uuid='e98ec731-71a5-4505-aef1-f9d999729532') }} nennt die sieben Basiseinheiten des Internationalen Einheitensystems {{ cite('iso80000', uuid='6218e319-8843-4496-9c8a-8a89b4ea09a5') }}. {{ uuid('e293f6d0-6806-4405-8c28-c0e0a3df4cd9') }}

{% call table('5.5cm', '3cm', '*', anchor='tab_einheiten', uuid='f110b4ce-47b3-4d2d-b9cc-c155b84b665e') %}
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

## Ohne Kopfzeile, ohne Nummer {{ uuid('1705e7c6-c3bc-4828-8995-01caf7c32168') }}

Ohne Trennzeile ist jede Zeile eine normale Zeile. Hier steht `table()` als einzelne Zeile direkt vor der Tabelle; zwei feste Breiten unter 16 cm ergeben eine schmalere Tabelle: {{ uuid('f9e3380c-154a-44c7-a8e4-368439d0ad71') }}

{{ table('4cm', '6cm', uuid='5a6e21f9-4bcc-4e38-95c7-df0ac92d6d9e') }}
| Format | A4 hoch |
| Textspalte | 16 cm |
| Schrift | Roboto |

Mit `numbered=False` steht nur der Titel über der Tabelle, ohne «Tabelle n:»: {{ uuid('388ffcc2-15ec-46eb-9dc3-f99c60674fdf') }}

{% call table('4cm', '*', numbered=False, uuid='56596974-73dc-4882-816a-df207fb9fee4') %}
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

## HTML-Tabelle mit verbundenen Zellen {{ uuid('490be495-9721-41b6-ba85-2ccdd3878b1a') }}

`colspan` verbindet Zellen nebeneinander, `rowspan` untereinander. Die Zeilen in `<thead>` sind Kopfzeilen. In einer Zelle stehen Text mit Markdown, Listen nach `<br>`, Formeln und Bilder: {{ uuid('5cc3483b-e4d7-4326-8e33-6dd222bc92c9') }}

{% call table('2.4cm', '2.4cm', '2.4cm', '*', anchor='tab_bildformate', uuid='2ae5698c-bc16-4520-b3ac-e5e96e617052') %}
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
      <td>Geeignet für:<br>- Diagramme<br>- technische Zeichnungen<br>{{ image('images/workflow.svg', width='5cm', uuid='d0de30a0-fd93-4d2c-86ac-b49bf1276c01') }}</td>
    </tr>
    <tr>
      <td><strong>PNG</strong></td><td>nein</td><td>ja</td>
      <td>Bildschirmfotos und Raster mit mindestens 150 dpi, also {{ formula('\frac{1800\,\text{px}}{300\,\text{dpi}} = 6\,\text{in}', uuid='07c71e11-ae9d-4026-8618-0208d6334e44') }}</td>
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

## Bilder nebeneinander {{ uuid('75d258b2-592a-4026-b8ba-f9ce6d02a982') }}

`type='pictures'` setzt Bilder ohne Linien nebeneinander, unter jedem seine Beschriftung; die Tabelle bleibt auf einer Seite und hat keine Tabellennummer. {{ uuid('3440578d-7d2a-4762-98f7-618748559b57') }}

{% call table('8cm', '8cm', type='pictures', uuid='287cc8b3-a72b-499c-b99a-031e82877025') %}
| {{ image('images/bauteil.png', width='7.5cm', uuid='40b25d47-65b8-43f6-9c11-455d8deeff31') }} | {{ image('images/diagramm.svg', width='7.5cm', uuid='263759f8-f6b1-4463-8132-17e4cd1466e5') }} |
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

## Text und Bild in Spalten {{ uuid('246c0e4f-932b-4ea4-af95-61d6c22660c0') }}

`type='layout'` stellt Text und Bilder in Spalten nebeneinander, ohne Linien; der Text bleibt Fliesstext. `<br><br>` beginnt einen neuen Absatz. Ein Bild mit `title` erhält seine Bildunterschrift. {{ uuid('e92fbe40-413b-419e-b8d6-a0d5133fc019') }}

{% call table('8.5cm', '7.5cm', type='layout', uuid='5592679b-0980-4e77-9314-547686e76b2d') %}
| Das Diagramm rechts zeigt Monatswerte als Balken, die Linie darüber ihren Verlauf.<br><br>In einer Layouttabelle steht das Bild neben dem Text, der es beschreibt, statt darunter. So bleibt die Seite ruhig, und Lernende sehen Text und Bild zugleich. | {{ image('images/diagramm.svg', width='7cm', title='Monatswerte als Balkendiagramm', uuid='78e8600a-74fa-4f07-afb4-54df4ced58e7') }} |
{% endcall %}

{% raw %}
```markdown
{% call table('8.5cm', '7.5cm', type='layout') %}
| Das Diagramm rechts …<br><br>In einer Layouttabelle … | {{ image('images/diagramm.svg', width='7cm', title='Monatswerte als Balkendiagramm') }} |
{% endcall %}
```
{% endraw %}

## Inhalte in Zellen kennzeichnen {{ uuid('1a745468-ecb5-4e83-a7f0-abd60da0b41e') }}

`content()` gibt einem Teil einer Zelle einen Identifikator, so wie `uuid()` einem Absatz; eine Zelle kann mehrere enthalten: {{ uuid('c4c4745f-3d05-4241-89f3-261ed6b030b4') }}

{{ table('4cm', '*', uuid='205d1220-a40f-41ad-ac96-25852f14f98b') }}
| Bauteil | Prüfung |
| --- | --- |
| Flansch | {% call content(uuid='d4bc4cef-25be-4e21-854b-a6bc4461aa47') %}Sichtprüfung vor der Montage{% endcall %}<br>{% call content(uuid='a62024f9-0f59-409f-8aa5-e3d8f38e9da8') %}- Lochkreis messen{% endcall %}<br>{% call content(uuid='a6bf6cb2-ca71-4aed-9905-bdd636610794') %}- Dichtfläche reinigen{% endcall %} |

{% raw %}
```markdown
| Flansch | {% call content(uuid='d4bc4cef-…') %}Sichtprüfung vor der Montage{% endcall %}<br>{% call content(uuid='a62024f9-…') %}- Lochkreis messen{% endcall %} |
```
{% endraw %}
