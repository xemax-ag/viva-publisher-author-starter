# Management Summary {{ uuid('8cd8f460-8367-4a93-aa8e-9c7ba1188607') }}

Ein Lehrmittel entsteht hier als Ordner von Markdown-Dateien: ein Manifest `_main_.md` legt die Reihenfolge fest, jedes Kapitel ist eine Datei, Bilder liegen im Ordner `images`. Der Konverter prüft jeden Befehl, schreibt daraus ein Word-Dokument nach der Vorlage textbook_2026_V02 und erstellt das PDF. {{ uuid('73c3206e-3e60-4e93-a7e2-298123162e20') }}

## Was dieses Dokument zeigt {{ uuid('fe3ee8cd-fce2-47f8-bd07-fd2d1252113c') }}

{% call list(uuid='56b6dfc5-a29b-4ae7-acdf-1922ebbe80be') %}
- Kapitel {{ ref('kap_text', uuid='9d9b32ad-52e7-4e3f-b167-952a8bb368dc') }}: Überschriften, Auszeichnungen, Listen, Verweise, Fussnoten und Kommentare
- Kapitel {{ ref('kap_bilder', uuid='50722e9b-b5a9-4642-afb4-b093524f2f57') }}: Bilder mit allen Optionen, QR-Codes und Rasterpapier
- Kapitel {{ ref('kap_tabellen', uuid='eba7b953-2a21-4c49-ae20-3d1b7a7cdb48') }}: Tabellen als Pipe- und HTML-Tabelle, Bildtabellen und Layouttabellen
- Kapitel {{ ref('kap_formeln', uuid='63be7a0f-3335-4680-bf21-894b6ce45b0b') }}: Formeln im Text und als abgesetzte Gleichung
- Kapitel {{ ref('kap_didaktik', uuid='5a5c5b4d-1d8a-4d3e-b1e4-406c1d1dc36d') }}: Lernziele, Etiketten, Hinweise, Rahmen und Aufgaben
{% endcall %}

## So arbeiten Sie damit {{ uuid('f25a7dc5-d1a3-421a-a909-b1b415320ae1') }}

Jeder Abschnitt zeigt zuerst das Ergebnis und darunter den Markdown-Code, der es erzeugt. Diese Seite selbst ist eine Management Summary: sie steht vor dem Inhaltsverzeichnis, ihre Überschriften sind nicht nummeriert. {{ uuid('f583d53c-cb11-4c52-9e4d-279c26c3e3a6') }}
