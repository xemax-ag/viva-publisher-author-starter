# Bilder {{ anchor('bilder', uuid='88e79be2-84c2-42b2-b2ad-9b0b290d7e51') }} {{ uuid('d7bf0638-7940-488d-9979-8262658cb095') }}

Bilder stehen mit image() auf einer eigenen Zeile, ihr Pfad relativ zur Kapiteldatei. PNG und JPG werden eingebettet, SVG als Vektorgrafik mit einem PNG als Ersatz für Programme ohne SVG. Ein Bild ist nie breiter als die Textspalte von 16 cm. Das Bild über diesem Kapitel setzt das Manifest mit chapter(…, image=…), das Titelbild mit cover(…, image=…). {{ uuid('ae2df53d-ec9d-42af-a23d-5c1af22308ce') }}

## Bild mit Bildunterschrift {{ uuid('49bf72da-e603-4ecf-98c3-a4d193d99a7c') }}

Ein title gibt dem Bild eine nummerierte Bildunterschrift, die das Abbildungsverzeichnis aufführt; anchor macht es zum Ziel eines Verweises: {{ ref('vom_manuskript_ueber_markdown_und_word_z', uuid='b3ffcdf4-2c9b-47d1-b949-8ac8c27dd5aa') }} steht auf Seite {{ ref('vom_manuskript_ueber_markdown_und_word_z', 'page', uuid='be8ab874-7c51-4878-a764-ffc70fbbba58') }}. Der alt_text ist der Alternativtext für Screenreader. {{ uuid('1f946c54-8fa7-4762-bd4f-dab67223f1c7') }}

{{ image('images/2_bilder/01.png', width='14.0cm', title='Vom Manuskript über Markdown und Word zum PDF', anchor='vom_manuskript_ueber_markdown_und_word_z', alt_text=None, uuid='7ae4b4ba-da77-4179-b766-afebb8807f3a') }}

{% raw %}{{{% endraw %} image('images/workflow.svg', width='14cm', title='Vom Manuskript über Markdown und Word zum PDF',<br> anchor='abb_workflow', alt_text='Vier Dokumente mit Pfeilen: Manuskript, Markdown, Word, PDF') }}<br>{% raw %}{{ ref('abb_workflow') }}{% endraw %} steht auf Seite {% raw %}{{ ref('abb_workflow', 'page') }}{% endraw %}. {{ uuid('2ad6fb0e-bad5-4353-b6d8-f383359a04ad') }}

## Grösse {{ uuid('75e7360a-23b2-493c-a97a-2d63269d9efd') }}

Die Breite width in cm, mm, pt oder Prozent der Textspalte; die Höhe folgt aus dem Seitenverhältnis. Mit height allein bestimmt die Höhe, mit beiden passt das Bild in den Rahmen, ohne verzerrt zu werden. scale bezieht sich auf die native Grösse der Datei (Pixel geteilt durch dpi): Das PNG des Flanschs hat 900 Pixel bei 300 dpi, also 7,6 cm. Bildschirmfotos verkleinern Sie nicht unter 84 %, sonst wird ihr Text zu klein; der Konverter warnt dann. {{ uuid('252983cc-6479-4a58-a44d-795509b6ab07') }}

{{ image('images/2_bilder/02.png', width='5.0cm', title='Breite 5 cm', alt_text=None, uuid='cdb07264-063e-483f-a9bf-032ca0cccaf5') }}

{{ image('images/2_bilder/03.png', width='8.0cm', title='Breite 50 % der Textspalte', alt_text=None, uuid='efd40625-18c8-4252-b4b9-675253843f2d') }}

{{ image('images/2_bilder/04.png', width='4.8cm', title='Höhe 3 cm', alt_text=None, uuid='9fe26e96-1961-4a32-94b3-789cfafd0ef2') }}

{{ image('images/2_bilder/05.png', width='6.9cm', title='90 % der nativen Grösse', alt_text=None, uuid='4248f3eb-b304-4a45-a091-6cfaca34c230') }}

{% raw %}{{ image('images/bauteil.png', width='5cm', title='Breite 5 cm') }}{% endraw %}<br>{% raw %}{{ image('images/bauteil.png', width='50%', title='Breite 50 % der Textspalte') }}{% endraw %}<br>{% raw %}{{ image('images/bauteil.png', height='3cm', title='Höhe 3 cm') }}{% endraw %}<br>{% raw %}{{ image('images/bauteil.png', scale='90%', title='90 % der nativen Grösse') }}{% endraw %} {{ uuid('9971631d-6704-4694-9e1a-129b636c98c1') }}

