# Didaktische Elemente {{ anchor('kap_didaktik', uuid='5f6a45b5-fc13-4b38-b48a-dfdbe12c4f2d') }} {{ uuid('316e17d1-4169-4a68-8346-37f2f8ee036d') }}

Lehrmittel gliedern den Stoff mit wiederkehrenden Elementen: Lernziele am Anfang, Hinweise und Beispiele im Text, Aufgaben mit Lösungen und eine Selbstkontrolle am Ende. Jedes Element hat seine Formatvorlage in der Vorlage textbook_2026_V02. {{ uuid('c83c1ec8-3671-4436-a09b-1dfd5f6a9cbe') }}

## Lernziele {{ uuid('be7a98ba-dfcf-495e-8c6b-025b8cb3c241') }}

Ein Etikett mit `label()` kündigt die Lernziele an; `learning_objectives()` macht die folgende Tabelle zur Lernzieltabelle, ein Lernziel pro Zeile. Die Nummer `LZ_…` wird ein Link auf das Lernziel; `link_lo()` nach der Nummer verknüpft es mit seinen Schlüsseln in der Datenbank futuremem, als Word-Kommentar auf der Nummer. {{ uuid('ae1ed606-3ed5-4400-877a-1391e5aa8ef5') }}

{{ label('Lernziele', icon='learning_objective', uuid='6f320a07-2cad-4197-8e72-e3ba189e8682') }}

{% call learning_objectives(uuid='57b16eda-2ffe-41a3-9aea-47ae8b00780a') %}
| LZ_0101 {{ link_lo('51620B64-F785-4D0C-B5B3-EEFF051576CA', uuid='ef2f9699-94c4-4ebd-b7a3-8b6e5c6448e9') }} | Sie schreiben ein Kapitel in Markdown mit Überschriften, Listen und Verweisen. |
| LZ_0102 {{ link_lo('E27A4E68-2441-44A1-9591-C228C4665F45', '3082EC75-46DA-4614-B452-1F4F9B1AD77A', uuid='423a26fd-23f2-4817-9143-0917fb40388b') }} | Sie setzen Bilder, Tabellen und Formeln mit den passenden Befehlen. |
| LZ_0103 | Sie gestalten Hinweise, Rahmen und Aufgaben mit den Formatvorlagen der Vorlage. |
{% endcall %}

Die Spaltenbreiten der Lernzieltabelle sind wählbar, hier in der Zeilenform direkt vor der Tabelle: {{ uuid('ba3c9acb-77d6-459c-ac70-ba2c0d173b3d') }}

{{ learning_objectives('2.5cm', '13.5cm', uuid='167793f3-5402-465b-9292-6e38dfa13fda') }}
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

## Etiketten {{ uuid('1e8b0911-d907-45f8-a68d-ccba0e335680') }}

Ein Etikett zeigt ein Symbol und einen kurzen Text in einem grauen Kasten. Die Symbole liegen in `reference/template/icons/`: `learning_objective`, `bell`, `magnifying_glass`, `arrow_right` und `summary`. Mit `link` wird das Etikett ein Link. {{ uuid('569fa2f1-2980-4f2c-89e6-69e0aaffbd37') }}

{{ label('Beispiel', icon='magnifying_glass', uuid='b06a2a1f-3704-426a-bdbb-fe748854da12') }}

Ein Motor hebt eine Last mit der Masse {{ formula('m = 200\,\text{kg}', uuid='91c05ca1-e0af-4687-826b-89924d9125d6') }} in {{ formula('t = 10\,\text{s}', uuid='ca445e24-0aaf-4430-a266-80671fea6939') }} um {{ formula('h = 5\,\text{m}', uuid='22b4d99b-ed6a-4679-be39-d276034e9cf9') }}. Die Hubarbeit ist {{ formula('W = m \cdot g \cdot h \approx 9810\,\text{J}', uuid='60ec0f72-cb21-4902-a1e0-c7d23e15ac3f') }}, die Leistung {{ formula('P = W / t \approx 981\,\text{W}', uuid='a4584bbc-f4f2-43b3-ad03-8f54793f9630') }}. {{ uuid('07603803-e025-403e-8a8e-3d18527cce31') }}

{{ label('Zusammenfassung', icon='summary', uuid='ee4299f9-308a-4601-ab61-3076b9bd4684') }}

Etiketten, Hinweise und Rahmen gliedern eine Seite, ohne dass Sie selbst formatieren. {{ uuid('b705a226-f98a-4212-a30c-25934c1448ae') }}

{{ label('Zur Spezifikation', icon='arrow_right', link='https://spec.commonmark.org/0.31.2/', uuid='aee6dc7c-7400-4679-bd4f-bb380876f50f') }}

{% raw %}
```markdown
{{ label('Beispiel', icon='magnifying_glass') }}
{{ label('Zusammenfassung', icon='summary') }}
{{ label('Zur Spezifikation', icon='arrow_right', link='https://spec.commonmark.org/0.31.2/') }}
```
{% endraw %}

