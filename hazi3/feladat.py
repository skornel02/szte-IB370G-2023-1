# Nev: StefĂĄn KornĂŠl
# Neptun: TFRXIL
# h: h269206

def hogolyo_csata(korok):
    osszesitett = {}

    for players in korok:
        for player in players.keys():
            if player in osszesitett.keys():
                osszesitett[player]['eldobott_hogolyok'] += players[player][
                    'eldobott_hogolyok'] if 'eldobott_hogolyok' in players[player].keys() else 0
                osszesitett[player]['talalt'] += players[player][
                    'talalt'] if 'talalt' in players[player].keys() else 0
                osszesitett[player]['fejtalalat'] += players[player][
                    'fejtalalat'] if 'fejtalalat' in players[player].keys() else 0
            else:
                osszesitett[player] = {
                    'eldobott_hogolyok': players[player]['eldobott_hogolyok'] if 'eldobott_hogolyok' in players[player].keys() else 0,
                    'talalt': players[player]['talalt'] if 'talalt' in players[player].keys() else 0,
                    'fejtalalat': players[player]['fejtalalat'] if 'fejtalalat' in players[player].keys() else 0,
                }

    return osszesitett

def hogolyo_pontossag(players):
    stats = players.copy()
    for player in players:
        if stats[player]['eldobott_hogolyok'] > 0:
            stats[player]['pontossag'] = stats[player]['talalt'] / stats[player]['eldobott_hogolyok']
        else:
            stats[player]['pontossag'] = 0

    return players

def hogolyo_piros_lap(playersWithStat):
    playersToBan = []

    for player in playersWithStat:
        if playersWithStat[player]['pontossag'] >= 0.7 and (playersWithStat[player]['fejtalalat'] / playersWithStat[player]['talalt']) > 0.5:
            playersToBan.append(player)

    return playersToBan

adat = [
{
'Tamas': {
'eldobott_hogolyok': 4,
'talalt': 1
},
'Ferenc': {
'eldobott_hogolyok': 16,
'talalt': 6,
'fejtalalat': 1
},
'Csaba': {
'eldobott_hogolyok': 28,
}
},
{
'Tamas': {
'eldobott_hogolyok': 2,
'talalt': 2
},
'Ferenc': {
'eldobott_hogolyok': 3,
'talalt': 2,
'fejtalalat': 1
},
'Csaba': {
'eldobott_hogolyok': 4,
'talalt': 2,
'fejtalalat': 1
}
}
]

stat = hogolyo_csata(adat)
print("Stat")
print(stat)

acc = hogolyo_pontossag(stat)
print("Acc")
print(acc)

banStat = {
"Geza": {
"eldobott_hogolyok": 14,
"talalt": 4,
"fejtalalat": 0,
"pontossag": 0.2857142857142857
},
"Lajos": {
"eldobott_hogolyok": 45,
"talalt": 36,
"fejtalalat": 22,
"pontossag": 0.8
},
"Jozsef": {
"eldobott_hogolyok": 37,
"talalt": 29,
"fejtalalat": 15,
"pontossag": 0.7837837837837838
}
}

toBan = hogolyo_piros_lap(banStat)
print("Bann")
print(toBan)