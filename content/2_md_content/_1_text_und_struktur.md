# Text und Struktur {{ anchor('text_und_struktur', uuid='4f59c2f2-2d52-467c-8242-0f13af3bdddc') }} {{ uuid('fb121547-8903-465e-a955-b3f7a8d8c414') }}

Dieses Kapitel zeigt, wie Sie Fliesstext, Überschriften, Listen und Verweise im {{ index('Markdown', uuid='25b2a903-995e-478c-b00e-8aad6bfccfcb') }}Markdown schreiben. Jeder Abschnitt zeigt zuerst das Ergebnis und darunter den Markdown-Code, der es erzeugt. Die Befehle in doppelten geschweiften Klammern prüft das Rendern; ein Fehler nennt Datei und Zeile. {{ uuid('7999c8af-1316-4bfb-aa6f-85ad1d91777c') }}

## Überschriften {{ anchor('ueberschriften', uuid='6233fe11-0c52-462a-9025-81f13336e539') }} {{ uuid('ccfdbe0a-1a9d-49b0-b7e3-707126d5c11f') }}

Ein Kapitel beginnt mit genau einer Überschrift #: Sie steht im Farbband der Kapitelseite. Darunter gliedern ## und ### den Text, nummeriert wie 1.1 und 1.1.1. Eine Überschrift #### ist eine Zwischenüberschrift ohne Nummer. Mit anchor() am Ende der Überschrift erhält sie einen Namen, auf den Sie verweisen können. {{ uuid('7c63ee35-31a8-442c-8a30-0951ec451fa3') }}

### Eine Überschrift der dritten Ebene {{ uuid('56929312-1b0b-4b4b-86d4-2f44ecf4ee53') }}

Text unter einer Überschrift der dritten Ebene. {{ uuid('50fe7b7a-9e91-495a-a06d-ec719b469109') }}

#### Eine Zwischenüberschrift ohne Nummer {{ uuid('d6f7f987-5960-4c34-9eb6-2bc3377bce1e') }}

Text unter einer Zwischenüberschrift. {{ uuid('e8bc1d01-0ed5-470c-8c13-7dc070df5aa1') }}

\# Text und Struktur {% raw %}{{ anchor('kap_text') }}{% endraw %}<br>## Überschriften {% raw %}{{ anchor('ueberschriften') }}{% endraw %}<br>### Eine Überschrift der dritten Ebene<br>#### Eine Zwischenüberschrift ohne Nummer {{ uuid('a0725733-4ff3-4143-a47a-e481b93feade') }}

## Auszeichnungen im Text {{ uuid('8f1a3f47-bfa0-481d-b546-443e5f749497') }}

Text kann **fett** oder *kursiv* sein; zwischen Backticks bleibt er, wie er ist: \*\*nicht fett\*\*. Farbiger Text steht in color(): {{ color('Lebensgefahr!', uuid='ebf3b440-94dc-4440-81b2-e832add18338') }} erscheint in Signalrot, {{ color('**grün und fett**', '#00B050', uuid='00bd70cc-3e61-441f-b1f5-e0a44202fcb7') }} in einer eigenen Farbe. Innerhalb von fettem Text bleibt die Farbe fett: **Warnung:** {{ color('**Starkstrom**', uuid='765bb740-ec93-4b02-a26f-39d9b8352b50') }}. {{ uuid('c47cbbd2-475c-4d86-9e29-fa5d2c66846d') }}

Ein Zeilenumbruch innerhalb eines Absatzes entsteht mit \<br>:<br>Diese Zeile beginnt neu, gehört aber zum selben Absatz. {{ uuid('47138d94-8c18-4d0d-8de1-7645c3f4564e') }}

Ein Backslash vor einem Satzzeichen macht es zu gewöhnlichem Text: {{ uuid('bc9755a9-3f36-4127-8462-85615cbbb010') }}

3\. Schritt: Diese Zeile beginnt mit Zahl und Punkt, ist aber keine Liste. {{ uuid('db1db369-c499-4957-ae85-43ce116753e2') }}

\# Diese Zeile beginnt mit einem Rautezeichen, ist aber keine Überschrift. {{ uuid('fc53acc6-1ec1-4af2-b9f1-c5d4ffdfeea4') }}

