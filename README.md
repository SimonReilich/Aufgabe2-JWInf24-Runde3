# Aufgabe 2 - Texthopsen

# Lösungsidee

Das Spiel wird simuliert. Es werden nur Buchstaben des lateinischen Alphabets betrachtet, Umlaute werden umgewandelt (”ä” zu “ae”, “ö” zu “oe”, “ü” zu “ue”), aus “ß” wird “ss”.

# Umsetzung

## Algorithmus

*Die Lösungsidee wurde in Python umgesetzt, auf die Dokumentation des Einlesens der Daten wird verzichtet*

Zuerst wird der Benutzer aufgefordert, den Pfad zu einer Textdatei anzugeben. Für die Beispiele recht es, die Nummer anzugeben (also statt “hopsen1.txt” nur “1”). Beim einlesen der Datei ist es auch wichtig, beim Einlesen der Dateien das korrekte Encoding anzugeben (hier: UTF-8), da Sonderzeichen sonst falsch eingelesen werden.

Die Liste von Zeilen der Eingabedatei, die `file.readlines()` zurückgibt wird in ihre String-representation umgewandelt (dies ist möglich, da “[”, “]”, “,” und “’” keine Buchstaben sind und später sowieso nicht beachtet werden).

Ein Wörterbuch `special_char_map` wird erstellt, um Umlaute durch ihre entsprechenden Buchstabenkombinationen zu ersetzen (z.B. 'ä' wird zu 'ae'), Der gesamte Text wird in Kleinbuchstaben umgewandelt und alle Zeichen außer Kleinbuchstaben entfernt.

Zwei Variablen, `a` und `b` repräsentieren die Positionen der Spieler Amira und Bella, die Variable `i` zählt die Runden. Bei jedem Durchgang der `while` Schleife wird zunächst `b` wird um den Wert des Buchstabens an der Position `b` erhöht. Falls die Position `b` außerhalb des Textes liegt wird abgebrochen. Ansonsten geschieht das selbe für `a` (Es ist wichtig, Bella zuerst zu simulieren, da sie im echten Spiel ebenfalls beginnt, andernfalls kann es zu falschen Ergebnissen kommen).

Der Gewinner und die Anzahl der Runden werden ausgegeben.

# Beispiele

## Beispiel 1

<aside>
📥

Eine Schildkröte wurde wegen ihrer Langsamkeit von einem Hasen verspottet. Trotzdem wagte sie es, den Hasen zum Wettrennen herauszufordern. Der Hase ließ sich mehr aus Scherz als aus Prahlerei darauf ein. Es kam der Tag, an dem der Wettlauf stattfinden sollte. Das Ziel wurde festgelegt und beide betraten im gleichen Augenblick die Laufbahn.

Die Schildkröte kroch langsam und unermüdlich. Der Hase dagegen legte sich mit mächtigen Sprüngen gleich ins Zeug, wollte er den Spott für die Schildkröte doch auf die Spitze treiben. Als der Hase nur noch wenige Schritte vom Ziel entfernt war, setzte er sich schnaufend ins Gras und schlief kurz darauf ein. Die großen, weiten Sprünge hatten ihn nämlich müde gemacht.

Doch plötzlich wurde der Hase vom Jubel der Zuschauer geweckt, denn die Schildkröte hatte gerade das Ziel erreicht und gewonnen.

Der Hase musste zugeben, dass das Vertrauen in seine Schnelligkeit ihn so leichtsinnig gemacht hatte, dass sogar ein langsames Kriechtier ihn mit Ausdauer besiegen konnte.

</aside>

<aside>
📤

Amira hat nach 79 Runden gewonnen!

</aside>

## Beispiel 2

<aside>
📥

Ein Federchen flog durch das Land;

Ein Nilpferd schlummerte im Sand.

Die Feder sprach: "Ich will es wecken!"

Sie liebte, andere zu necken.

Aufs Nilpferd setzte sich die Feder

Und streichelte sein dickes Leder.

Das Nilpferd sperrte auf den Rachen

Und musste ungeheuer lachen.

</aside>

<aside>
📤

Bella hat nach 20 runden gewonnen!

</aside>

## Beispiel 3

<aside>
📥

