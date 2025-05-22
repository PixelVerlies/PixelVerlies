from database import database

def loadEnemie(enemieID, data):
    data.cur.execute(f"""SELECT Gegner.Name, Gegner.LP, Gegner.GegnerID, Wuerfel.seiten
                        FROM Gegner JOIN Wuerfel ON Gegner.wuerfelID = Wuerfel.wuerfelID
                        WHERE GegnerID = {enemieID}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    return lis[0]

def loadHealingPotion(data, charac):
    data.cur.execute(f"""SELECT Heiltraenke.Beschreibung, Heiltraenke.Heilung, CharakterHeiltraenke.Anzahl, Heiltraenke.HeilID
                        FROM Heiltraenke JOIN CharakterHeiltraenke ON Heiltraenke.HeilID = CharakterHeiltraenke.HeiltrankID
                        WHERE CharakterHeiltraenke.CharakterID = {charac.id}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    return lis