Das Produkt 2\*3\*4 ergibt 24, ohne dass ein Teil kursiv wird. {{ uuid('ce265376-43d2-4f3f-a17f-11c1076a1a88') }}

Text kann **fett** oder *kursiv* sein; zwischen Backticks bleibt er, wie er ist: \*\*nicht fett\*\*.<br>{% raw %}{{ color('Lebensgefahr!') }}{% endraw %} {% raw %}{{{% endraw %} color('**grün und fett**', '#00B050') }} **Warnung: {% raw %}{{ color('Starkstrom') }}{% endraw %}**<br>Ein Zeilenumbruch mit \<br>:<br>Diese Zeile beginnt neu.<br>3\\. Schritt … \\# Diese Zeile … 2\\*3\\*4 {{ uuid('5972316c-4700-4619-a064-3c1e5a58976a') }}

#### Symbole {{ uuid('498573d3-390e-4f20-bcb5-fa58977f7f27') }}

Ein Symbol ist ein Zeichen wie jedes andere: z. B. □ zum Ankreuzen, → für einen Ablauf, ± × ≈ für Werte. Das Kästchen der Schrift Wingdings wird als □ übernommen: □. Fett bleibt auch auf farbigem Text erhalten: {{ color('**✓ erledigt**', '#00B050', uuid='6563c1fb-6e11-4532-8a0f-ffed4bcfdce6') }}. {{ uuid('f46944df-03dc-44e4-92ea-c61560d69d38') }}

## Listen {{ uuid('07572752-7412-46d5-8073-3f95f2561a26') }}

Aufzählungen beginnen mit -, nummerierte Listen mit 1.; eingerückte Einträge bilden eine zweite Ebene: {{ uuid('1dbcb1b8-980d-4d73-8803-809dca607bd6') }}

{% call list(uuid='8accf9aa-afde-4985-b955-93f340ffa0c5') %}
- Manuskript in Markdown schreiben
- Befehle einfügen
  - Bilder mit image()
  - Formeln mit formula()
- Dokument rendern und prüfen
{% endcall %}

{% call list(uuid='f2886a14-e15c-4b64-aefd-9df4a104489d') %}
1. Ordner demo_starter kopieren
2. Texte und Bilder ersetzen
3. Word-Dokument und PDF erstellen
{% endcall %}

Eine nummerierte Liste beginnt mit der Nummer ihres ersten Eintrags: {{ uuid('d306711d-6039-4b96-97b3-ce5b1a7e2496') }}

{% call list(uuid='dfed4321-cf36-41bf-81e7-09e9e71eb0c8') %}
3. dritter Schritt
4. vierter Schritt
{% endcall %}

Mit {% raw %}{% call list() %}{% endraw %} erhält eine Liste einen Identifikator, wie ihn die Word-Importe schreiben: {{ uuid('e2e628f1-27bb-4a95-9de4-b5ba21e77f91') }}

{% call list(uuid='ae418e6b-e421-4904-bf04-9d67c638237c') %}
- Vorgehensweise
- benötigtes Material
- Wahl der Messinstrumente
{% endcall %}

\- Manuskript in Markdown schreiben<br>- Befehle einfügen<br> - Bilder mit image()<br>1. Ordner demo_starter kopieren<br>3. dritter Schritt<br><br>{% raw %}{% call list(uuid='ae418e6b-e421-4904-bf04-9d67c638237c') %}{% endraw %}<br>- Vorgehensweise<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('c4ee61bd-013f-4673-a87f-8c00796942b6') }}

## Links und Verweise {{ uuid('32c4f682-ba74-4899-abba-479060950970') }}

