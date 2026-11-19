## Ein Kapitel in mehreren Dateien

Ab hier steht dieses Kapitel in eigenen Dateien, \_3\_1\_html\_tabellen.md und \_3\_2\_bilder\_in\_tabellen.md: Ein grosses Kapitel lässt sich so auf mehrere Dateien verteilen. Im Manifest steht jede mit subchapter() direkt nach ihrem Kapitel oder einem anderen subchapter(), im Ordner der Kapiteldatei. Das Rendern hängt sie in dieser Reihenfolge an ihr Kapitel an: Word zeigt ein einziges Kapitel, seine Abschnitte weiter nummeriert. Eine solche Datei hat keine Überschrift #, ihre Überschriften beginnen bei ##.

{% raw %}{{ document('Demo Starter', state='development') }}{% endraw %}<br>…<br>{% raw %}{{ chapter('_3_0_tabellen.md', image='images/3_tabellen/chapter_image.png') }}{% endraw %}<br>{% raw %}{{ subchapter('_3_1_html_tabellen.md') }}{% endraw %}<br>{% raw %}{# {{ subchapter('_3_2_bilder_in_tabellen.md') }} #}{% endraw %}

Solange das Dokument entsteht, steht im Manifest document(…, state='development'). Dann lassen sich Kapitel und ihre Teile auskommentieren wie oben, und erstellt wird nur, woran man gerade arbeitet; ein auskommentiertes Kapitel nimmt seine Teile mit. Verweise auf Ausgelassenes meldet das Rendern, das Dokument entsteht trotzdem, mit ?? an ihrer Stelle. Das fertige Dokument hat state='production', die Vorgabe: Dann bricht jeder Verweis ohne Ziel das Erstellen ab.

## HTML-Tabelle mit verbundenen Zellen {{ uuid('a5e89261-7d62-491c-89de-217258dcb059') }}

colspan verbindet Zellen nebeneinander, rowspan untereinander. Die Zeilen in <thead> sind Kopfzeilen. In einer Zelle stehen Text mit Markdown, Listen nach \<br>, Formeln und Bilder: {{ uuid('b1ed030e-a298-40cd-b654-b99be2f8017c') }}

{% call table('2.4cm', '2.4cm', '2.4cm', '8.8cm', anchor='bildformate_im_vergleich', uuid='3be00c64-c180-4390-b735-ce12f7930002') %}
Tabelle: Bildformate im Vergleich
<table>
  <thead>
    <tr>
      <th rowspan="2">Format</th>
      <th colspan="2">Eigenschaften</th>
      <th rowspan="2">Geeignet für</th>
    </tr>
    <tr>
      <th>Vektor</th>
      <th>Transparenz</th>
    </tr>
  </thead>
  <tr>
    <td>**SVG**</td>
    <td>ja</td>
    <td>ja</td>
    <td>Geeignet für:<br>- Diagramme<br>- technische Zeichnungen<br>{{ image('images/3_tabellen/01.png', width='5.0cm', alt_text=None, uuid='c6869d52-c13e-4026-b5c0-e157baa408e1') }}</td>
  </tr>
  <tr>
    <td>**PNG**</td>
    <td>nein</td>
    <td>ja</td>
    <td>Bildschirmfotos und Raster mit mindestens 150 dpi, also {{ formula('\frac{1800\text{ px}}{300\text{ dpi}} = 6\text{ in}', uuid='9125d493-013c-47d9-9086-285c74372a22') }}</td>
  </tr>
  <tr>
    <td>**JPG**</td>
    <td colspan="2">*weder noch*</td>
    <td>Fotos</td>
  </tr>
</table>
{% endcall %}

{% raw %}{% call table('2.4cm', '2.4cm', '2.4cm', '\*', anchor='tab_bildformate') %}{% endraw %}<br>Tabelle: Bildformate im Vergleich<br><table><br> <thead><br> <tr><th rowspan="2">Format</th><th colspan="2">Eigenschaften</th><th rowspan="2">Geeignet für</th></tr><br> <tr><th>Vektor</th><th>Transparenz</th></tr><br> </thead><br> <tbody><br> <tr><td><strong>SVG</strong></td><td>ja</td><td>ja</td><br> <td>Geeignet für:<br>- Diagramme<br>{% raw %}{{ image('images/workflow.svg', width='5cm') }}{% endraw %}</td></tr><br> <tr><td><strong>JPG</strong></td><td colspan="2"><em>weder noch</em></td><td>Fotos</td></tr><br> </tbody><br></table><br>{% raw %}{% endcall %}{% endraw %} {{ uuid('4a41707c-63a9-4b21-b411-bd9e9e1de009') }}

#### Ausrichtung, gedrehter Text und Lösungen in Zellen {{ uuid('18c02dcd-c5ad-4272-9ebc-20a65260a8c5') }}

Die Ausrichtung in der Zelle und gedrehter Text bleiben erhalten; die erste Zeile ist eine Kopfzeile: {{ uuid('3c32ffe3-7056-47b9-97de-2421057c7440') }}

{% call table('1.5cm', '5.0cm', '5.0cm', '4.5cm', uuid='f6960dcb-0c11-43d5-a27d-4e0a804deff9') %}
<table>
  <thead>
    <tr>
      <th></th>
      <th>Links, oben</th>
      <th align="center">Zentriert, Mitte</th>
      <th align="right">Rechts, unten</th>
    </tr>
  </thead>
  <tr>
    <td vertical="up" align="center">Werte</td>
    <td>Zeile 1<br>Zeile 2<br>Zeile 3</td>
    <td align="center" valign="middle">Mitte</td>
    <td align="right" valign="bottom">unten</td>
  </tr>
</table>
{% endcall %}

Eine Zelle in der Formatvorlage Solutions ist eine Lösung, z. B. das Kreuz einer Selbstkontrolle: {{ uuid('953d6b42-6b83-4cb2-8b1b-7f16adcfcc85') }}

{% call table('1.5cm', '14.5cm', uuid='d95561fb-6e17-4c28-900a-9c1a1cad80c9') %}
<table>
  <tr>
    <td align="center" solution>X</td>
    <td>Freiformflächen sind stetig gekrümmt.</td>
  </tr>
  <tr>
    <td align="center">□</td>
    <td>Freiformflächen sind immer eben.</td>
  </tr>
</table>
{% endcall %}

#### Auswahlliste mit gedrehter Kopfzeile {{ uuid('b6a97f9d-b48b-42c5-b22c-978200dee582') }}

Eine Kopfzeile nur aus gedrehten Zellen hat eine Zeilenhöhe «Mindestens» (Tabelleneigenschaften › Zeile), so hoch wie ihr längster Text; verbundene Zellen, Bilder und farbige Zeichen in den Zellen bleiben erhalten: {{ uuid('5fbc90ab-8645-44eb-a9fc-4549444cd97e') }}

{% call table('4.6cm', '0.9cm', '0.9cm', '0.9cm', '0.9cm', '0.9cm', '4.9cm', '2.0cm', uuid='65c87efc-f523-4be9-a9db-52b82c598f27') %}
<table>
  <thead>
    <tr>
      <th colspan="8">Auswahlliste</th>
    </tr>
    <tr>
      <th rowspan="3" valign="middle">Variante</th>
      <th colspan="6">Analyse und Beurteilung<br>\+ ja<br>\- nein<br>? fehlende Informationen<br>! Anforderungen abklären</th>
      <th rowspan="3" vertical="up" valign="bottom">Entscheidung</th>
    </tr>
    <tr height="2.3cm">
      <th vertical="up" valign="bottom">Kriterium 1</th>
      <th vertical="up" valign="bottom">Kriterium 2</th>
      <th vertical="up" valign="bottom">Kriterium 3</th>
      <th vertical="up" valign="bottom">Kriterium 4</th>
      <th vertical="up" valign="bottom">Kriterium 5</th>
      <th rowspan="2" vertical="up" valign="bottom">Bemerkungen</th>
    </tr>
    <tr height="4.8cm">
      <th vertical="up" valign="bottom">Sicheres Spannen</th>
      <th vertical="up" valign="bottom">Einfaches Einrichten</th>
      <th vertical="up" valign="bottom">Einfaches Bedienen</th>
      <th vertical="up" valign="bottom">Genauigkeit der Aufspannung</th>
      <th vertical="up" valign="bottom">Herstellkosten</th>
    </tr>
  </thead>
  <tr>
    <td>Variante 1<br>{{ image('images/3_tabellen/02.png', width='4.2cm', alt_text=None, uuid='ab01cb99-069b-4910-9b29-7e32550f98ca') }}</td>
    <td align="center" valign="middle">?</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">?</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">+</td>
    <td valign="middle">Zeitintensive Spannung mit mehreren Werkzeugen<br>Gabelschlüssel, Innensechskantschlüssel</td>
    <td align="center" valign="middle">{{ color('✗', uuid='1c6517c9-ef0e-4741-95b5-723b20289830') }}</td>
  </tr>
  <tr>
    <td>Variante 2<br>{{ image('images/3_tabellen/03.png', width='4.2cm', alt_text=None, uuid='4bc7850d-a564-415f-89c5-8e7fc4b59316') }}</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">+</td>
    <td align="center" valign="middle">!</td>
    <td align="center" valign="middle">+</td>
    <td valign="middle">Spannt schnell mit einem einzigen Werkzeug</td>
    <td align="center" valign="middle">{{ color('✓', '#00B050', uuid='8cd42d0b-da5b-441f-bbc4-3d371c8961b7') }}</td>
  </tr>
</table>
{% endcall %}