## Hinweise {{ uuid('3a7b0da9-03fc-4a7c-bd41-d89c4c656993') }}

`note()` direkt vor einem Absatz oder einer Liste setzt ihn in die Formatvorlage Note, einen hellblauen Kasten; aufeinanderfolgende Hinweise bilden einen Kasten. Das Etikett darüber ragt mit `offset_y='50%'` halb in den Kasten, `offset_x` rückt es an den Text. {{ uuid('2a3154d2-4193-4a27-bd38-a388eff5dad0') }}

{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%', uuid='bdcf40ca-b06a-4fe4-82f9-d536eb58edbf') }}

{{ note(uuid='6c4eb542-c124-49ec-adec-eece3ed8220d') }}
Prüfen Sie vor dem Rendern, ob jede Bilddatei im Ordner `images` liegt.

{{ note(uuid='973f8b69-e188-4c5f-a2b9-52a21b4d5e0a') }}
- fehlende Datei: ein Problem mit Datei und Zeile
- noch kein Bild: ein Platzhalter in doppelten runden Klammern

Mehrere Blöcke in einem Kasten umschliessen Sie mit `{% raw %}{% call note() %}{% endraw %}`, auch mit einer Formel: {{ uuid('ff68e399-c85e-4808-8415-b7c9139c759f') }}

{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%', uuid='0f828ed2-fb1f-4045-8797-363da119734d') }}

{% call note(uuid='ad1dcd9f-fc12-4c56-a00b-0e96d1a38af5') %}
Sicherheit steht an oberster Stelle.

- Anlage spannungsfrei schalten
- gegen Wiedereinschalten sichern

{{ formula('U = R \cdot I', uuid='9b408f2a-fc10-4c68-89b5-92b21e3947c1') }}
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

## Rahmen {{ uuid('c3ca7534-bbb8-4d5c-8361-e37363156a2c') }}

`frame()` setzt den folgenden Absatz oder die folgende Liste in einen Kasten mit farbiger Linie, etwa eine Definition. Farbe, Hintergrund und Linienstärke sind wählbar. {{ uuid('16f56662-9a5d-4164-9242-49f51ebe2876') }}

{{ frame(uuid='b7b6a49b-9f5c-4dcb-80fd-6b0be0c502c4') }}
**Manifest:** die Datei `_main_.md`, die die Teile des Dokuments in ihrer Reihenfolge aufzählt.

{{ frame(color='#FFC000', background='#FFF8E1', thickness='2pt', uuid='6c767397-7878-4ecc-9b6c-58d0bab05cec') }}
**Befehl:** ein Aufruf in doppelten geschweiften Klammern, den das Rendern prüft.

{% call frame(color='#00B050', uuid='a484f7dd-5c62-45ac-acf2-4aa59eef2572') %}
Ein Rahmen kann mehrere Blöcke enthalten:

1. einen Absatz
2. eine Liste

{{ formula('P = \frac{W}{t}', align='center', uuid='1a8ee47e-d7ae-43b9-bed7-9b10b9214741') }}
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

## Aufgaben und Lösungen {{ uuid('edb40c91-5698-4e3d-bed6-dd9388e61480') }}

Aufgaben, Lösungen und weitere Kästen schreiben Sie als Markdown-Zitat mit einer Kennung in eckigen Klammern; der Text nach der Kennung ist der Titel. {{ uuid('67725406-c7d7-449f-84bb-4a13d642477a') }}

> [!AUFGABE] Aufgabe 1: Hubleistung
> Ein Kran hebt eine Palette von 500 kg in 20 s um 8 m. Berechnen Sie die Leistung.

> [!LOESUNG] Lösung
> {{ formula('P = \frac{m \cdot g \cdot h}{t} = \frac{500\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot 8\,\text{m}}{20\,\text{s}} \approx 1{,}96\,\text{kW}', uuid='3b4f3591-855b-45d5-b892-c1e83a0fef7a') }}

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

## Selbstkontrolle {{ uuid('9d923240-7500-4843-9189-5315718023bf') }}

Am Ende eines Kapitels führt ein Etikett mit Link zur Selbstkontrolle, darunter ihr QR-Code für das gedruckte Buch: {{ uuid('97a7fdc0-1454-4b56-a2e6-2e8c9d5838ed') }}

{{ label('Selbstkontrolle', icon='arrow_right', link='https://example.org/selbstkontrolle/kapitel-5', uuid='d70cc121-ca18-409b-ae7a-44a0f21616f4') }}

{{ qr_code('https://example.org/selbstkontrolle/kapitel-5', uuid='c409ac38-d627-4b22-a6a4-00dbad488dc2') }}

{% raw %}
```markdown
{{ label('Selbstkontrolle', icon='arrow_right', link='https://example.org/selbstkontrolle/kapitel-5') }}

{{ qr_code('https://example.org/selbstkontrolle/kapitel-5') }}
```
{% endraw %}
