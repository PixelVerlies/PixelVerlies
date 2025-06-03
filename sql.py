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

def loadWinItems(data, level):
    data.cur.execute(f"""SELECT BeuteWaffen.WaffenID
                        FROM Beute JOIN BeuteWaffen ON Beute.BeuteID = BeuteWaffen.BeuteID
                        WHERE Beute.StufenID = {level}""")
    
    lis = []
    for i in data.cur:
        lis.append((i,1))

    data.cur.execute(f"""SELECT BeuteRuestungen.RuestungsID
                        FROM Beute JOIN BeuteRuestungen ON Beute.BeuteID = BeuteRuestungen.BeuteID
                        WHERE Beute.StufenID = {level}""")
    
    for i in data.cur:
        lis.append((i,2))

    return lis

def loadItems(data, charac):
    data.cur.execute(f"""SELECT CharakterWaffen.WaffenID, CharakterWaffen.CharakterID
                        FROM CharakterWaffen
                        WHERE CharakterWaffen.CharakterID = {charac.id}""")
    
    lis = []
    for i in data.cur:
        #print(i)
        it = (i,1)
        lis.append(it)

    data.cur.execute(f"""SELECT CharakterRuestungen.RuestungsID
                        FROM CharakterRuestungen
                        WHERE CharakterRuestungen.CharakterID = {charac.id}""")
    
    for i in data.cur:
        it = (i,1)
        lis.append(it)

    #print(lis)

    return lis


def saveWin(data, charac, winItem):
    if winItem[1] == 1:
        data.cur.execute(f"""INSERT INTO CharakterWaffen (CharakterID, WaffenID, Ausgeruestet)
                         VALUES ('{charac.id}', '{winItem[0][0]}', '0')""")
    elif winItem[1] == 2:
        data.cur.execute(f"""INSERT INTO CharakterRuestungen (CharakterID, RuestungsID, Ausgeruestet)
                         VALUES ('{charac.id}', '{winItem[0][0]}', '0')""")
        
    data.conn.commit()


def loadWinExpirence(data, level, ep):
    data.cur.execute(f"""SELECT Stufe.winEP, Stufe.LevelEP
                        FROM Stufe
                        WHERE Stufe.StufenID = {level}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    data.cur.execute(f"""SELECT Stufe.winEP, Stufe.LevelEP
                        FROM Stufe
                        WHERE Stufe.StufenID = {ep[1]+1}""")
    
    for i in data.cur:
        lis.append(i)

    return(lis)


def loadExpirence(data, charac):
    data.cur.execute(f"""SELECT Charakter.EP, Charakter.StufenID, Charakter.LP, Wuerfel.Seiten
                        FROM (Charakter JOIN Klassen ON Charakter.KlassenID = Klassen.KlassenID) JOIN Wuerfel ON Klassen.LPWuerfel = Wuerfel.WuerfelID
                        WHERE Charakter.CharakterID = {charac.id}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    return(lis[0])

def saveExpirence(data, charac, ep):
    data.cur.execute(f"""UPDATE Charakter 
                    SET Charakter.EP = {ep[0]}, Charakter.StufenID = {ep[1]}, Charakter.LP =  {ep[2]}
                    WHERE Charakter.CharakterID = {charac.id}""")
        
    data.conn.commit()

def saveRating(data, rod, charac):
    data.cur.execute(f"""INSERT INTO AbgeDungeon (StufenID, Runden, CharakterID)
                        VALUES ('{rod.level}', '{rod.roundNr}', '{charac.id}')""")
        
    data.conn.commit()


def loadCharacter(data, id):
    data.cur.execute(f"""SELECT Klassen.Bewegungsrate, Charakter.StufenID, Charakter.LP
                        FROM Charakter JOIN Klassen ON Charakter.KlassenID = Klassen.KlassenID
                        WHERE Charakter.CharakterID = {id}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)
    
    data.cur.execute(f"""SELECT CharakterWaffen.WaffenID, Wuerfel.Seiten
                        FROM (CharakterWaffen JOIN Waffen ON CharakterWaffen.WaffenID = Waffen.WaffenID) JOIN Wuerfel ON Waffen.WuerfelID = Wuerfel.WuerfelID
                        WHERE CharakterWaffen.CharakterID = {id}
                        AND CharakterWaffen.Ausgeruestet = 1""")
    
    for i in data.cur:
        lis.append(i)

    data.cur.execute(f"""SELECT CharakterRuestungen.RuestungsID, Ruestungen.Schutz
                        FROM CharakterRuestungen JOIN Ruestungen ON CharakterRuestungen.RuestungsID = Ruestungen.RuestungsID
                        WHERE CharakterRuestungen.CharakterID = {id}
                        AND CharakterRuestungen.Ausgeruestet = 1""")

    check = 0
    for i in data.cur:
        check += 1
        lis.append(i)

    if check == 0:
        lis.append((0, 0))

    return(lis)