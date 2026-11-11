# Didaktische Elemente {{ anchor('kap_didaktik') }}

Lehrmittel gliedern den Stoff mit wiederkehrenden Elementen: Lernziele am Anfang, Hinweise und Beispiele im Text, Aufgaben mit Lösungen und eine Selbstkontrolle am Ende. Jedes Element hat seine Formatvorlage in der Vorlage textbook_2026_V02.

## Lernziele

Ein Etikett mit `label()` kündigt die Lernziele an; `learning_objectives()` macht die folgende Tabelle zur Lernzieltabelle, ein Lernziel pro Zeile. Die Nummer `LZ_…` wird ein Link auf das Lernziel; `link_lo()` nach der Nummer verknüpft es mit seinen Schlüsseln in der Datenbank futuremem, als Word-Kommentar auf der Nummer.

{{ label('Lernziele', icon='learning_objective') }}

{% call learning_objectives() %}
| LZ_0101 {{ link_lo('51620B64-F785-4D0C-B5B3-EEFF051576CA') }} | Sie schreiben ein Kapitel in Markdown mit Überschriften, Listen und Verweisen. |
| LZ_0102 {{ link_lo('E27A4E68-2441-44A1-9591-C228C4665F45', '3082EC75-46DA-4614-B452-1F4F9B1AD77A') }} | Sie setzen Bilder, Tabellen und Formeln mit den passenden Befehlen. |
| LZ_0103 | Sie gestalten Hinweise, Rahmen und Aufgaben mit den Formatvorlagen der Vorlage. |
{% endcall %}

Die Spaltenbreiten der Lernzieltabelle sind wählbar, hier in der Zeilenform direkt vor der Tabelle:

{{ learning_objectives('2.5cm', '13.5cm') }}
| LZ_0104 | Sie erstellen aus dem Markdown ein Word-Dokument und ein PDF. |

{% raw %}
```markdown
{{ label('Lernziele', icon='learning_objective') }}

{% call learning_objectives() %}
| LZ_0101 {{ link_lo('51620B64-F785-4D0C-B5B3-EEFF051576CA') }} | Sie schreiben ein Kapitel in Markdown … |
| LZ_0103 | Sie gestalten Hinweise, Rahmen und Aufgaben … |
{% endcall %}

{{ learning_objectives('2.5cm', '13.5cm') }}
| LZ_0104 | Sie erstellen aus dem Markdown ein Word-Dokument und ein PDF. |
```
{% endraw %}

## Etiketten

Ein Etikett zeigt ein Symbol und einen kurzen Text in einem grauen Kasten. Die Symbole liegen in `reference/template/icons/`: `learning_objective`, `bell`, `magnifying_glass`, `arrow_right` und `summary`. Mit `link` wird das Etikett ein Link.

{{ label('Beispiel', icon='magnifying_glass') }}

Ein Motor hebt eine Last mit der Masse {{ formula('m = 200\,\text{kg}') }} in {{ formula('t = 10\,\text{s}') }} um {{ formula('h = 5\,\text{m}') }}. Die Hubarbeit ist {{ formula('W = m \cdot g \cdot h \approx 9810\,\text{J}') }}, die Leistung {{ formula('P = W / t \approx 981\,\text{W}') }}.

{{ label('Zusammenfassung', icon='summary') }}

Etiketten, Hinweise und Rahmen gliedern eine Seite, ohne dass Sie selbst formatieren.

{{ label('Zur Spezifikation', icon='arrow_right', link='https://spec.commonmark.org/0.31.2/') }}

{% raw %}
```markdown
{{ label('Beispiel', icon='magnifying_glass') }}
{{ label('Zusammenfassung', icon='summary') }}
{{ label('Zur Spezifikation', icon='arrow_right', link='https://spec.commonmark.org/0.31.2/') }}
```
{% endraw %}

## Hinweise

`note()` direkt vor einem Absatz oder einer Liste setzt ihn in die Formatvorlage Note, einen hellblauen Kasten; aufeinanderfolgende Hinweise bilden einen Kasten. Das Etikett darüber ragt mit `offset_y='50%'` halb in den Kasten, `offset_x` rückt es an den Text.

{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}

{{ note() }}
Prüfen Sie vor dem Rendern, ob jede Bilddatei im Ordner `images` liegt.

{{ note() }}
- fehlende Datei: ein Problem mit Datei und Zeile
- noch kein Bild: ein Platzhalter in doppelten runden Klammern

