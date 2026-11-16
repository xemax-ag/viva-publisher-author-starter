# Formeln {{ anchor('formeln', uuid='6f886ea8-9ddf-4409-8658-5808d22df542') }} {{ uuid('2aef3c2e-873f-4ea1-9e19-90434e83c3b6') }}

Formeln schreiben Sie in LaTeX {{ cite('lamport1994', uuid='e7eaa184-7860-4700-a598-f539bd7914ba') }}; der Konverter macht daraus Word-Gleichungen, die sich in Word weiter bearbeiten lassen. Das Rendern übersetzt jede Formel einmal zur Probe: Ein Fehler im LaTeX ist ein Problem mit Datei und Zeile. {{ uuid('79e4a89e-aca5-4d07-a5d6-356b53bd5a74') }}

## Formeln im Text {{ uuid('e1a76808-d85a-4a4d-8ed4-b2b2ddaac861') }}

Im Fliesstext steht formula() mitten im Satz: Die elektrische Leistung {{ formula('P = U \cdot I', uuid='b8437755-a767-4526-b94a-a2ab9092a673') }} ist das Produkt aus Spannung {{ formula('U', uuid='5c5cf7cc-f7a6-49d6-b3ac-8e8a3a7ffcdb') }} und Strom {{ formula('I', uuid='2a47923a-81d9-4393-9d52-56211d516944') }}. Eine Formel mit Apostroph steht in doppelten Anführungszeichen: {{ formula("f'(x) = 2x", uuid='6abedf59-6dfb-428c-8e62-a95671520342') }}. {{ uuid('20882ebd-e0f3-4fa5-97fd-41cfeb138de3') }}

Die elektrische Leistung {% raw %}{{ formula('P = U \cdot I') }}{% endraw %} ist das Produkt …<br>{% raw %}{{ formula("f'(x) = 2x") }}{% endraw %} {{ uuid('b409f4a5-8b34-4b43-ba54-4bfe79e12337') }}

## Abgesetzte Gleichungen {{ uuid('3b235f83-acc6-4598-851a-66a124dcf692') }}

Auf einer eigenen Zeile wird formula() eine abgesetzte Gleichung, ohne align links am Einzug ihrer Formatvorlage, mit align zentriert oder rechts: {{ uuid('ba71f1b5-e17d-4bb3-9a6a-252203b993f0') }}

{{ formula('W = F \cdot s', uuid='e13e4754-476c-46a4-8757-5eb10bcba38e') }}

{{ formula('P = \frac{W}{t}', align='center', uuid='43cbbfe2-2425-4cc1-93f9-597cc4dc03f4') }}

{{ formula('\eta = \frac{P_{\textit{ab}}}{P_{\textit{zu}}} \cdot 100\text{ }\%', align='right', uuid='092da505-529a-416a-a6bc-10d8b0294160') }}

Eine Word-Gleichung entsteht nur mit formula(): LaTeX zwischen Dollarzeichen bleibt Text. {{ uuid('becafd7f-d109-4996-8593-7ada29e88144') }}

{% raw %}{{ formula('W = F \cdot s') }}{% endraw %}<br>{% raw %}{{ formula('P = \frac{W}{t}', align='center') }}{% endraw %}<br>{% raw %}{{ formula('\eta = \frac{P\_{ab}}{% endraw %}{P\_{zu}} \cdot 100\\,\\%', align='right') }} {{ uuid('bafa4596-808b-4c71-b37d-bf0ce0640222') }}

## Was LaTeX kann {{ uuid('82b39078-3d70-42f1-bb4c-76952b3e9ffe') }}

Brüche, Wurzeln, Indizes und Exponenten, griechische Buchstaben, Summen und Integrale, Text in einer Formel und Matrizen: {{ uuid('77fc31c9-ad17-4853-b7bd-06ac3e9e4068') }}

{{ formula('x_{1,2} = \frac{- b \pm \sqrt{b^{2} - 4\textit{ac}}}{2a}', uuid='f70b11bf-486e-494f-b694-a1c0a66d14e2') }}

{{ formula('\bar{x} = \frac{1}{n}\sum_{i = 1}^{n}x_{i}', uuid='83b8c577-27b7-416e-aa93-0bb8870f192b') }}

{{ formula('W = \int_{s_{1}}^{s_{2}}F(s)\text{ }\textit{ds}', uuid='2f779866-288f-4db3-90cb-75b6e98ec9d5') }}

{{ formula('\omega = 2\pi f\text{\quad mit\quad}f = 50\text{ Hz}', uuid='b4aa0c27-8bc3-4d72-8f86-969f1661e735') }}

{{ formula('\begin{pmatrix} \cos\varphi & - \sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}', uuid='3793dc4a-2882-4011-8189-79023e6ea949') }}

Auch eine Formel kann einen Identifikator tragen: {{ uuid('7be3021a-edb1-4098-a9ed-c9afba65f3d4') }}

{{ formula('E = m \cdot c^{2}', uuid='1105b258-0ab7-4f07-8c43-6debe6263e68') }}

{% raw %}{{ formula('x\_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{% endraw %}{2a}') }}<br>{% raw %}{{ formula('\bar{x} = \frac{1}{n} \sum\_{i=1}^{n} x_i') }}{% endraw %}<br>{% raw %}{{ formula('W = \int\_{s_1}^{s_2} F(s)\\,\mathrm{d}s') }}{% endraw %}<br>{% raw %}{{ formula('\omega = 2 \pi f \quad \text{mit} \quad f = 50\\,\text{Hz}') }}{% endraw %}<br>{% raw %}{{ formula('\begin{pmatrix} \cos\varphi & -\sin\varphi \\\ \sin\varphi & \cos\varphi \end{pmatrix}') }}{% endraw %}<br>{% raw %}{{ formula('E = m \cdot c^2', uuid='1105b258-0ab7-4f07-8c43-6debe6263e68') }}{% endraw %} {{ uuid('f5be7416-1c57-413f-8464-b9f5266d2872') }}

Formeln in Tabellenzellen zeigt {{ ref('bildformate_im_vergleich', uuid='4ea06dd1-2309-4403-a06d-6943b0abbbb1') }}, Formeln in Hinweisen, Rahmen und Aufgaben das Kapitel {{ ref('didaktische_elemente', uuid='1e5048a4-d986-4bbe-813b-719b512ecb2e') }}. {{ uuid('1cb91172-fcbf-42ba-9574-cd2b5515097f') }}
