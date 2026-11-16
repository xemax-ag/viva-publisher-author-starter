# Didaktische Elemente {{ anchor('didaktische_elemente', uuid='4302a9b7-ceeb-4322-b0e3-957f6df6c079') }} {{ uuid('4de41978-3af4-4790-8b37-2e1f896b2325') }}

Lehrmittel gliedern den Stoff mit wiederkehrenden Elementen: Lernziele am Anfang, Hinweise und Beispiele im Text, Aufgaben mit Lösungen und eine Selbstkontrolle am Ende. Jedes Element hat seine Formatvorlage in der Vorlage textbook_2026_V02. {{ uuid('d82d602e-b2fe-4320-a4dd-3e90355a9653') }}

## Lernziele {{ uuid('a9f6b338-a830-47ad-a51c-5832aca71318') }}

Ein Etikett mit label() kündigt die Lernziele an; learning_objectives() macht die folgende Tabelle zur Lernzieltabelle, ein Lernziel pro Zeile. Die Nummer LZ\_… wird ein Link auf das Lernziel; link_lo() nach der Nummer verknüpft es mit seinen Schlüsseln in der Datenbank futuremem, als Word-Kommentar auf der Nummer. {{ uuid('d946f25d-aa88-4a13-86d6-0b04832d383e') }}

{{ label('Lernziele', icon='learning_objective', uuid='54c79ea0-0eef-47e6-8b85-d673241c63e6') }}

{% call learning_objectives(uuid='7120b0e4-672f-41ee-9924-31ff5d56471e') %}
| LZ_0101 {{ link_lo('51620B64-F785-4D0C-B5B3-EEFF051576CA', uuid='163df6c8-a3d9-45b6-8667-2ea009987742') }} | Sie schreiben ein Kapitel in Markdown mit Überschriften, Listen und Verweisen. |
| LZ_0102 {{ link_lo('E27A4E68-2441-44A1-9591-C228C4665F45', '3082EC75-46DA-4614-B452-1F4F9B1AD77A', uuid='6d85a1db-7ea4-40ac-b7e8-b64298689a58') }} | Sie setzen Bilder, Tabellen und Formeln mit den passenden Befehlen. |
| LZ_0103 | Sie gestalten Hinweise, Rahmen und Aufgaben mit den Formatvorlagen der Vorlage. |
{% endcall %}

Die Spaltenbreiten der Lernzieltabelle sind wählbar, hier in der Zeilenform direkt vor der Tabelle: {{ uuid('0039e021-a80f-407a-8440-6a69e943d9ff') }}

{% call learning_objectives(uuid='6d7b33c7-9c68-49dc-88c4-8d1140a2381f') %}
| LZ_0104 | Sie erstellen aus dem Markdown ein Word-Dokument und ein PDF. |
{% endcall %}

{% raw %}{{ label('Lernziele', icon='learning_objective') }}{% endraw %}<br><br>{% raw %}{% call learning_objectives() %}{% endraw %}<br>| LZ_0101 {% raw %}{{ link_lo('51620B64-F785-4D0C-B5B3-EEFF051576CA') }}{% endraw %} | Sie schreiben ein Kapitel in Markdown … |<br>| LZ_0103 | Sie gestalten Hinweise, Rahmen und Aufgaben … |<br>{% raw %}{% endcall %}{% endraw %}<br><br>{% raw %}{{ learning_objectives('2.5cm', '13.5cm') }}{% endraw %}<br>| LZ_0104 | Sie erstellen aus dem Markdown ein Word-Dokument und ein PDF. | {{ uuid('1173d922-00b3-4d04-8954-80f374fe0fdf') }}

## Etiketten {{ uuid('e63a57c4-711b-4fe4-aafb-f6686b743fb2') }}

Ein Etikett zeigt ein Symbol und einen kurzen Text in einem grauen Kasten. Die Symbole liegen in reference/template/icons/: learning_objective, bell, magnifying_glass, arrow_right und summary. Mit link wird das Etikett ein Link. {{ uuid('d8fd9b66-b7a2-436f-b3c0-1b91ccbb0ffa') }}

{{ label('Beispiel', icon='magnifying_glass', uuid='31b2b845-3c58-45c9-a2a2-42fbc395be1e') }}

Ein Motor hebt eine Last mit der Masse {{ formula('m = 200\text{ kg}', uuid='fb305329-75a6-4214-9f92-a1585fee9b27') }} in {{ formula('t = 10\text{ s}', uuid='579f682c-f4ef-4c8f-a76c-ca31227f049c') }} um {{ formula('h = 5\text{ m}', uuid='ce3c1570-aa10-4d60-b0b5-54325f77a78f') }}. Die Hubarbeit ist {{ formula('W = m \cdot g \cdot h \approx 9810\text{ J}', uuid='fcfb5584-7bc8-432c-a1df-8007315116e3') }}, die Leistung {{ formula('P = W/t \approx 981\text{ W}', uuid='54ca0c80-7c50-4145-9f17-5b8558676308') }}. {{ uuid('1be84afe-ae4a-4918-837c-011c218f1766') }}

