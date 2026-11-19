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
