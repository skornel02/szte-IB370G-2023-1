# Nev: Stefán Kornél
# Neptun: TFRXIL
# h:h269206
# MOTD: Ez az új másolásvédés?

def szekem(sorszam):
    sor = (sorszam - 1) // 14 + 1

    bal = (sorszam - 1) % 14 + 1 > 7
    soroldal = "bal" if bal else "jobb"

    szekszam = (sorszam - 1) % 7 + 1 
    if not bal:
        szekszam = 8 - szekszam


    szoveg = f"{sor}. sor, {soroldal} {szekszam}. szek"

    return szoveg