{{ label('Zusammenfassung', icon='summary', uuid='00d088da-4043-47af-bbf8-dd1eb551da1f') }}

Etiketten, Hinweise und Rahmen gliedern eine Seite, ohne dass Sie selbst formatieren. {{ uuid('759a62c7-b732-4439-9311-35b524d4a0bf') }}

{{ label('Zur Spezifikation', icon='arrow_right', link='https://spec.commonmark.org/0.31.2/', uuid='4e3eb0c5-05b7-49ca-83df-7f752d1a4a4f') }}

{% raw %}{{ label('Beispiel', icon='magnifying_glass') }}{% endraw %}<br>{% raw %}{{ label('Zusammenfassung', icon='summary') }}{% endraw %}<br>{% raw %}{{ label('Zur Spezifikation', icon='arrow_right', link='https://spec.commonmark.org/0.31.2/') }}{% endraw %} {{ uuid('7efb1b4b-e135-4f5e-a081-507b38a7659b') }}

## Hinweise {{ uuid('683717a4-341d-4d60-b2b8-3a595a3d42e4') }}

note() direkt vor einem Absatz oder einer Liste setzt ihn in die Formatvorlage Note, einen hellblauen Kasten; aufeinanderfolgende Hinweise bilden einen Kasten. Das Etikett darüber ragt mit offset_y='50%' halb in den Kasten, offset_x rückt es an den Text. {{ uuid('27c3e209-2cd6-41df-be6e-be1af519e1a2') }}

