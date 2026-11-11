# Formeln {{ anchor('kap_formeln') }}

Formeln schreiben Sie in LaTeX {{ cite('lamport1994') }}; der Konverter macht daraus Word-Gleichungen, die sich in Word weiter bearbeiten lassen. Das Rendern übersetzt jede Formel einmal zur Probe: Ein Fehler im LaTeX ist ein Problem mit Datei und Zeile.

## Formeln im Text

Im Fliesstext steht `formula()` mitten im Satz: Die elektrische Leistung {{ formula('P = U \cdot I') }} ist das Produkt aus Spannung {{ formula('U') }} und Strom {{ formula('I') }}. Eine Formel mit Apostroph steht in doppelten Anführungszeichen: {{ formula("f'(x) = 2x") }}.

{% raw %}
```markdown
Die elektrische Leistung {{ formula('P = U \cdot I') }} ist das Produkt …
{{ formula("f'(x) = 2x") }}
```
{% endraw %}

## Abgesetzte Gleichungen

Auf einer eigenen Zeile wird `formula()` eine abgesetzte Gleichung, ohne `align` links am Einzug ihrer Formatvorlage, mit `align` zentriert oder rechts:

{{ formula('W = F \cdot s') }}

{{ formula('P = \frac{W}{t}', align='center') }}

{{ formula('\eta = \frac{P_{ab}}{P_{zu}} \cdot 100\,\%', align='right') }}

Eine Word-Gleichung entsteht nur mit `formula()`: LaTeX zwischen Dollarzeichen bleibt Text.

{% raw %}
```markdown
{{ formula('W = F \cdot s') }}
{{ formula('P = \frac{W}{t}', align='center') }}
{{ formula('\eta = \frac{P_{ab}}{P_{zu}} \cdot 100\,\%', align='right') }}
```
{% endraw %}

## Was LaTeX kann

Brüche, Wurzeln, Indizes und Exponenten, griechische Buchstaben, Summen und Integrale, Text in einer Formel und Matrizen:

{{ formula('x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}') }}

{{ formula('\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i') }}

{{ formula('W = \int_{s_1}^{s_2} F(s)\,\mathrm{d}s') }}

{{ formula('\omega = 2 \pi f \quad \text{mit} \quad f = 50\,\text{Hz}') }}

{{ formula('\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}') }}

Auch eine Formel kann einen Identifikator tragen:

{{ formula('E = m \cdot c^2', uuid='1105b258-0ab7-4f07-8c43-6debe6263e68') }}

{% raw %}
```markdown
{{ formula('x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}') }}
{{ formula('\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i') }}
{{ formula('W = \int_{s_1}^{s_2} F(s)\,\mathrm{d}s') }}
{{ formula('\omega = 2 \pi f \quad \text{mit} \quad f = 50\,\text{Hz}') }}
{{ formula('\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}') }}
{{ formula('E = m \cdot c^2', uuid='1105b258-0ab7-4f07-8c43-6debe6263e68') }}
```
{% endraw %}

Formeln in Tabellenzellen zeigt {{ ref('tab_bildformate') }}, Formeln in Hinweisen, Rahmen und Aufgaben das Kapitel {{ ref('kap_didaktik') }}.
