# Nev: Stefán Kornél
# Neptun: TFRXIL
# h: h269206

def n_grammer(text: str, n: int = 3) -> list[int]:
    pieces = len(text) // n
    szamok = []

    for i in range(pieces + 1):
        start = 0 + i * n
        end = start + n
        if end > len(text):
            text += "0" * (end - len(text))
        substr = text[start:end]
        print(substr)
        szamok.append(int(substr))

    if szamok[-1] == 0:
        szamok.pop()

    return szamok

class Matematikus:

    def __init__(self, nev, kedvenc_hossz = 3) -> None:
        self.nev = nev
        self.kedvenc_hossz = kedvenc_hossz
        self.tanulmanyok = {}
    
    @property
    def nev(self):
        return self._nev
    
    @nev.setter
    def nev(self, value):
        if isinstance(value, str):
            self._nev = value

    def tanulmanyt_felvesz(self, szamok: list[int]):
        same = True
        length = len(str(szamok[0]))

        for szam in szamok[1:]:
            curlen = len(str(szam))
            if curlen != length:
                same = False

        if same and length == self.kedvenc_hossz:
            self.tanulmanyok[self.kedvenc_hossz] = szamok
        elif same:
            self.kedvenc_hossz = length
        else:
            raise ValueError("Csunya szamok")

    def __lt__(self, other) -> bool:
        if isinstance(other, Matematikus):
            return self.kedvenc_hossz < other.kedvenc_hossz
        return False

    def __str__(self):
        return f"A {self.nev} nevu matematikus kedvenc szam hossza {self.kedvenc_hossz}, es {len(self.tanulmanyok.keys())} tanulmanyban vett reszt."

print(n_grammer("125175329812574521", 4))
print(n_grammer("121117532981", 2))
