# Bilder {{ anchor('kap_bilder') }}

Bilder stehen mit `image()` auf einer eigenen Zeile, ihr Pfad relativ zur Kapiteldatei. PNG und JPG werden eingebettet, SVG als Vektorgrafik mit einem PNG als Ersatz für Programme ohne SVG. Ein Bild ist nie breiter als die Textspalte von 16 cm. Das Bild über diesem Kapitel setzt das Manifest mit `chapter(…, image=…)`, das Titelbild mit `cover(…, image=…)`.

## Bild mit Bildunterschrift

Ein `title` gibt dem Bild eine nummerierte Bildunterschrift, die das Abbildungsverzeichnis aufführt; `anchor` macht es zum Ziel eines Verweises: {{ ref('abb_workflow') }} steht auf Seite {{ ref('abb_workflow', 'page') }}. Der `alt_text` ist der Alternativtext für Screenreader.

{{ image('images/workflow.svg', width='14cm', title='Vom Manuskript über Markdown und Word zum PDF', anchor='abb_workflow', alt_text='Vier Dokumente mit Pfeilen: Manuskript, Markdown, Word, PDF') }}

{% raw %}
```markdown
{{ image('images/workflow.svg', width='14cm', title='Vom Manuskript über Markdown und Word zum PDF',
         anchor='abb_workflow', alt_text='Vier Dokumente mit Pfeilen: Manuskript, Markdown, Word, PDF') }}
{{ ref('abb_workflow') }} steht auf Seite {{ ref('abb_workflow', 'page') }}.
```
{% endraw %}

## Grösse

Die Breite `width` in cm, mm, pt oder Prozent der Textspalte; die Höhe folgt aus dem Seitenverhältnis. Mit `height` allein bestimmt die Höhe, mit beiden passt das Bild in den Rahmen, ohne verzerrt zu werden. `scale` bezieht sich auf die native Grösse der Datei (Pixel geteilt durch dpi): Das PNG des Flanschs hat 900 Pixel bei 300 dpi, also 7,6 cm. Bildschirmfotos verkleinern Sie nicht unter 84 %, sonst wird ihr Text zu klein; der Konverter warnt dann.

{{ image('images/bauteil.png', width='5cm', title='Breite 5 cm') }}

{{ image('images/bauteil.png', width='50%', title='Breite 50 % der Textspalte') }}

{{ image('images/bauteil.png', height='3cm', title='Höhe 3 cm') }}

{{ image('images/bauteil.png', scale='90%', title='90 % der nativen Grösse') }}

{% raw %}
```markdown
{{ image('images/bauteil.png', width='5cm', title='Breite 5 cm') }}
{{ image('images/bauteil.png', width='50%', title='Breite 50 % der Textspalte') }}
{{ image('images/bauteil.png', height='3cm', title='Höhe 3 cm') }}
{{ image('images/bauteil.png', scale='90%', title='90 % der nativen Grösse') }}
```
{% endraw %}

## Ausrichtung, Rahmen und Zuschnitt

Ohne `align` steht ein Bild in der Mitte; `'left'` und `'right'` setzen es an den Rand. `border=True` zeichnet eine graue Linie um das Bild. `crop` schneidet in Prozent ab, in der Reihenfolge oben, rechts, unten, links wie in CSS; Word schneidet zu, die Datei bleibt unverändert.

{{ image('images/bauteil.png', width='5cm', align='left', border=True, title='Links, mit Rahmen') }}

{{ image('images/bauteil.png', width='5cm', align='right', crop='0 25% 0 25%', title='Rechts, links und rechts je 25 % abgeschnitten') }}

{% raw %}
```markdown
{{ image('images/bauteil.png', width='5cm', align='left', border=True, title='Links, mit Rahmen') }}
{{ image('images/bauteil.png', width='5cm', align='right', crop='0 25% 0 25%',
         title='Rechts, links und rechts je 25 % abgeschnitten') }}
```
{% endraw %}

