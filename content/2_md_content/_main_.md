{# Demo Starter: das Manifest. Jede Zeile ein Eintrag des Dokuments, in dieser Reihenfolge; ausser den Aufrufen nur
   Kommentare wie dieser (die das Rendern entfernt). Dateien relativ zu diesem Ordner. #}
{{ title('Demo Starter') }}
{# ein eigenes Logo aus reference/template/logos/misc/, z. B. logo('nextecmedia'); ohne logo() bleiben die Logos der Vorlage #}
{{ watermark('MUSTER') }}
{{ cover('cover.md', image='images/cover.svg') }}
{{ imprint('impressum.md', top='190mm') }}
{{ management_summary('management_summary.md') }}
{{ table_of_contents() }}
{{ chapter('_1_text_und_struktur.md', image='images/kapitel_1.svg') }}
{{ chapter('_2_bilder.md', image='images/kapitel_2.svg') }}
{{ chapter('_3_tabellen.md', image='images/kapitel_3.svg') }}
{{ chapter('_4_formeln.md', image='images/kapitel_4.svg') }}
{{ chapter('_5_didaktik.md', image='images/kapitel_5.svg') }}
{{ list_of_illustrations() }}
{{ list_of_tables() }}
{{ glossar('glossar.md') }}
{{ bibliography('quellen.md') }}
{{ keyword_index() }}
