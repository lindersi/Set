# Set-Ermittlung. Start 13.5.2022 mit händischer Eingabe des Sets in der Konsole.

from itertools import combinations


def get_set_prompt():
    print("Bitte Kartenset eingeben (oder mit 'a' automatisch Kartenset generieren).\n"
          "Beispiel für eine Karte: 'r2sn'.\n"
          "1. Stelle: Farbe r (Rot), g (Grün), v (Violett)\n"
          "2. Stelle: Anzahl 1, 2, 3\n"
          "3. Stelle: Füllung v (voll), s (schraffiert), l (leer)\n"
          "4. Stelle: Form o (Oval), r (Raute), n (Nüssli)\n"
          "OK - 9 oder 12 Karten kommagetrennt eingeben:")
    cardset = input()  # z.B. v1sn, r2vo, g1vn, v1lo, v1so, v1ln, r2sn, r3vo, g3vn
    while True:
        if cardset == "a":
            cardset = "v1sn, r2vo, g1vn, v1lo, v1so, v1ln, r2sn, r3vo, g3vn, g2vr, v3ln, g3vr"
        cardlist = cardset.replace(' ', '').split(',')
        if len(cardlist) != 9 and len(cardlist) != 12:
            cardset = input("Das waren nicht 9 oder 12 Karten. Nächster Versuch:")
        else:
            break
    i = 0
    newlist = []
    for card in cardlist:
        newlist.append(tuple(card + hex(i+1)[-1]))  # Jede Karte ein Tuple mit Nummer (Reihenfolge der Input list)
        i += 1
    return newlist


def check_set(cards):
    result = []
    for testset in combinations(cards, 3):
        hit = False
        for i in range(0, 4):
            if testset[0][i] == testset[1][i] == testset[2][i]:
                hit = True
            elif testset[0][i] != testset[1][i] != testset[2][i] != testset[0][i]:
                hit = True
            else:
                hit = False
                break
        if hit:
            result.append(testset)
            print(testset)
    return result


if __name__ == '__main__':
    getset = get_set_prompt()
    # getset = get_set_vision()
    check_set(getset)
