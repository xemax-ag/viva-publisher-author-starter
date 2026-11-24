## Ein Kapitel in mehreren Dateien

Ab hier steht dieses Kapitel in eigenen Dateien, `_3_1_html_tabellen.md` und `_3_2_bilder_in_tabellen.md`: Ein grosses Kapitel lässt sich so auf mehrere Dateien verteilen. Im Manifest steht jede mit `subchapter()` direkt nach ihrem Kapitel oder einem anderen `subchapter()`, im Ordner der Kapiteldatei. Das Rendern hängt sie in dieser Reihenfolge an ihr Kapitel an: Word zeigt ein einziges Kapitel, seine Abschnitte weiter nummeriert. Eine solche Datei hat keine Überschrift `#`, ihre Überschriften beginnen bei `##`.

{% raw %}
```markdown
{{ document('Demo Starter', state='development') }}
…
{{ chapter('_3_0_tabellen.md', image='images/kapitel_3.svg') }}
{{ subchapter('_3_1_html_tabellen.md') }}
{# {{ subchapter('_3_2_bilder_in_tabellen.md') }} #}
```
{% endraw %}

Solange das Dokument entsteht, steht im Manifest `document(…, state='development')`. Dann lassen sich Kapitel und ihre Teile auskommentieren wie oben, ebenso Glossar, Quellenverzeichnis und Stichwortverzeichnis, und erstellt wird nur, woran man gerade arbeitet; ein auskommentiertes Kapitel nimmt seine Teile mit. Verweise auf Ausgelassenes meldet das Rendern, das Dokument entsteht trotzdem: Ein `ref()` ohne seinen Anker zeigt ??, ein `cite()` ohne `bibliography()` oder ohne Eintrag [?]; ohne `keyword_index()` fehlt das Stichwortverzeichnis, und ist `glossar()` auskommentiert, das Glossar mit den Verweisen auf seine Begriffe. Das fertige Dokument hat `state='production'`, die Vorgabe: Dann bricht jeder dieser Verweise ohne Ziel das Erstellen ab.

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

{{ page_break() }}

## Auswahlliste mit gedrehter Kopfzeile

Eine Zeile nur aus gedrehten Zellen braucht eine Höhe: `height` auf ihrem `<tr>` macht sie mindestens so hoch (in Word die Zeilenhöhe «Mindestens»), so hoch wie ihr längster Text; ohne sie lässt LibreOffice die Zeile im PDF weg. Eine Zeile einer Zelle, die mit `+ `, `- ` oder `* ` beginnt, wird ein Aufzählungspunkt; `\+` und `\-` lassen sie Text:

{% call table('4.6cm', '0.9cm', '0.9cm', '0.9cm', '0.9cm', '0.9cm', '4.9cm', '2cm') %}
<table>
  <thead>
    <tr>
      <th colspan="8">Auswahlliste</th>
    </tr>
    <tr>
      <th rowspan="3" valign="middle">Variante</th>
      <th colspan="6">Analyse und Beurteilung<p>\+ ja<p>\- nein<p>? fehlende Informationen<p>! Anforderungen abklären</th>
      <th rowspan="3" vertical valign="bottom">Entscheidung</th>
    </tr>
    <tr height="2.3cm">
      <th vertical valign="bottom">Kriterium 1</th>
      <th vertical valign="bottom">Kriterium 2</th>
      <th vertical valign="bottom">Kriterium 3</th>
      <th vertical valign="bottom">Kriterium 4</th>
      <th vertical valign="bottom">Kriterium 5</th>
      <th rowspan="2" vertical valign="bottom">Bemerkungen</th>
    </tr>
    <tr height="4.8cm">
      <th vertical valign="bottom">Sicheres Spannen</th>
      <th vertical valign="bottom">Einfaches Einrichten</th>
      <th vertical valign="bottom">Einfaches Bedienen</th>
      <th vertical valign="bottom">Genauigkeit der Aufspannung</th>
      <th vertical valign="bottom">Herstellkosten</th>
    </tr>
  </thead>
  <tr>
    <td>Variante 1<br>{{ image('images/bauteil.png', width='4.2cm') }}</td>
    <td align="center" valign="middle">?</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">?</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">+</td>
    <td valign="middle">Zeitintensive Spannung mit mehreren Werkzeugen<p>Gabelschlüssel, Innensechskantschlüssel</td>
    <td align="center" valign="middle">{{ color('✗') }}</td>
  </tr>
  <tr>
    <td>Variante 2<br>{{ image('images/bauteil.png', width='4.2cm') }}</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">!</td>
    <td align="center" valign="middle">+</td>
    <td valign="middle">Spannt schnell mit einem einzigen Werkzeug</td>
    <td align="center" valign="middle">{{ color('✓', '#00B050') }}</td>
  </tr>
