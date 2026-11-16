Ein Lehrmittel entsteht hier als Ordner von Markdown-Dateien: ein Manifest \_main\_.md legt die Reihenfolge fest, jedes Kapitel ist eine Datei, Bilder liegen im Ordner images/. Der Konverter prüft jeden Befehl, schreibt daraus ein Word-Dokument nach der Vorlage textbook_2026_V02 und erstellt das PDF. {{ uuid('260986ca-a942-4c41-bc9d-4fbd3b49aa29') }}

## Was dieses Dokument zeigt {{ uuid('099a7f58-8e48-40f0-b543-34f5a0d80675') }}

{% call list(uuid='38ef7e96-e691-4e43-a26d-b0b5010052e2') %}
- Kapitel {{ ref('text_und_struktur', uuid='196b4033-0245-4422-93bf-fef0df559e38') }}: Überschriften, Auszeichnungen, Listen, Verweise, Fussnoten und Kommentare
- Kapitel {{ ref('bilder', uuid='2f30c2e7-134f-4586-999a-c1ef2ec99674') }}: Bilder mit allen Optionen, QR-Codes und Rasterpapier
- Kapitel {{ ref('tabellen', uuid='5fecb166-f57b-4c82-ac00-300ec15292b9') }}: Tabellen als Pipe- und HTML-Tabelle, Bildtabellen und Layouttabellen
- Kapitel {{ ref('formeln', uuid='13020f67-0695-4e04-b291-277110041fb7') }}: Formeln im Text und als abgesetzte Gleichung
- Kapitel {{ ref('didaktische_elemente', uuid='5f7a8a06-feb0-4cad-ba07-da97c667a29d') }}: Lernziele, Etiketten, Hinweise, Rahmen und Aufgaben
{% endcall %}

## So arbeiten Sie damit {{ uuid('b5f26e8a-6aa7-4950-b5cb-fa3511e7676d') }}

Jeder Abschnitt zeigt zuerst das Ergebnis und darunter den Markdown-Code, der es erzeugt. Diese Seite selbst ist eine Management Summary: sie steht vor dem Inhaltsverzeichnis, ihre Überschriften sind nicht nummeriert. {{ uuid('8cba84bb-94d1-412b-8c0a-96b6c3f985a1') }}
