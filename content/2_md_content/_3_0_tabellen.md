# Tabellen {{ anchor('tabellen', uuid='d90e0923-33d6-4570-9337-28c7fcf73b1b') }} {{ uuid('6e4db1f3-8798-4e71-9854-fae642775811') }}

Eine Tabelle schreiben Sie als Pipe-Tabelle, eine Zeile pro Tabellenzeile, oder als HTML-Tabelle, wenn Zellen über mehrere Zeilen oder Spalten reichen. Eine Zeile Tabelle: Titel direkt davor wird die nummerierte Tabellenüberschrift, die das Tabellenverzeichnis aufführt. table() davor legt die Spaltenbreiten fest. {{ uuid('b7574aa8-6800-4e9a-87ae-1ace22e84536') }}

## Einfache Tabelle {{ uuid('d5540511-bf55-458b-b006-d625becacf03') }}

Die Trennzeile | --- | macht die erste Zeile zur Kopfzeile, die auf jeder Seite wiederholt wird. Ohne table() teilen sich die Spalten die Textspalte gleichmässig. {{ uuid('28355bdb-d71d-4f8a-aa6a-4a4878d9df38') }}

{% call table('8.0cm', '8.0cm', uuid='6ef7f852-f1f3-4453-b45e-2a1d58e36fd0') %}
Tabelle: Dateien eines Dokuments
<table>
  <thead>
    <tr>
      <th>Datei</th>
      <th>Inhalt</th>
    </tr>
  </thead>
  <tr>
    <td>\_main\_.md</td>
    <td>das Manifest: Titelseite, Kapitel und Verzeichnisse</td>
  </tr>
  <tr>
    <td>cover.md</td>
    <td>die Zeilen im Farbband der Titelseite</td>
  </tr>
  <tr>
    <td>\_1_text_und_struktur.md</td>
    <td>ein Kapitel</td>
  </tr>
  <tr>
    <td>images/</td>
    <td>die Bilder der Kapitel</td>
  </tr>
</table>
{% endcall %}

Tabelle: Dateien eines Dokuments<br>| Datei | Inhalt |<br>| --- | --- |<br>| \_main\_.md | das Manifest: Titelseite, Kapitel und Verzeichnisse | {{ uuid('095ea144-d2fb-4fd1-98ee-6f6aa89f7686') }}

## Spaltenbreiten und Verweis {{ uuid('5ef4ecfa-eed5-4ffb-a75b-971842e8f037') }}

Eine Breite pro Spalte, in cm, mm, pt oder Prozent; die Spalten mit \* teilen sich den Rest. anchor macht die Tabelle zum Ziel eines Verweises: {{ ref('si_basiseinheiten', uuid='d7ac728b-0683-4abc-93ab-35bba7158be4') }} nennt die sieben Basiseinheiten des Internationalen Einheitensystems {{ cite('iso80000', uuid='84f9958d-8d35-41bb-bf6b-514ebe5ac6cb') }}. {{ uuid('7f741554-b803-462b-ac5a-07ac33c4b2ce') }}

{% call table('5.5cm', '3.0cm', '7.5cm', anchor='si_basiseinheiten', uuid='d43b8b45-7b50-4b71-8c6a-1c35ec0f1be5') %}
Tabelle: SI-Basiseinheiten
<table>
  <thead>
    <tr>
      <th>Grösse</th>
      <th>Einheit</th>
      <th>Zeichen</th>
    </tr>
  </thead>
  <tr>
    <td>Länge</td>
    <td>Meter</td>
    <td>m</td>
  </tr>
  <tr>
    <td>Masse</td>
    <td>Kilogramm</td>
    <td>kg</td>
  </tr>
  <tr>
    <td>Zeit</td>
    <td>Sekunde</td>
    <td>s</td>
  </tr>
  <tr>
    <td>elektrische Stromstärke</td>
    <td>Ampere</td>
    <td>A</td>
  </tr>
  <tr>
    <td>thermodynamische Temperatur</td>
    <td>Kelvin</td>
    <td>K</td>
  </tr>
  <tr>
    <td>Stoffmenge</td>
    <td>Mol</td>
    <td>mol</td>
  </tr>
  <tr>
    <td>Lichtstärke</td>
    <td>Candela</td>
    <td>cd</td>
  </tr>
</table>
{% endcall %}

{% raw %}{% call table('5.5cm', '3cm', '\*', anchor='tab_einheiten') %}{% endraw %}<br>Tabelle: SI-Basiseinheiten<br>| Grösse | Einheit | Zeichen |<br>| --- | --- | --- |<br>| Länge | Meter | m |<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('085e560a-b1dd-4219-b193-d01c5634714d') }}

## Ohne Kopfzeile, ohne Nummer {{ uuid('78da556d-bd33-4d57-a4e5-b63b3ac753e7') }}

Ohne Trennzeile ist jede Zeile eine normale Zeile. Hier steht table() als einzelne Zeile direkt vor der Tabelle; zwei feste Breiten unter 16 cm ergeben eine schmalere Tabelle: {{ uuid('582ea68f-eed8-4c5a-b752-9e85bec57ec7') }}

{% call table('4.0cm', '6.0cm', uuid='4ec677ef-7d45-4ca2-bb45-387d730ff738') %}
<table>
  <tr>
    <td>Format</td>
    <td>A4 hoch</td>
  </tr>
  <tr>
    <td>Textspalte</td>
    <td>16 cm</td>
  </tr>
  <tr>
    <td>Schrift</td>
    <td>Roboto</td>
  </tr>
</table>
{% endcall %}

Mit numbered=False steht nur der Titel über der Tabelle, ohne «Tabelle n:»: {{ uuid('ac6b0312-6428-4d1e-a470-711efdb92500') }}

{% call table('4.0cm', '12.0cm', uuid='fa98c623-c90f-4ef8-ba19-b1e63a8009de') %}
Tabelle: Seitenränder der Vorlage
<table>
  <tr>
    <td>oben</td>
    <td>35,2 mm</td>
  </tr>
  <tr>
    <td>unten</td>
    <td>23,7 mm</td>
  </tr>
</table>
{% endcall %}

{% raw %}{{ table('4cm', '6cm') }}{% endraw %}<br>| Format | A4 hoch |<br>| Textspalte | 16 cm |<br><br>{% raw %}{% call table('4cm', '\*', numbered=False) %}{% endraw %}<br>Tabelle: Seitenränder der Vorlage<br>| oben | 35,2 mm |<br>{% raw %}{% endcall %}{% endraw %} {{ uuid('e9c188ee-4cca-4ef2-bb2a-2e90eed457e3') }}