## Ausrichtung, Rahmen und Zuschnitt {{ uuid('791dc132-bfc8-4619-8128-63ba838f63ed') }}

Ohne align steht ein Bild in der Mitte; 'left' und 'right' setzen es an den Rand. border=True zeichnet eine graue Linie um das Bild. crop schneidet in Prozent ab, in der Reihenfolge oben, rechts, unten, links wie in CSS; Word schneidet zu, die Datei bleibt unverändert. {{ uuid('cb54dda2-f5d5-4a37-83b7-0af38328bdaf') }}

{{ image('images/2_bilder/06.png', width='5.0cm', align='left', title='Links, mit Rahmen', alt_text=None, uuid='aac57484-46c6-43b0-a6b0-9c1f85613b3a') }}

{{ image('images/2_bilder/07.png', width='5.0cm', align='right', title='Rechts, links und rechts je 25 % abgeschnitten', alt_text=None, uuid='12a49a35-e1b8-44ac-82c6-e9be955c8ba1') }}

{% raw %}{{ image('images/bauteil.png', width='5cm', align='left', border=True, title='Links, mit Rahmen') }}{% endraw %}<br>{% raw %}{{{% endraw %} image('images/bauteil.png', width='5cm', align='right', crop='0 25% 0 25%',<br> title='Rechts, links und rechts je 25 % abgeschnitten') }} {{ uuid('d57fe345-4e7f-41c0-85a8-9f84e12cb735') }}

## Umfliessender Text {{ uuid('bd927a4b-c6ea-449a-a3fc-3ef5f2af0e32') }}

{{ image('images/2_bilder/08.png', width='6.0cm', align='right', wrap=True, title='Flansch, Draufsicht', alt_text=None, uuid='95ca73fa-dda9-400a-a355-c3ddcd2eb797') }}

Mit wrap=True steht das Bild mit seiner Bildunterschrift in einem Rahmen am Rand, der Text fliesst daneben vorbei. Das eignet sich für kleine Bilder neben einem längeren Absatz, etwa eine Zeichnung neben ihrer Beschreibung. Der Flansch in der Zeichnung hat vier Bohrungen auf einem Lochkreis; die strichpunktierten Linien sind Mittellinien, die Pfeile bemassen Aussendurchmesser und Lochkreis. In einer technischen Zeichnung stehen an diesen Massen Zahlen; hier bleibt die Zeichnung ohne Text, damit sie in jeder Sprache passt. {{ uuid('2df2e2b8-b100-4a12-b205-7b72fb618206') }}

Ein umflossenes Bild steht links oder rechts, nie in der Mitte. Folgt kein Text, beginnt der nächste Block unter dem Bild. {{ uuid('7f551a3f-6897-43f4-937e-cedaa2a8a614') }}

{% raw %}{{ image('images/bauteil.png', width='6cm', align='right', wrap=True, title='Flansch, Draufsicht') }}{% endraw %}<br><br>Mit wrap=True steht das Bild … {{ uuid('6e120f74-7748-4786-b597-8ed16974485e') }}

## Bildunterschrift ohne Nummer und gedrehtes Bild {{ uuid('aacca99f-68d5-4435-bd0a-8c493bb694a8') }}

Mit numbered=False steht nur der Titel unter dem Bild, ohne «Abbildung n:». rotate dreht das Bild um 90, 180 oder 270 Grad im Uhrzeigersinn, negativ dagegen; Breite und Zuschnitt gelten danach. So passt ein Diagramm im Querformat hochkant auf die Seite: {{ uuid('dbfb2259-2909-4c31-b318-05f54e0e7177') }}

{{ image('images/2_bilder/09.png', width='7.0cm', title='Monatswerte, um 90 Grad gedreht', numbered=False, alt_text=None, uuid='047a1018-a393-4a70-823f-49388e56a1df') }}

{% raw %}{{ image('images/diagramm.svg', width='7cm', rotate=-90, title='Monatswerte, um 90 Grad gedreht', numbered=False) }}{% endraw %} {{ uuid('5928fb3c-b0fa-4066-a5fe-f470f47919a4') }}

## Pfeile und Text über dem Bild

