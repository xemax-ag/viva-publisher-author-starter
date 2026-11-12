{# Demo Starter: das Manifest. Jede Zeile ein Eintrag des Dokuments, in dieser Reihenfolge; ausser den Aufrufen nur
   Kommentare wie dieser (die das Rendern entfernt). Dateien relativ zu diesem Ordner. #}
{{ title('Demo Starter', uuid='34aa4ced-6d21-4e22-8592-99d243a6b356') }}
{# ein eigenes Logo aus reference/template/logos/misc/, z. B. logo('nextecmedia'); ohne logo() bleiben die Logos der Vorlage #}
{{ watermark('MUSTER', uuid='afcf1612-75c6-46aa-b3b5-e2471a2e4a3d') }}
{{ cover('cover.md', image='images/cover.svg', uuid='5386aab0-9c67-4f59-a719-c4a8ff4c2830') }}
{{ imprint('impressum.md', top='190mm', uuid='3e345ab5-b11f-427c-b4e4-51fc3cb8a27a') }}
{{ management_summary('management_summary.md', uuid='6ca0274d-8cd1-4382-821f-1288fa072b24') }}
{{ table_of_contents(uuid='cd9b0578-d530-4c75-bb2d-8d1c7760567b') }}
{{ chapter('_1_text_und_struktur.md', image='images/kapitel_1.svg', uuid='0ca61c56-3f2d-4609-b97c-5b7451413e09') }}
{{ chapter('_2_bilder.md', image='images/kapitel_2.svg', uuid='53b56986-d826-4d5b-b0a0-88bdecd63b38') }}
{{ chapter('_3_tabellen.md', image='images/kapitel_3.svg', uuid='a5168cd2-8549-46e6-8df1-077d46d3432f') }}
{{ chapter('_4_formeln.md', image='images/kapitel_4.svg', uuid='bddf26fd-99ec-44ce-a046-1d2b228b6e98') }}
{{ chapter('_5_didaktik.md', image='images/kapitel_5.svg', uuid='1340b041-f830-4ac5-9de5-9eb83cf7768d') }}
{{ list_of_illustrations(uuid='0401c084-c84c-4aff-9f11-d16e0c5ed37f') }}
{{ list_of_tables(uuid='d0702371-1a60-420d-a15a-84742976b80d') }}
{{ glossar('glossar.md', uuid='ce2f4710-2a44-430c-b763-18f93033ec9a') }}
{{ bibliography('quellen.md', uuid='655d9ec2-1e30-410b-9852-1533b73bdbc0') }}
{{ keyword_index(uuid='81d31b42-c35e-4dee-ae22-9a887f49a29e') }}