## Umfliessender Text

{{ image('images/bauteil.png', width='6cm', align='right', wrap=True, title='Flansch, Draufsicht') }}

Mit `wrap=True` steht das Bild mit seiner Bildunterschrift in einem Rahmen am Rand, der Text fliesst daneben vorbei. Das eignet sich für kleine Bilder neben einem längeren Absatz, etwa eine Zeichnung neben ihrer Beschreibung. Der Flansch in der Zeichnung hat vier Bohrungen auf einem Lochkreis; die strichpunktierten Linien sind Mittellinien, die Pfeile bemassen Aussendurchmesser und Lochkreis. In einer technischen Zeichnung stehen an diesen Massen Zahlen; hier bleibt die Zeichnung ohne Text, damit sie in jeder Sprache passt.

Ein umflossenes Bild steht links oder rechts, nie in der Mitte. Folgt kein Text, beginnt der nächste Block unter dem Bild.

{% raw %}
```markdown
{{ image('images/bauteil.png', width='6cm', align='right', wrap=True, title='Flansch, Draufsicht') }}

Mit `wrap=True` steht das Bild …
```
{% endraw %}

## Bildunterschrift ohne Nummer und gedrehtes Bild

Mit `numbered=False` steht nur der Titel unter dem Bild, ohne «Abbildung n:». `rotate` dreht das Bild um 90, 180 oder 270 Grad im Uhrzeigersinn, negativ dagegen; Breite und Zuschnitt gelten danach. So passt ein Diagramm im Querformat hochkant auf die Seite:

{{ image('images/diagramm.svg', width='7cm', rotate=-90, title='Monatswerte, um 90 Grad gedreht', numbered=False) }}

{% raw %}
```markdown
{{ image('images/diagramm.svg', width='7cm', rotate=-90, title='Monatswerte, um 90 Grad gedreht', numbered=False) }}
```
{% endraw %}

## Markdown-Bild und Platzhalter

Auch die Markdown-Schreibweise für Bilder funktioniert; der Text in eckigen Klammern wird der Alternativtext, ein Titel in Anführungszeichen die Bildunterschrift:

![Flansch mit vier Bohrungen auf dem Lochkreis](images/bauteil.png "Flansch als Markdown-Bild")

Fehlt ein Bild noch, steht sein Dateiname in doppelten runden Klammern als Platzhalter:

((Foto_Druckmaschine.jpg))

{% raw %}
```markdown
![Flansch mit vier Bohrungen auf dem Lochkreis](images/bauteil.png "Flansch als Markdown-Bild")
((Foto_Druckmaschine.jpg))
```
{% endraw %}

## QR-Code

`qr_code()` erzeugt beim Rendern einen QR-Code; Grösse, Farbe und Ausrichtung sind wählbar. Ohne Text erscheint ein Warnzeichen, damit ein fehlender Code auffällt.

{{ qr_code('https://commonmark.org') }}

{{ qr_code('https://spec.commonmark.org/0.31.2/', '2cm', '#03A4C0', 'center') }}

{{ qr_code(size='2cm', alignment='right') }}

{% raw %}
```markdown
{{ qr_code('https://commonmark.org') }}
{{ qr_code('https://spec.commonmark.org/0.31.2/', '2cm', '#03A4C0', 'center') }}
{{ qr_code(size='2cm', alignment='right') }}
```
{% endraw %}

## Rasterpapier

`grid()` zeichnet Häuschenpapier, etwa als Platz für eine Skizze oder eine Rechnung: ohne Argumente 32 × 47 Häuschen zu 5 mm, die eine ganze Seite füllen.

{{ grid(n_height=6) }}

{{ grid('4mm', 20, 5, '0.2mm', '#03A4C0', 'center') }}

{% raw %}
```markdown
{{ grid(n_height=6) }}
{{ grid('4mm', 20, 5, '0.2mm', '#03A4C0', 'center') }}
```
{% endraw %}