Mit overlay liegt ein zweites Bild über dem Bild, meist ein durchsichtiges SVG mit Pfeilen, Kreisen und Text. Seine linke obere Ecke ist die des Bildes, overlay_x und overlay_y verschieben sie; ragt es oben oder unten über das Bild hinaus, erhält das Bild dort Platz. Ohne overlay_width und overlay_height ist es so gross wie das Bild; der Build schreibt beide in den Aufruf. Hier ragt es rechts 3 cm über das Bild hinaus:

{{ image('images/2_bilder/03.png', width='8cm', overlay='images/2_bilder/bauteil_pfeile.svg', overlay_width='11.00cm', overlay_height='5.00cm', title='Flansch mit markierter Bohrung') }}

{% raw %}
```markdown
{{ image('images/bauteil.png', width='8cm', overlay='images/bauteil_pfeile.svg', overlay_width='11.00cm',
         overlay_height='5.00cm', title='Flansch mit markierter Bohrung') }}
```
{% endraw %}

Pfeile, Kreise, Rechtecke und Textfelder, die in Word über ein Bild gezeichnet sind, übernimmt der Word-Import so als Overlay, auch gruppiert.

## Markdown-Bild und Platzhalter {{ uuid('32bec117-2169-4eca-bfd4-f6bead1ca124') }}

Auch die Markdown-Schreibweise für Bilder funktioniert; der Text in eckigen Klammern wird der Alternativtext, ein Titel in Anführungszeichen die Bildunterschrift: {{ uuid('425d01b6-662a-4a59-9380-4495b469b100') }}

{{ image('images/2_bilder/10.png', width='7.6cm', align='left', title='Flansch als Markdown-Bild', alt_text=None, uuid='5b24c54c-2937-4589-a9dc-c8222c28c006') }}

Fehlt ein Bild noch, steht sein Dateiname in doppelten runden Klammern als Platzhalter: {{ uuid('122658e0-f343-4835-9494-680ab6a2b681') }}

((Foto_Druckmaschine.jpg))

!\[Flansch mit vier Bohrungen auf dem Lochkreis](images/bauteil.png "Flansch als Markdown-Bild")<br>((Foto_Druckmaschine.jpg)) {{ uuid('80192fd9-6462-4ade-8567-136353663a48') }}

## QR-Code {{ uuid('09400cbb-f509-4ab7-b8c9-cd67c93db7a4') }}

qr_code() erzeugt beim Rendern einen QR-Code; Grösse, Farbe und Ausrichtung sind wählbar. Ohne Text erscheint ein Warnzeichen, damit ein fehlender Code auffällt. {{ uuid('7c05d3bb-4720-4c04-a719-3f4ae2772caf') }}

{{ qr_code('https://commonmark.org', uuid='efbaa7b8-770d-4bab-abdf-5beb19f35d0b') }}

{{ qr_code('https://spec.commonmark.org/0.31.2/', uuid='2a8df86f-c27d-47c2-95e2-8d66e610b25f') }}

{{ qr_code(None, uuid='6f4ce5c1-ed4b-49b3-b684-19380928b1af') }}

{% raw %}{{ qr_code('https://commonmark.org') }}{% endraw %}<br>{% raw %}{{ qr_code('https://spec.commonmark.org/0.31.2/', '2cm', '#03A4C0', 'center') }}{% endraw %}<br>{% raw %}{{ qr_code(size='2cm', alignment='right') }}{% endraw %} {{ uuid('6f632e93-cb1c-46f8-8e42-ae284b6cce90') }}

## Rasterpapier {{ uuid('d7c615ea-be0f-4d02-b2a7-88c7249cd547') }}

grid() zeichnet Häuschenpapier, etwa als Platz für eine Skizze oder eine Rechnung: ohne Argumente 32 × 47 Häuschen zu 5 mm, die eine ganze Seite füllen. {{ uuid('0004986f-1f3d-41ed-b2f9-f4977e7858fc') }}

{{ grid(n_height=6, uuid='1df12302-0278-41ce-9891-9b9f09fecb46') }}

{{ grid(spacing='4mm', n_width=20, n_height=5, thickness='0.2mm', color='#03A4C0', alignment='center', uuid='a8b19705-a0bb-49b8-bee0-ea36e6c3ae46') }}

{% raw %}{{ grid(n_height=6) }}{% endraw %}<br>{% raw %}{{ grid('4mm', 20, 5, '0.2mm', '#03A4C0', 'center') }}{% endraw %} {{ uuid('477b622b-4094-46a5-90ec-29fbb213bf11') }}
