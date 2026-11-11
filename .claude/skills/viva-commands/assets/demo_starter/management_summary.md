# Management Summary

Ein Lehrmittel entsteht hier als Ordner von Markdown-Dateien: ein Manifest `_main_.md` legt die Reihenfolge fest, jedes Kapitel ist eine Datei, Bilder liegen im Ordner `images/`. Der Konverter prüft jeden Befehl, schreibt daraus ein Word-Dokument nach der Vorlage textbook_2026_V02 und erstellt das PDF.

## Was dieses Dokument zeigt

- Kapitel {{ ref('kap_text') }}: Überschriften, Auszeichnungen, Listen, Verweise, Fussnoten und Kommentare
- Kapitel {{ ref('kap_bilder') }}: Bilder mit allen Optionen, QR-Codes und Rasterpapier
- Kapitel {{ ref('kap_tabellen') }}: Tabellen als Pipe- und HTML-Tabelle, Bildtabellen und Layouttabellen
- Kapitel {{ ref('kap_formeln') }}: Formeln im Text und als abgesetzte Gleichung
- Kapitel {{ ref('kap_didaktik') }}: Lernziele, Etiketten, Hinweise, Rahmen und Aufgaben

## So arbeiten Sie damit

Jeder Abschnitt zeigt zuerst das Ergebnis und darunter den Markdown-Code, der es erzeugt. Diese Seite selbst ist eine Management Summary: sie steht vor dem Inhaltsverzeichnis, ihre Überschriften sind nicht nummeriert.
