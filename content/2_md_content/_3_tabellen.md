# Tabellen {{ anchor('tabellen', uuid='d90e0923-33d6-4570-9337-28c7fcf73b1b') }} {{ uuid('6e4db1f3-8798-4e71-9854-fae642775811') }}

Eine Tabelle schreiben Sie als Pipe-Tabelle, eine Zeile pro Tabellenzeile, oder als HTML-Tabelle, wenn Zellen über mehrere Zeilen oder Spalten reichen. Eine Zeile Tabelle: Titel direkt davor wird die nummerierte Tabellenüberschrift, die das Tabellenverzeichnis aufführt. table() davor legt die Spaltenbreiten fest. {{ uuid('b7574aa8-6800-4e9a-87ae-1ace22e84536') }}

## Einfache Tabelle {{ uuid('d5540511-bf55-458b-b006-d625becacf03') }}

Die Trennzeile | --- | macht die erste Zeile zur Kopfzeile, die auf jeder Seite wiederholt wird. Ohne table() teilen sich die Spalten die Textspalte gleichmässig. {{ uuid('28355bdb-d71d-4f8a-aa6a-4a4878d9df38') }}

{% call table('8.0cm', '8.0cm', uuid='6ef7f852-f1f3-4453-b45e-2a1d58e36fd0') %}
Tabelle: Dateien eines Dokuments
<table>
  <thead>
    <tr>
      <th>Datei</th>
      <th>Inhalt</th>
    </tr>
  </thead>
  <tr>
    <td>\_main\_.md</td>
    <td>das Manifest: Titelseite, Kapitel und Verzeichnisse</td>
  </tr>
  <tr>
    <td>cover.md</td>
    <td>die Zeilen im Farbband der Titelseite</td>
  </tr>
  <tr>
    <td>\_1_text_und_struktur.md</td>
    <td>ein Kapitel</td>
  </tr>
  <tr>
    <td>images/</td>
    <td>die Bilder der Kapitel</td>
  </tr>
</table>
{% endcall %}

Tabelle: Dateien eines Dokuments<br>| Datei | Inhalt |<br>| --- | --- |<br>| \_main\_.md | das Manifest: Titelseite, Kapitel und Verzeichnisse | {{ uuid('095ea144-d2fb-4fd1-98ee-6f6aa89f7686') }}

## Spaltenbreiten und Verweis {{ uuid('5ef4ecfa-eed5-4ffb-a75b-971842e8f037') }}

Eine Breite pro Spalte, in cm, mm, pt oder Prozent; die Spalten mit \* teilen sich den Rest. anchor macht die Tabelle zum Ziel eines Verweises: {{ ref('si_basiseinheiten', uuid='d7ac728b-0683-4abc-93ab-35bba7158be4') }} nennt die sieben Basiseinheiten des Internationalen Einheitensystems {{ cite('iso80000', uuid='84f9958d-8d35-41bb-bf6b-514ebe5ac6cb') }}. {{ uuid('7f741554-b803-462b-ac5a-07ac33c4b2ce') }}

{% call table('5.5cm', '3.0cm', '7.5cm', anchor='si_basiseinheiten', uuid='d43b8b45-7b50-4b71-8c6a-1c35ec0f1be5') %}
Tabelle: SI-Basiseinheiten
<table>
  <thead>
    <tr>
      <th>Grösse</th>
      <th>Einheit</th>
      <th>Zeichen</th>
    </tr>
  </thead>
  <tr>
    <td>Länge</td>
    <td>Meter</td>
    <td>m</td>
  </tr>
  <tr>
    <td>Masse</td>
    <td>Kilogramm</td>
    <td>kg</td>
  </tr>
  <tr>
    <td>Zeit</td>
    <td>Sekunde</td>
    <td>s</td>
  </tr>
  <tr>
    <td>elektrische Stromstärke</td>
    <td>Ampere</td>
    <td>A</td>
  </tr>
  <tr>
    <td>thermodynamische Temperatur</td>
    <td>Kelvin</td>
    <td>K</td>
  </tr>
  <tr>
    <td>Stoffmenge</td>
    <td>Mol</td>
    <td>mol</td>
  </tr>
  <tr>
    <td>Lichtstärke</td>
    <td>Candela</td>
    <td>cd</td>
  </tr>
</table>
{% endcall %}

{% raw %}{% call table('5.5cm', '3cm', '\*', anchor='tab_einheiten') %}{% endraw %}<br>Tabelle: SI-Basiseinheiten<br>| Grösse | Einheit | Zeichen |<br>| --- | --- | --- |<br>| Länge | Meter | m |<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('085e560a-b1dd-4219-b193-d01c5634714d') }}

## Ohne Kopfzeile, ohne Nummer {{ uuid('78da556d-bd33-4d57-a4e5-b63b3ac753e7') }}

Ohne Trennzeile ist jede Zeile eine normale Zeile. Hier steht table() als einzelne Zeile direkt vor der Tabelle; zwei feste Breiten unter 16 cm ergeben eine schmalere Tabelle: {{ uuid('582ea68f-eed8-4c5a-b752-9e85bec57ec7') }}

{% call table('4.0cm', '6.0cm', uuid='4ec677ef-7d45-4ca2-bb45-387d730ff738') %}
<table>
  <tr>
    <td>Format</td>
    <td>A4 hoch</td>
  </tr>
  <tr>
    <td>Textspalte</td>
    <td>16 cm</td>
  </tr>
  <tr>
    <td>Schrift</td>
    <td>Roboto</td>
  </tr>
</table>
{% endcall %}

Mit numbered=False steht nur der Titel über der Tabelle, ohne «Tabelle n:»: {{ uuid('ac6b0312-6428-4d1e-a470-711efdb92500') }}

