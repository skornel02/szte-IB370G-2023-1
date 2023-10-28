def read_file(filename: str) -> list[list[str]]:
    with open(filename, "r", encoding="utf8") as f:
        lines = 0
        adatok = []
        while line := f.readline():
            if lines == 0:
                lines += 1
                continue
            adatok.append([data.strip() for data in line.strip().split(",")])
        return adatok

def write_file(filename: str, lines: list[str], mode: str = "w") -> None:
    with open(filename, mode, encoding="utf8") as f:
        for line in lines:
            f.write(line + "\n")

# with
# with
# with
# with
# with
# with
# with
# with

def legnagyobb_stadion(filename: str) -> None:
    data = read_file(filename)
    if len(data) == 0:
        write_file("legnagyobb.txt", ["Nincs (Nincs)"])
        return

    legnagyobb = data[0]
    for sor in data:
        if int(sor[4]) > int(legnagyobb[4]):
            legnagyobb = sor

    if int(legnagyobb[4]) == 0:
        write_file("legnagyobb.txt", ["Nincs (Nincs)"])
        return

    print(f"A legnagyobb stadion: {legnagyobb[3]} ({legnagyobb[2]})")
    write_file("legnagyobb.txt", [f"{legnagyobb[3]} ({legnagyobb[2]})"])

def osszes_arena(filename: str) -> None:
    data = read_file(filename)
    arenak = ["Stadium,City,Country,Big"]

    for sor in data:
        if sor[3].endswith("Arena"):
            big = "True" if int(sor[4]) > 50000 else "False"
            arenak.append(f"{sor[3]},{sor[2]},{sor[7]},{big}")

    write_file("arena_park.csv", arenak)

def osszes_park(filename: str) -> None:
    data = read_file(filename)
    arenak = []

    for sor in data:
        if sor[3].endswith("Park"):
            big = "True" if int(sor[4]) > 20000 else "False"
            arenak.append(f"{sor[3]},{sor[2]},{sor[7]},{big}")

    write_file("arena_park.csv", arenak, "a")

def varosok_szama(filename: str, *orszagok: list[str]) -> None:
    if len(orszagok) == 0:
        raise Exception("Nincs megadva egy orszag sem!")

    data = read_file(filename)
    orszagStat = {}
    for orszag in orszagok:
        orszagStat[orszag] = []

    for sor in data:
        if sor[7] in orszagok:
            orszagStat[sor[7]].append(sor[2])



    output = []
    for orszag in orszagok:
        orszagStat[orszag].sort()

        output.append(f"{orszag} varosai:")
        for varos in orszagStat[orszag]:
            output.append(f"\t{varos}")
        output.append("-" * 10)
        
    write_file("varosok.txt", output)

#legnagyobb_stadion("stadium.csv")
#osszes_arena("stadium.csv")
#osszes_park("stadium.csv")
#varosok_szama("stadium.csv", "Germany", "Spain", "Hungary")