{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%', uuid='393fd3e0-e538-42b7-9a69-ac43c0590df2') }}

{% call note(uuid='86409677-02c0-46ac-8882-69df68478236') %}
Prüfen Sie vor dem Rendern, ob jede Bilddatei im Ordner images/ liegt.

- fehlende Datei: ein Problem mit Datei und Zeile
- noch kein Bild: ein Platzhalter in doppelten runden Klammern
{% endcall %}

Mehrere Blöcke in einem Kasten umschliessen Sie mit {% raw %}{% call note() %}{% endraw %}, auch mit einer Formel: {{ uuid('f0726795-9578-46f8-9751-7e15c9879f35') }}

{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%', uuid='079e024c-3099-47e0-92b0-0cceeed29bd1') }}

{% call note(uuid='1ba1efd3-b5b0-4ca4-8fc3-4ea5603d1401') %}
Sicherheit steht an oberster Stelle.

- Anlage spannungsfrei schalten
- gegen Wiedereinschalten sichern

{{ formula('U = R \cdot I', uuid='8c7f32f3-a3d5-4271-8717-1725279cacee') }}
{% endcall %}

{% raw %}{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%') }}{% endraw %}<br><br>{% raw %}{{ note() }}{% endraw %}<br>Prüfen Sie vor dem Rendern, ob jede Bilddatei im Ordner images/ liegt.<br><br>{% raw %}{% call note() %}{% endraw %}<br>Sicherheit steht an oberster Stelle.<br><br>- Anlage spannungsfrei schalten<br><br>{% raw %}{{ formula('U = R \cdot I') }}{% endraw %}<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('4d492038-d23b-47f4-ae65-5f4576444816') }}

Ein Etikett «Hinweis» kann auch über einem gewöhnlichen Absatz stehen, ohne Kasten: {{ uuid('f5ab7b82-873d-4df4-b005-3d67abc1ffc2') }}

{{ label('Hinweis', icon='bell', offset_x='4mm', uuid='641d4e8d-50a5-4553-bef7-1189e7c95fdc') }}

Wertelisten enthalten zusätzlich einen Platzhalter für «nicht zugeordnet». {{ uuid('e13f9f35-6e0b-459f-8ad3-7bcf603e2055') }}

## Rahmen {{ uuid('deedca2c-fdc2-4dd5-a890-0dc67c32f636') }}

frame() setzt den folgenden Absatz oder die folgende Liste in einen Kasten mit farbiger Linie, etwa eine Definition. Farbe, Hintergrund und Linienstärke sind wählbar. {{ uuid('9a18b0aa-7ac3-48a2-9bad-81dfe015e184') }}

{{ frame(uuid='7a74379a-2a12-4312-85cb-5016cd3784aa') }}
**Manifest****:** die Datei \_main\_.md, die die Teile des Dokuments in ihrer Reihenfolge aufzählt.

{{ frame(color='#FFC000', background='#FFF8E1', thickness='2pt', uuid='b806aaef-59f1-44c5-af03-74e7d21ebd99') }}
**Befehl:** ein Aufruf in doppelten geschweiften Klammern, den das Rendern prüft.

{% call frame(color='#00B050', uuid='945e51ad-efea-4f3c-bb7d-511d317bbe57') %}
Ein Rahmen kann mehrere Blöcke enthalten:

1. einen Absatz
2. eine Liste

{{ formula('P = \frac{W}{t}', align='center', uuid='36ab88c7-9b8f-48ac-a341-6e5139c7dc3e') }}
{% endcall %}

{% raw %}{{ frame() }}{% endraw %}<br>**Manifest:** die Datei \_main\_.md, …<br><br>{% raw %}{{ frame(color='#FFC000', background='#FFF8E1', thickness='2pt') }}{% endraw %}<br>**Befehl:** ein Aufruf in doppelten geschweiften Klammern, …<br><br>{% raw %}{% call frame(color='#00B050') %}{% endraw %}<br>Ein Rahmen kann mehrere Blöcke enthalten:<br>1. einen Absatz<br>{% raw %}{{ formula('P = \frac{W}{t}', align='center') }}{% endraw %}<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('5e3158d6-3cd4-4efe-98db-a6ee978f0e9c') }}

## Aufgaben und Lösungen {{ uuid('1d3bd13e-4257-40c6-98d1-f66d9b49b414') }}

Aufgaben, Lösungen und weitere Kästen schreiben Sie als Markdown-Zitat mit einer Kennung in eckigen Klammern; der Text nach der Kennung ist der Titel. {{ uuid('12f93e37-111a-4ba4-9612-26be7b8d3cd2') }}

> [!AUFGABE] Aufgabe 1: Hubleistung
> Ein Kran hebt eine Palette von 500 kg in 20 s um 8 m. Berechnen Sie die Leistung.

> [!LOESUNG]
> Lösung
>
> {{ formula('P = \frac{m \cdot g \cdot h}{t} = \frac{500\text{ kg} \cdot 9,81\text{ }\text{m/s}^{2} \cdot 8\text{ m}}{20\text{ s}} \approx 1,96\text{ kW}', uuid='2fb3a337-7d9d-432d-9760-b2e423d293a4') }}

{{ label('Hinweis', icon='bell', offset_x='4mm', offset_y='50%', uuid='f0645187-9729-4195-9738-7e1fc53ca1cf') }}

{% call note(uuid='e753e69f-6b43-4a4e-84b3-0be1c8544eb9') %}
Einheiten prüfen

Rechnen Sie immer mit Einheiten; ein Fehler fällt dann sofort auf.
{% endcall %}

> [!SELBSTKONTROLLE] Quiz zu Kapitel 5

<!-- Autorenkommentar: Notiz an das Lektorat -->

<!-- Autorenkommentar: Die Aufgabe ist neu und noch nicht geprüft. -->

\> [!AUFGABE] Aufgabe 1: Hubleistung<br>> Ein Kran hebt eine Palette von 500 kg in 20 s um 8 m. Berechnen Sie die Leistung.<br><br>> [!LOESUNG] Lösung<br>> {% raw %}{{ formula('P = \frac{m \cdot g \cdot h}{t} = … \approx 1{,}96\\,\text{kW}') }}{% endraw %}<br><br>> [!HINWEIS] Einheiten prüfen<br>> Rechnen Sie immer mit Einheiten; ein Fehler fällt dann sofort auf.<br><br>> [!SELBSTKONTROLLE] Quiz zu Kapitel 5<br><br>> [!KOMMENTAR] Notiz an das Lektorat<br>> Die Aufgabe ist neu und noch nicht geprüft. {{ uuid('4c75ffab-c32a-406b-8031-40263c13a2db') }}

## Selbstkontrolle {{ uuid('584e6508-b548-4edb-b66f-e1819e02e533') }}

Am Ende eines Kapitels führt ein Etikett mit Link zur Selbstkontrolle, darunter ihr QR-Code für das gedruckte Buch: {{ uuid('a3a32830-42cb-4849-b5a8-df7c4607c975') }}

{{ label('Selbstkontrolle', icon='arrow_right', link='https://example.org/selbstkontrolle/kapitel-5', uuid='19fe66f7-7121-4936-a779-8ade14aa0f34') }}

{{ qr_code('https://example.org/selbstkontrolle/kapitel-5', uuid='8cecc2a4-0b99-4f9d-a50c-664b003a2137') }}

{% raw %}{{ label('Selbstkontrolle', icon='arrow_right', link='https://example.org/selbstkontrolle/kapitel-5') }}{% endraw %}<br><br>{% raw %}{{ qr_code('https://example.org/selbstkontrolle/kapitel-5') }}{% endraw %} {{ uuid('3bd99964-dac9-40a6-b62e-279e697c9edf') }}
