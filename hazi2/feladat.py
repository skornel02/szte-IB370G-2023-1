# Nev: Stefán Kornél
# Neptun: TFRXIL
# h: h269206
# MOTD: Boldogak a sajtkészítők.

def nyertes_korok(adamPoints, enemyPoints):
    if len(adamPoints) != len(enemyPoints):
        return -1

    if len(adamPoints) == 0 or len(enemyPoints) == 0:
        return -1

    won = 0
    
    for i in range(len(adamPoints)):
        if adamPoints[i] > enemyPoints[i]:
            won += 1
    
    return won


print(nyertes_korok([30, 50, 10, 80, 100, 40], [60, 20, 10, 20, 30, 20]))
print(nyertes_korok([70, 40, 50, 80, 0], [10, 90, 100, 20]))