{% call table('4.0cm', '12.0cm', uuid='fa98c623-c90f-4ef8-ba19-b1e63a8009de') %}
Tabelle: Seitenränder der Vorlage
<table>
  <tr>
    <td>oben</td>
    <td>35,2 mm</td>
  </tr>
  <tr>
    <td>unten</td>
    <td>23,7 mm</td>
  </tr>
</table>
{% endcall %}

{% raw %}{{ table('4cm', '6cm') }}{% endraw %}<br>| Format | A4 hoch |<br>| Textspalte | 16 cm |<br><br>{% raw %}{% call table('4cm', '\*', numbered=False) %}{% endraw %}<br>Tabelle: Seitenränder der Vorlage<br>| oben | 35,2 mm |<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('e9c188ee-4cca-4ef2-bb2a-2e90eed457e3') }}

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

## Bilder nebeneinander {{ uuid('96fc8f30-0512-4356-a454-6c73b13bbcd9') }}

type='pictures' setzt Bilder ohne Linien nebeneinander, unter jedem seine Beschriftung; die Tabelle bleibt auf einer Seite und hat keine Tabellennummer. {{ uuid('57c35e6f-05d1-4290-a1c4-5bf6bbefb74b') }}

{% call table('8.0cm', '8.0cm', type='pictures', uuid='3c996515-d79c-40e3-8d89-29125a0149ff') %}
<table>
  <tr>
    <td>{{ image('images/3_tabellen/04.png', width='7.5cm', alt_text=None, uuid='410d09c4-b42b-4b5e-ba73-78cfe3782865') }}</td>
    <td>{{ image('images/3_tabellen/05.png', width='7.5cm', alt_text=None, uuid='1e5fecab-07f3-42ab-81e1-ad472be7796c') }}</td>
  </tr>
  <tr>
    <td>Flansch<br>technische Zeichnung als PNG</td>
    <td>Monatswerte<br>Diagramm als SVG</td>
  </tr>
</table>
{% endcall %}

{% raw %}{% call table('8cm', '8cm', type='pictures') %}{% endraw %}<br>| {% raw %}{{ image('images/bauteil.png', width='7.5cm') }}{% endraw %} | {% raw %}{{ image('images/diagramm.svg', width='7.5cm') }}{% endraw %} |<br>| Flansch<br>technische Zeichnung als PNG | Monatswerte<br>Diagramm als SVG |<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('ee9abf2c-80cc-4a50-9a51-0e8b36dc5887') }}

## Text und Bild in Spalten {{ uuid('72cf48d0-cb5d-4294-a4db-3f01d17f21d1') }}

type='layout' stellt Text und Bilder in Spalten nebeneinander, ohne Linien; der Text bleibt Fliesstext. \<br>\<br> beginnt einen neuen Absatz. Ein Bild mit title erhält seine Bildunterschrift. {{ uuid('d14c8109-5af0-4989-acb1-3e923c541d1e') }}

{% call table('8.5cm', '7.5cm', type='layout', uuid='8491e27a-7d25-4008-af99-eb35b5f8b386') %}
<table>
  <tr>
    <td>Das Diagramm rechts zeigt Monatswerte als Balken, die Linie darüber ihren Verlauf.<br><br>In einer Layouttabelle steht das Bild neben dem Text, der es beschreibt, statt darunter. So bleibt die Seite ruhig, und Lernende sehen Text und Bild zugleich.</td>
    <td>{{ image('images/3_tabellen/06.png', width='7.0cm', title='Monatswerte als Balkendiagramm', alt_text=None, uuid='ec513978-c1ca-4deb-880d-e6dc42367fa3') }}</td>
  </tr>
</table>
{% endcall %}

{% raw %}{% call table('8.5cm', '7.5cm', type='layout') %}{% endraw %}<br>| Das Diagramm rechts …<br><br>In einer Layouttabelle … | {% raw %}{{ image('images/diagramm.svg', width='7cm', title='Monatswerte als Balkendiagramm') }}{% endraw %} |<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('992c7e3d-f7a5-4a02-8c69-cb74f1f9138f') }}

## Inhalte in Zellen kennzeichnen {{ uuid('7f86dc98-99f7-4e78-a775-25ec51fef7ec') }}

content() gibt einem Teil einer Zelle einen Identifikator, so wie uuid() einem Absatz; eine Zelle kann mehrere enthalten: {{ uuid('34695315-2eed-41d3-85df-0c1eb27fecd4') }}

{% call table('4.0cm', '12.0cm', uuid='9bb15f9f-6c4f-4869-821f-162b2f421eb7') %}
<table>
  <thead>
    <tr>
      <th>Bauteil</th>
      <th>Prüfung</th>
    </tr>
  </thead>
  <tr>
    <td>Flansch</td>
    <td>{% call content(uuid='d4bc4cef-25be-4e21-854b-a6bc4461aa47') %}Sichtprüfung vor der Montage{% endcall %}<br>{% call content(uuid='a62024f9-0f59-409f-8aa5-e3d8f38e9da8') %}- Lochkreis messen{% endcall %}<br>{% call content(uuid='a6bf6cb2-ca71-4aed-9905-bdd636610794') %}- Dichtfläche reinigen{% endcall %}</td>
  </tr>
</table>
{% endcall %}

| Flansch | {% raw %}{% call content(uuid='d4bc4cef-…') %}{% endraw %}Sichtprüfung vor der Montage{% raw %}{% endcall %}{% endraw %}<br>{% raw %}{% call content(uuid='a62024f9-…') %}{% endraw %}- Lochkreis messen{% raw %}{% endcall %}{% endraw %} |
