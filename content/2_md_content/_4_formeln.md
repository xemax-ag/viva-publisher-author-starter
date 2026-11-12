# Formeln {{ anchor('kap_formeln', uuid='8444207b-d21e-44bd-bfb1-d1c000dd5b6f') }} {{ uuid('351cb675-b45a-4cbe-828a-ff8e9273a9fb') }}

Formeln schreiben Sie in LaTeX {{ cite('lamport1994', uuid='89fb93a3-2ea4-45a5-9cef-9828653fa9e7') }}; der Konverter macht daraus Word-Gleichungen, die sich in Word weiter bearbeiten lassen. Das Rendern übersetzt jede Formel einmal zur Probe: Ein Fehler im LaTeX ist ein Problem mit Datei und Zeile. {{ uuid('184921ba-09ac-4314-be65-3b4288418afc') }}

## Formeln im Text {{ uuid('8d50f68e-aa43-4260-96ec-a43644237887') }}

Im Fliesstext steht `formula()` mitten im Satz: Die elektrische Leistung {{ formula('P = U \cdot I', uuid='0f3b144a-7bef-48b8-9e74-a8c6722cb493') }} ist das Produkt aus Spannung {{ formula('U', uuid='26773c6b-5d57-4b0d-a2bf-61545c4f48db') }} und Strom {{ formula('I', uuid='72ef0946-7235-4d0e-a11d-d4c2c4fc188e') }}. Eine Formel mit Apostroph steht in doppelten Anführungszeichen: {{ formula("f'(x) = 2x", uuid='bfe411ea-a5da-44d1-b2e0-ecf246207485') }}. {{ uuid('6e95bfee-fe5f-4048-aeb7-fedc0fe501a4') }}

{% raw %}
```markdown
Die elektrische Leistung {{ formula('P = U \cdot I') }} ist das Produkt …
{{ formula("f'(x) = 2x") }}
```
{% endraw %}

## Abgesetzte Gleichungen {{ uuid('0b9de1da-6d0c-4a3d-9529-c9a8d470ae2f') }}

Auf einer eigenen Zeile wird `formula()` eine abgesetzte Gleichung, ohne `align` links am Einzug ihrer Formatvorlage, mit `align` zentriert oder rechts: {{ uuid('8568ef47-5069-43d8-9be3-d050ade494e2') }}

{{ formula('W = F \cdot s', uuid='040f1cfd-4249-4123-86dd-41277d310624') }}

{{ formula('P = \frac{W}{t}', align='center', uuid='4f1bc5e7-67e8-4305-a334-d8ed44c535fd') }}

{{ formula('\eta = \frac{P_{ab}}{P_{zu}} \cdot 100\,\%', align='right', uuid='2fbf91bc-f12e-43ed-b082-bd891d8f1753') }}

Eine Word-Gleichung entsteht nur mit `formula()`: LaTeX zwischen Dollarzeichen bleibt Text. {{ uuid('1a54f293-8fff-4310-bc12-d78f676a8583') }}

{% raw %}
```markdown
{{ formula('W = F \cdot s') }}
{{ formula('P = \frac{W}{t}', align='center') }}
{{ formula('\eta = \frac{P_{ab}}{P_{zu}} \cdot 100\,\%', align='right') }}
```
{% endraw %}

## Was LaTeX kann {{ uuid('67379b8b-ae14-4c6f-b684-3efe248882ff') }}

Brüche, Wurzeln, Indizes und Exponenten, griechische Buchstaben, Summen und Integrale, Text in einer Formel und Matrizen: {{ uuid('8dd3b987-7b9b-4e32-9dfb-000d44df122c') }}

{{ formula('x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}', uuid='a7daf50f-f5a3-496d-a718-2a3563cb9f4f') }}

{{ formula('\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i', uuid='114665a0-73be-4c78-a982-7d6ad0adc34b') }}

{{ formula('W = \int_{s_1}^{s_2} F(s)\,\mathrm{d}s', uuid='ce440ead-16e0-452a-85be-55a9fe11091d') }}

{{ formula('\omega = 2 \pi f \quad \text{mit} \quad f = 50\,\text{Hz}', uuid='67e34f2a-c0ae-4e43-a2af-bcd4eddf67bb') }}

{{ formula('\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}', uuid='42c101dd-1075-4e4f-8f09-1c956d7438fd') }}

Auch eine Formel kann einen Identifikator tragen: {{ uuid('9b0ed12d-b164-46f6-896c-44a1da5ac15e') }}

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

Formeln in Tabellenzellen zeigt {{ ref('tab_bildformate', uuid='c7dff148-7f3c-4a4e-b60c-7e1354f88b7b') }}, Formeln in Hinweisen, Rahmen und Aufgaben das Kapitel {{ ref('kap_didaktik', uuid='bfb98ece-4fc3-4729-ac6c-f731cf19297a') }}. {{ uuid('04eb8365-fe2e-4f7f-adfc-ac3e99eac5e1') }}
