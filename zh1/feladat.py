# Nev: Vezeteknev Keresztnev
# Neptun: NEP4LF
# h: h123456

def borfesztival(text: 'str'):
    if not isinstance(text, str) or len(text) == 0:
        return -1

    stats = {
        'Vörösbor': 0,
        'Fehérbor': 0,
        'Szóda': 0,
        'Összérték': 0
        }

    names = [name.strip().lower() for name in text.split(';')]
    for name in names:
        if name == "gábor":
            stats["Vörösbor"] += 12
            stats["Szóda"] += 1

        elif name == "marci":
            stats["Fehérbor"] += 6

        elif name == "istván":
            stats["Fehérbor"] += 8
            stats["Szóda"] += 2

    stats["Összérték"] = stats["Vörösbor"] * 4500 + stats["Fehérbor"] * 3000 + stats["Szóda"] * 350
    stats["Összérték"] -= (stats["Fehérbor"] // 5) * 3000

    return stats


class ValorantUgynok:
    def __init__(self, nev: 'str', tamadas: 'int' = 10) -> None:
        super().__init__()
        self.nev = nev
        self._tamadas = tamadas
        self.hp = 100
        self.kepessegek = []

    @property
    def tamadas(self):
        return self._tamadas

    @tamadas.setter
    def tamadas(self, value):
        if not isinstance(value, int) or 100 < value or value < 0:
            self._tamadas = 10
        else:
            self._tamadas = value

    def kepesseg_hozzaadas(self, kepesseg):
        if not isinstance(kepesseg, str):
            raise ValueError('Érvénytelen képesség')

        kodolt = ""
        for i in range(0, len(kepesseg), 2):
            kodolt += kepesseg[i]

        print(kodolt)

        self.kepessegek.append(kodolt)

    def kepesseg_torles(self, kepesseg):
        if not isinstance(kepesseg, str):
            raise ValueError('Érvénytelen képesség')

        kodolt = ""

        for i in range(0, len(kepesseg), 2):
            kodolt += kepesseg[i]

        if kodolt in self.kepessegek:
            self.kepessegek.remove(kodolt)

    def __lt__(self, other):
        if not isinstance(other, ValorantUgynok):
            raise ValueError('Nem ugynok')

        return self.tamadas < other.tamadas

    def __str__(self):
        return f"Az ügynök neve: {self.nev}, támadása: {self.tamadas}, HP: {self.hp}, és {len(self.kepessegek)} képessége van."

    def __add__(self, other) -> 'ValorantUgynok':
        if not isinstance(self, ValorantUgynok) or not isinstance(other, ValorantUgynok):
            raise TypeError('Nem ügynököt adtál meg!')

        ugynok = ValorantUgynok(self.nev, max(self.tamadas, other.tamadas))
        ugynok.hp = max(self.hp, other.hp)

        for kepesseg in self.kepessegek:
            ugynok.kepessegek.append(kepesseg)
        for kepesseg in other.kepessegek:
            ugynok.kepessegek.append(kepesseg)

        return ugynok

res = borfesztival("GÁBor; mARci;István;István;Gábor ;Marci;Marci;gábor;Gábor;ISTván")
print(res)

myval = ValorantUgynok("sajt", 14)
myval.kepesseg_hozzaadas("123456789")
print(myval)