Koukonisi ist eine kleine, nicht bewohnte griechische Insel im Golf von Moudros der Insel Limnos. Diese Insel liegt nördlich von Moudros und gehört zu dessen Gemeindebezirk. Koukonisi ist über eine befestigte Straße von der etwa 400m entfernten Küste zu erreichen.

</aside>

<aside>
📤

Amira hat nach 18 Runden gewonnen!

</aside>

## Beispiel 4

<aside>
📥

128 Zeichen umfasst das ASCII-System und stellt damit eine simple, aber effektive Möglichkeit dar, Texte digital zu codieren. Jeder Buchstabe des lateinischen Alphabets sowie grundlegende Satzzeichen und Zahlen sind darin enthalten. Diese Beschränkung auf 128 Zeichen machte ASCII besonders für frühe Computer attraktiv, da Speicherplatz sehr knapp war. Auch wenn moderne Systeme komplexere Codierungen nutzen, bleibt ASCII in vielen Bereichen relevant.

</aside>

<aside>
📤

Bella hat nach 31 runden gewonnen!

</aside>

## Beispiel 5

<aside>
📥

Vor einem großen Wald wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; die beiden Kinder hießen Hänsel und Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun des Abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll nun aus uns werden? Wie können wir unsere armen Kinder ernähren trotz dass wir für uns selbst nichts mehr haben?" - "Weißt du was," antwortete die Frau, "wir wollen morgen früh die Kinder hinaus in den Wald führen, wo er am dicksten ist. Da machen wir ihnen ein Feuer an und geben jedem noch ein Stückchen Brot, dann gehen wir an unsere Arbeit und lassen sie allein. Sie finden den Weg nicht wieder nach Haus, und wir sind sie los." - "Nein," sagte der Mann, "das tue ich nicht; wie sollt ich's übers Herz bringen, meine Kinder im Walde allein zu lassen! Die wilden Tiere würden bald kommen und sie zerreißen." - "Oh, du Narr," sagte sie, "dann müssen wir alle vier verhungern, du kannst nur die Bretter für die Särge hobeln," und ließ ihm keine Ruhe, bis er einwilligte. "Aber die armen Kinder dauern mich doch," sagte der Mann.

Die zwei Kinder hatten vor Hunger auch nicht einschlafen können und hatten gehört, was die Stiefmutter zum Vater gesagt hatte. Gretel weinte bittere Tränen und sprach zu Hänsel: "Nun ist's um uns geschehen." - "Sei still, Gretel," sprach Hänsel, "gräme dich nicht, ich will uns schon helfen." Und als die Alten eingeschlafen waren, stand er auf, zog sein Röcklein an, machte die Türe auf und schlich sich hinaus. Da schien der Mond ganz hell, und die Kieselsteine, die vor dem Haus lagen, glänzten wie lauter Batzen. Hänsel bückte sich und steckte so viele Steine in sein Rocktäschlein, als nur hinein wollten. Dann ging er wieder zurück, sprach zu Gretel: "Sei getrost, liebe Schwester, und schlaf nur ruhig ein, Gott wird uns nicht verlassen," und legte sich wieder in sein Bett.

… [Aus Gründen der Übersichtlichkeit gekürzt]

</aside>

<aside>
📤

Bella hat nach 991 runden gewonnen!

</aside>

# Quellcode

```python
def int_from_char(character):
    return ord(character) - ord("a") + 1

file_name = input("""Please provide the path of the .txt-file 
		containing the input: """)
if file_name == "1" or file_name == "2" or file_name == "3" or file_name == "4" 
		or file_name == "5":
    file_name = f"hopsen{file_name}.txt"
file = open(file_name, encoding="UTF-8")

special_char_map = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}
raw_text = str(file.readlines())
text = "".join(e for e in raw_text.lower().translate(special_char_map) 
				if ord("a") <= ord(e) <= ord("z"))

a = 1
b = 0
i = 0

while a < len(text) and b < len(text):
    i += 1
    b += int_from_char(text[b])
    if b >= len(text):
        print(f"Bella hat nach {i} runden gewonnen!")
        break
    a += int_from_char(text[a])
    if a >= len(text):
        print(f"Amira hat nach {i} Runden gewonnen!")
        break

```