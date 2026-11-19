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
