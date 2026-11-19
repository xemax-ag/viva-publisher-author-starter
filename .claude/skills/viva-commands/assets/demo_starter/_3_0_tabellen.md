# Tabellen {{ anchor('kap_tabellen') }}

Eine Tabelle schreiben Sie als Pipe-Tabelle, eine Zeile pro Tabellenzeile, oder als HTML-Tabelle, wenn Zellen über mehrere Zeilen oder Spalten reichen. Eine Zeile `Tabelle: Titel` direkt davor wird die nummerierte Tabellenüberschrift, die das Tabellenverzeichnis aufführt. `table()` davor legt die Spaltenbreiten fest.

## Einfache Tabelle

Die Trennzeile `| --- |` macht die erste Zeile zur Kopfzeile, die auf jeder Seite wiederholt wird. Ohne `table()` teilen sich die Spalten die Textspalte gleichmässig.

Tabelle: Dateien eines Dokuments
| Datei | Inhalt |
| --- | --- |
| `_main_.md` | das Manifest: Titelseite, Kapitel und Verzeichnisse |
| `cover.md` | die Zeilen im Farbband der Titelseite |
| `_1_text_und_struktur.md` | ein Kapitel |
| `images` | die Bilder der Kapitel |

{% raw %}
```markdown
Tabelle: Dateien eines Dokuments
| Datei | Inhalt |
| --- | --- |
| `_main_.md` | das Manifest: Titelseite, Kapitel und Verzeichnisse |
```
{% endraw %}

## Spaltenbreiten und Verweis

Eine Breite pro Spalte, in cm, mm, pt oder Prozent; die Spalten mit `*` teilen sich den Rest. `anchor` macht die Tabelle zum Ziel eines Verweises: {{ ref('tab_einheiten') }} nennt die sieben Basiseinheiten des Internationalen Einheitensystems {{ cite('iso80000') }}.

{% call table('5.5cm', '3cm', '*', anchor='tab_einheiten') %}
Tabelle: SI-Basiseinheiten
| Grösse | Einheit | Zeichen |
| --- | --- | --- |
| Länge | Meter | m |
| Masse | Kilogramm | kg |
| Zeit | Sekunde | s |
| elektrische Stromstärke | Ampere | A |
| thermodynamische Temperatur | Kelvin | K |
| Stoffmenge | Mol | mol |
| Lichtstärke | Candela | cd |
{% endcall %}

{% raw %}
```markdown
{% call table('5.5cm', '3cm', '*', anchor='tab_einheiten') %}
Tabelle: SI-Basiseinheiten
| Grösse | Einheit | Zeichen |
| --- | --- | --- |
| Länge | Meter | m |
{% endcall %}
```
{% endraw %}

## Ohne Kopfzeile, ohne Nummer

Ohne Trennzeile ist jede Zeile eine normale Zeile. Hier steht `table()` als einzelne Zeile direkt vor der Tabelle; zwei feste Breiten unter 16 cm ergeben eine schmalere Tabelle:

{{ table('4cm', '6cm') }}
| Format | A4 hoch |
| Textspalte | 16 cm |
| Schrift | Roboto |

Mit `numbered=False` steht nur der Titel über der Tabelle, ohne «Tabelle n:»:

{% call table('4cm', '*', numbered=False) %}
Tabelle: Seitenränder der Vorlage
| oben | 35,2 mm |
| unten | 23,7 mm |
{% endcall %}

{% raw %}
```markdown
{{ table('4cm', '6cm') }}
| Format | A4 hoch |
| Textspalte | 16 cm |

{% call table('4cm', '*', numbered=False) %}
Tabelle: Seitenränder der Vorlage
| oben | 35,2 mm |
{% endcall %}
```
{% endraw %}
