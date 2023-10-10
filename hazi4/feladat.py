# Nev: StefĂĄn KornĂŠl
# Neptun: TFRXIL
# h: h269206

class Palack:
    def __init__(self, ital, max_urtartalom, jelenlegi_urtaltalom = 1):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = jelenlegi_urtaltalom

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom

    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, value):
        self._jelenlegi_urtartalom = value if value <= self.max_urtartalom else self.max_urtartalom
        if value == 0:
            self.ital = None

    def suly(self):
        return self.max_urtartalom / 35 + self.jelenlegi_urtartalom

    def __str__(self):
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self.jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

    def __eq__(self, other):
        if not isinstance(other, Palack):
            return False
        return self.ital == other.ital and self.max_urtartalom == other.max_urtartalom and self._jelenlegi_urtartalom == other._jelenlegi_urtartalom

    def __iadd__(self, other):
        if isinstance(other, Palack):
            self.jelenlegi_urtartalom = self.jelenlegi_urtartalom + other.jelenlegi_urtartalom
            if self.ital != other.ital and self.ital is not None and other.ital is not None:
                self.ital = "keverek"
            if self.ital is None:
                self.ital = other.ital

        return self

class VisszavalthatoPalack(Palack):
    def __init__(self, ital, max_urtartalom, jelenlegi_urtaltalom = 1, palackdij = 25):
        super().__init__(ital, max_urtartalom, jelenlegi_urtaltalom)
        self.palackdij = palackdij

    def __str__(self):
        return "Visszavalthato" + super().__str__()


class Rekesz:
    def __init__(self, max_teherbiras):
        self.max_teherbiras = max_teherbiras
        self.palackok = []

    def suly(self):
        suly = 0

        for palack in self.palackok:
            suly += palack.suly()

        return suly

    def uj_palack(self, palack):
        if self.suly() + palack.suly() <= self.max_teherbiras:
            self.palackok.append(palack)

    def osszes_penz(self):
        osszesdij = 0

        for palack in self.palackok:
            if isinstance(palack, VisszavalthatoPalack):
                osszesdij += palack.palackdij

        return osszesdij