from database import database

def loadEnemie(enemieID):
    data = database()
    data.connection()

    data.cur.execute(f"""SELECT gegner.Name, gegner.LP, gegner.bewegungsrate, gegner.GegnerID, wuerfel.seiten
                        FROM gegner JOIN wuerfel ON gegner.wuerfelID = wuerfel.wuerfelID
                        WHERE gegnerID = {enemieID}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)
    
    data.connClose()
    return lis
    