Mehrere Blöcke in einem Kasten umschliessen Sie mit `{% raw %}{% call note() %}{% endraw %}`, auch mit einer Formel:

{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}

{% call note() %}
Sicherheit steht an oberster Stelle.

- Anlage spannungsfrei schalten
- gegen Wiedereinschalten sichern

{{ formula('U = R \cdot I') }}
{% endcall %}

{% raw %}
```markdown
{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}

{{ note() }}
Prüfen Sie vor dem Rendern, ob jede Bilddatei im Ordner `images/` liegt.

{% call note() %}
Sicherheit steht an oberster Stelle.

- Anlage spannungsfrei schalten

{{ formula('U = R \cdot I') }}
{% endcall %}
```
{% endraw %}

## Rahmen

`frame()` setzt den folgenden Absatz oder die folgende Liste in einen Kasten mit farbiger Linie, etwa eine Definition. Farbe, Hintergrund und Linienstärke sind wählbar.

{{ frame() }}
**Manifest:** die Datei `_main_.md`, die die Teile des Dokuments in ihrer Reihenfolge aufzählt.

{{ frame(color='#FFC000', background='#FFF8E1', thickness='2pt') }}
**Befehl:** ein Aufruf in doppelten geschweiften Klammern, den das Rendern prüft.

{% call frame(color='#00B050') %}
Ein Rahmen kann mehrere Blöcke enthalten:

1. einen Absatz
2. eine Liste

{{ formula('P = \frac{W}{t}', align='center') }}
{% endcall %}

{% raw %}
```markdown
{{ frame() }}
**Manifest:** die Datei `_main_.md`, …

{{ frame(color='#FFC000', background='#FFF8E1', thickness='2pt') }}
**Befehl:** ein Aufruf in doppelten geschweiften Klammern, …

{% call frame(color='#00B050') %}
Ein Rahmen kann mehrere Blöcke enthalten:
1. einen Absatz
{{ formula('P = \frac{W}{t}', align='center') }}
{% endcall %}
```
{% endraw %}

## Aufgaben und Lösungen

Aufgaben, Lösungen und weitere Kästen schreiben Sie als Markdown-Zitat mit einer Kennung in eckigen Klammern; der Text nach der Kennung ist der Titel.

> [!AUFGABE] Aufgabe 1: Hubleistung
> Ein Kran hebt eine Palette von 500 kg in 20 s um 8 m. Berechnen Sie die Leistung.

> [!LOESUNG] Lösung
> {{ formula('P = \frac{m \cdot g \cdot h}{t} = \frac{500\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot 8\,\text{m}}{20\,\text{s}} \approx 1{,}96\,\text{kW}') }}

> [!HINWEIS] Einheiten prüfen
> Rechnen Sie immer mit Einheiten; ein Fehler fällt dann sofort auf.

> [!SELBSTKONTROLLE] Quiz zu Kapitel 5

> [!KOMMENTAR] Notiz an das Lektorat
> Die Aufgabe ist neu und noch nicht geprüft.

{% raw %}
```markdown
> [!AUFGABE] Aufgabe 1: Hubleistung
> Ein Kran hebt eine Palette von 500 kg in 20 s um 8 m. Berechnen Sie die Leistung.

> [!LOESUNG] Lösung
> {{ formula('P = \frac{m \cdot g \cdot h}{t} = … \approx 1{,}96\,\text{kW}') }}

> [!HINWEIS] Einheiten prüfen
> Rechnen Sie immer mit Einheiten; ein Fehler fällt dann sofort auf.

> [!SELBSTKONTROLLE] Quiz zu Kapitel 5

> [!KOMMENTAR] Notiz an das Lektorat
> Die Aufgabe ist neu und noch nicht geprüft.
```
{% endraw %}

## Selbstkontrolle

Am Ende eines Kapitels führt ein Etikett mit Link zur Selbstkontrolle, darunter ihr QR-Code für das gedruckte Buch:

{{ label('Selbstkontrolle', icon='arrow_right', link='https://example.org/selbstkontrolle/kapitel-5') }}

{{ qr_code('https://example.org/selbstkontrolle/kapitel-5') }}

{% raw %}
```markdown
{{ label('Selbstkontrolle', icon='arrow_right', link='https://example.org/selbstkontrolle/kapitel-5') }}

{{ qr_code('https://example.org/selbstkontrolle/kapitel-5') }}
```
{% endraw %}