Ein Link führt zu einer Webseite: [CommonMark](https://commonmark.org) oder, als Markdown-Link, [Jinja](https://jinja.palletsprojects.com/). Ohne Text zeigt der Link seine Adresse: [mailto:redaktion@example.org](mailto:redaktion@example.org). {{ uuid('52aedb93-2045-445a-89b8-dd7cdeb7eba7') }}

Ein Verweis mit ref() nennt die Nummer, den Titel oder die Seite seines Ziels und ist im PDF anklickbar. Der Abschnitt {{ ref('ueberschriften', uuid='d9bf0362-0014-4b1c-a687-983a3c5cc128') }} heisst «{{ ref('ueberschriften', 'title', uuid='6cd6557e-3ea1-40ff-9239-64eb2b78a1bc') }}» und steht auf Seite {{ ref('ueberschriften', 'page', uuid='c55d996b-8182-4500-998c-f3bb8edf4f82') }}. {{ ref('vom_manuskript_ueber_markdown_und_word_z', uuid='4c86c18d-f96e-4ec8-a04c-6ebfe82b28ef') }} zeigt den Weg vom Manuskript zum PDF, {{ ref('si_basiseinheiten', uuid='c931ae6e-f482-482e-acdf-cee3ee76724a') }} auf Seite {{ ref('si_basiseinheiten', 'page', uuid='a40bc78d-0ece-44dc-852a-f2eceb28440e') }} die SI-Basiseinheiten. Das Ziel darf auch in einem späteren Kapitel stehen. {{ uuid('75615225-fd84-4008-bd4c-ebd2bbaaf1d3') }}

{% raw %}{{ link('https://commonmark.org', 'CommonMark') }}{% endraw %} [Jinja](https://jinja.palletsprojects.com/)<br>{% raw %}{{ link('mailto:redaktion@example.org') }}{% endraw %}<br>Der Abschnitt {% raw %}{{ ref('ueberschriften') }}{% endraw %} heisst «{% raw %}{{ ref('ueberschriften', 'title') }}{% endraw %}»<br>und steht auf Seite {% raw %}{{ ref('ueberschriften', 'page') }}{% endraw %}.<br>{% raw %}{{ ref('abb_workflow') }}{% endraw %} zeigt … {% raw %}{{ ref('tab_einheiten') }}{% endraw %} auf Seite {% raw %}{{ ref('tab_einheiten', 'page') }}{% endraw %} {{ uuid('38c74050-88de-4721-af55-29e13a861cc2') }}

## Fussnoten, Quellen und Stichwörter {{ uuid('20d766a9-a2c2-4a3a-9648-a708be3b4704') }}

Eine Fussnote{{ footnote('Der Text einer Fussnote steht unten auf der Seite; er darf **fett**, *kursiv* oder ein Link sein.', uuid='ab7c4198-64c3-47f9-acb7-63833d9c8133') }} setzt ihre Nummer an die Stelle im Text. Die Nummern beginnen in jedem Kapitel bei 1{{ footnote('Die zweite Fussnote dieses Kapitels.', uuid='74ccfb9a-9c41-4953-a1af-c3f0a6cedab1') }}. {{ uuid('24406627-5e19-423f-b373-2d97a976f45e') }}

Quellen zitieren Sie mit cite(): Die Syntax von Markdown ist in der CommonMark-Spezifikation festgelegt {{ cite('commonmark', uuid='9c7d4dc6-c5e1-4992-8c79-3408b22f4efa') }}, die Formeln folgen der Schreibweise von LaTeX {{ cite('lamport1994', '23–25', uuid='1b83d81b-2d5e-47d5-acf3-5f6206c7099c') }}. Die Nummern zählen in der Reihenfolge der ersten Zitate; das Quellenverzeichnis am Ende listet nur die zitierten Einträge. Fehlt bibliography() im Manifest oder ein Eintrag in quellen.md, bricht das Erstellen ab; im Zustand development meldet das Rendern es nur, und an der Stelle steht [?]. {{ uuid('3902cd6a-ce93-4301-9fcb-570e019737aa') }}

Ein {{ index('Stichwort', uuid='5d032f88-5ebf-43ee-a771-73803646a2e5') }}Stichwort für das Stichwortverzeichnis setzen Sie mit index() direkt vor das Wort, ein Unterstichwort mit einem zweiten Argument: die {{ index('Fussnote', 'Nummerierung', uuid='25749a9d-0216-42e2-8c81-3d0680cc60ca') }}Nummerierung der Fussnoten, der {{ index('Verweis', 'auf Abschnitte', uuid='610672c5-15e8-4fc2-b314-5848813b3ed7') }}Verweis auf einen Abschnitt. Das Manifest braucht dazu keyword_index(): Fehlt es, bricht das Erstellen ab; im Zustand development meldet das Rendern es nur, und das Stichwortverzeichnis fehlt. {{ uuid('d6120b62-345b-4eb0-9854-37e437b7ec0c') }}

Eine Fussnote{% raw %}{{ footnote('Der Text einer Fussnote steht unten auf der Seite.') }}{% endraw %} setzt …<br>… festgelegt {% raw %}{{ cite('commonmark') }}{% endraw %} … LaTeX {% raw %}{{ cite('lamport1994', '23–25') }}{% endraw %}.<br>Ein {% raw %}{{ index('Stichwort') }}{% endraw %}Stichwort … die {% raw %}{{ index('Fussnote', 'Nummerierung') }}{% endraw %}Nummerierung … {{ uuid('f6e31daf-47f5-4e0f-8ed0-bacd8a2970bb') }}

## Identifikatoren {{ uuid('c554c85c-8452-4021-84a0-0100423e7444') }}

Jede Überschrift und jeder Absatz kann am Ende einen Identifikator uuid() tragen; jeder Befehl nimmt ihn als Argument uuid=. Im Word-Dokument steht der Block dann in einem Inhaltssteuerelement mit diesem Identifikator. Die Word-Importe schreiben ihn an jeden Block, damit Änderungen in Word ihrem Block im Markdown zugeordnet werden können. Dieser Absatz trägt einen. {{ uuid('ccde7461-61cd-4e2f-918a-5677649eccad') }}

\## Identifikatoren {% raw %}{{ uuid('c554c85c-8452-4021-84a0-0100423e7444') }}{% endraw %}<br>… Dieser Absatz trägt einen. {% raw %}{{ uuid('ccde7461-61cd-4e2f-918a-5677649eccad') }}{% endraw %}<br>{% raw %}{{ image('images/bauteil.png', width='6cm', uuid='3082ec75-46da-4614-b452-1f4f9b1ad77a') }}{% endraw %} {{ uuid('b0b7caa7-d845-4e5c-9afe-d8cf6af74f31') }}

## Kommentare und Code {{ uuid('cab78eea-bac9-4f00-900a-87ed8ec5ad1b') }}

Was nicht ins Dokument gehört, schreiben Sie als Kommentar. {% raw %}{# … #}{% endraw %} und [//]: # (…) entfernt das Rendern ganz: Nach diesem Absatz stehen zwei solche Kommentare, sichtbar ist keiner. {{ uuid('17d37c43-91f9-4e76-af9b-7cfa5762ffce') }}

Ein HTML-Kommentar dagegen wird ein Autorenkommentar in der Formatvorlage Author Comment, eine Notiz an Lektorat oder Satz: {{ uuid('19bc5e9c-2607-413c-a7f4-241ebc4e7e2a') }}

<!-- Autorenkommentar: Bitte das Foto der Druckmaschine noch nachliefern. -->

Ein Codeblock zwischen drei Backticks erscheint eingerückt, Zeile für Zeile, so wie die Beispiele in diesem Dokument: {{ uuid('ee40ccfc-7b53-4cfb-b6f4-472713f1eded') }}

def flaeche(breite: float, hoehe: float) -> float:<br> return breite \* hoehe {{ uuid('2afbca6d-d381-41ed-9004-f292c3dc95a9') }}

{% raw %}{# Ein Jinja-Kommentar #}{% endraw %}<br>[//]: # (Ein Markdown-Kommentar)<br><!-- Autorenkommentar: Bitte das Foto der Druckmaschine noch nachliefern. --> {{ uuid('344666fc-7647-4c0f-9f92-ef19bd2bb5d2') }}

## Seitenumbruch {{ uuid('ef1a75fd-0bba-4a0a-96de-915ddec90159') }}

Mit page_break() auf einer eigenen Zeile beginnt der nächste Block auf einer neuen Seite. Setzen Sie ihn sparsam ein: Die Formatvorlagen übernehmen das Layout. {{ uuid('4a7ffa15-890c-433b-9012-9339366747c4') }}

{{ page_break(uuid='7b34d240-66cc-4fd8-bd7f-91a37a5ff254') }}

Dieser Absatz steht nach {% raw %}{{ page_break() }}{% endraw %} oben auf einer neuen Seite. {{ uuid('97ae0e5f-4113-481b-80a6-213df834bcc7') }}