</table>
{% endcall %}

{% raw %}
```markdown
<tr height="4.8cm">
  <th vertical valign="bottom">Sicheres Spannen</th>
  <th vertical valign="bottom">Genauigkeit der Aufspannung</th>
</tr>
<th colspan="6">Analyse und Beurteilung<p>\+ ja<p>\- nein<p>? fehlende Informationen</th>
<td align="center" valign="middle">{{ color('✗') }}</td>
```
{% endraw %}

## Farbige Zellen und Overlay

`bgcolor` auf `<td>` oder `<th>` gibt einer Zelle eine Hintergrundfarbe, `#RRGGBB` wie bei `color()`; in Word ist es die Schattierung der Zelle. `overlay` im Aufruf von `table()` legt ein Bild über die ganze Tabelle, etwa ein transparentes SVG mit den Lösungslinien einer Zuordnungsaufgabe: Seine linke obere Ecke ist die der Tabelle, es wird auf die Grösse der Tabelle gestreckt, und die Tabelle bleibt auf einer Seite.

{% call table('4.5cm', '3cm', '*', overlay='images/zuordnung.svg', overlay_width='16.00cm', overlay_height='2.77cm') %}
Tabelle: Zuordnung mit farbigen Zellen und Lösungslinien
<table>
  <thead>
    <tr><th>Begriff</th><th></th><th>Bedeutung</th></tr>
  </thead>
  <tr><td bgcolor="#E2F0D9">CAD</td><td></td><td bgcolor="#DDEBF7">Rechnergestützte Fertigung</td></tr>
  <tr><td bgcolor="#E2F0D9">CAM</td><td></td><td bgcolor="#DDEBF7">Produktdatenmanagement</td></tr>
  <tr><td bgcolor="#E2F0D9">PDM</td><td></td><td bgcolor="#DDEBF7">Rechnergestütztes Konstruieren</td></tr>
</table>
{% endcall %}

Ohne `overlay_height` misst der PDF-Schritt die Höhe der Tabelle; danach schreibt der Build `overlay_width` und `overlay_height` in den Aufruf, wie oben zu sehen, und nimmt sie beim nächsten Mal so. Beide lassen sich von Hand anpassen; ohne `overlay_height` wird wieder gemessen. Zeichnen Sie das SVG so breit und so hoch wie die Tabelle. Der Word-Import schreibt ein solches SVG aus den Linien, Kreisen und Rechtecken, die in Word über eine Tabelle gezeichnet sind.

{% raw %}
```markdown
{% call table('4.5cm', '3cm', '*', overlay='images/zuordnung.svg', overlay_width='16.00cm', overlay_height='2.77cm') %}
Tabelle: Zuordnung mit farbigen Zellen und Lösungslinien
<table>
  <tr><td bgcolor="#E2F0D9">CAD</td><td></td><td bgcolor="#DDEBF7">Rechnergestützte Fertigung</td></tr>
</table>
{% endcall %}
```
{% endraw %}
