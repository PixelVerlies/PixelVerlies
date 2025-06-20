from database import database

# Globale Datenbankinstanz
db = database()

def LoginDB(username, password): #Login Daten prüfen
    db.connection()
    db.cur.execute(f"""SELECT SpielerID, Benutzername, Passwort
                   FROM Spieler
                   WHERE BINARY Benutzername like '{username}' AND BINARY Passwort like '{password}'""")#Binary für groß/klein Schreibung
    
    result = db.cur.fetchone()
    if result:
        return result[0]  # Gibt die SpielerID zurück, wenn Login erfolgreich
    else:
        return None  # Gibt None zurück, wenn Login fehlschlägt

def username(username): #Holt gleichen Benutzername
    db.connection()
    db.cur.execute(f"""SELECT Benutzername
                   FROM Spieler
                   WHERE BINARY Benutzername like '{username}'""")
    
    result = db.cur.fetchone()
    return result is not None

def registrierDB(username, password): #Speichert den neuen Spieler
    db.connection()
    db.cur.execute(f"""INSERT INTO `Spieler` (`Benutzername`, `Passwort`)
                   VALUES ('{username}', '{password}')""")
    
    db.conn.commit()


def CharakterMenuDB(spieler_id): #Holt Daten von Charakter und der Klasse für den Spieler
    db.connection()
    db.cur.execute(f"""
        SELECT c.CharakterID, c.Name, k.KlassenName, c.StufenID
        FROM Charakter c
        JOIN Klassen k ON c.KlassenID = k.KlassenID
        WHERE c.SpielerID = {spieler_id}
    """)
    return db.cur.fetchall()

def KlassenMenuDB(): #Holt Daten für die Klassen Auswhal
    db.connection()
    db.cur.execute(f"""
        SELECT Klassen.KlassenName, Wuerfel.Seiten, Klassen.Bewegungsrate, Klassen.KlassenID
        FROM Klassen JOIN Wuerfel ON Klassen.LPWuerfel = Wuerfel.WuerfelID
    """)
    return db.cur.fetchall()

def get_character_details(character_id): #Holt einige Daten für den Character_Screen, Joint die Tabellen nach Notwenigkeit
    db.connection()
    db.cur.execute(f"""
        SELECT
            c.Name,
            k.KlassenName,
            c.LP,
            c.StufenID,
            k.Bewegungsrate,
            w.Beschreibung AS AusgeruesteteWaffeBeschreibung,
            wurf.Seiten AS WaffenSchadenWuerfel,
            r.Beschreibung,
            r.Schutz
        FROM Charakter c
        JOIN Klassen k ON c.KlassenID = k.KlassenID
        LEFT JOIN CharakterWaffen cw ON c.CharakterID = cw.CharakterID AND cw.Ausgeruestet = 1
        LEFT JOIN Waffen w ON cw.WaffenID = w.WaffenID
        LEFT JOIN Wuerfel wurf ON w.WuerfelID = wurf.WuerfelID
        LEFT JOIN CharakterRuestungen cr ON c.CharakterID = cr.CharakterID AND cr.Ausgeruestet = 1
        LEFT JOIN Ruestungen r ON cr.RuestungsID = r.RuestungsID  
        WHERE c.CharakterID = {character_id}
    """)
    return db.cur.fetchone()

def get_character_potions(character_id): #Holt Heiltränke die der Charakter hat
    db.connection()
    db.cur.execute(f"""
        SELECT h.Beschreibung, ch.Anzahl
        FROM CharakterHeiltraenke ch
        JOIN Heiltraenke h ON ch.HeiltrankID = h.HeilID
        WHERE ch.CharakterID = {character_id}
    """)
    return db.cur.fetchall()

def get_character_weapons(character_id): # Holt Waffen die der Charakter hat
    db.connection()
    db.cur.execute(f"""
        SELECT w.WaffenID, w.Beschreibung, wurf.Seiten AS Schaden, cw.Ausgeruestet
        FROM CharakterWaffen cw
        JOIN Waffen w ON cw.WaffenID = w.WaffenID
        JOIN Wuerfel wurf ON w.WuerfelID = wurf.WuerfelID
        WHERE cw.CharakterID = {character_id}
    """)
    return db.cur.fetchall()

def create_character(name, klassen_id, spieler_id): #Neuen Charakter anlegen
    db.connection()
    try: #die Daten holen für die LP
        db.cur.execute(f"SELECT Wuerfel.Seiten FROM Klassen JOIN Wuerfel ON Klassen.LPWuerfel = Wuerfel.WuerfelID WHERE KlassenID = {klassen_id}")
        lp_wuerfel = db.cur.fetchone()[0]
        #Speichert neuen Charakter, mit eingebenen daten, dazu 0 EP und Stufe 1
        db.cur.execute(f"""
            INSERT INTO Charakter (KlassenID, Name, SpielerID, LP, EP, StufenID)
            VALUES ({klassen_id}, '{name}', {spieler_id}, {lp_wuerfel}, 0, 1)
        """)
        character_id = db.cur.lastrowid
        #Speichert zu dem Charakter die Standard Waffe Faust mit dazu
        db.cur.execute(f"""
            INSERT INTO CharakterWaffen (CharakterID, WaffenID, Ausgeruestet)
            VALUES ({character_id}, 7, 1)
        """)
        #Speichert zu dem Charakter die Standard Rüstung mit dazu
        db.cur.execute(f"""
            INSERT INTO CharakterRuestungen (CharakterID, RuestungsID, Ausgeruestet)
            VALUES ({character_id}, 6, 1)
        """)

        #Heiltränke am anfang zur auswahl.(3 Kleine, zwei mittlere und ei Großen)
        db.cur.execute("SELECT HeilID FROM Heiltraenke")
        heal_potion_ids = db.cur.fetchall()
        counter = 1
        for heal_id in heal_potion_ids:
            db.cur.execute(f"""
                INSERT INTO CharakterHeiltraenke (CharakterID, HeiltrankID, Anzahl)
                VALUES ({character_id}, {heal_id[0]}, {counter})
            """)
            counter +=1

        db.conn.commit()
        return True
    except Exception as e:
        print(f"Fehler beim Erstellen des Charakters: {e}")
        db.conn.rollback()
        return False

def update_character_name(character_id, new_name): #Ändert den Namen des Charakters
    db.connection()
    db.cur.execute(f"""
        UPDATE Charakter
        SET Name = '{new_name}'
        WHERE CharakterID = {character_id}
    """)
    db.conn.commit()

def unequip_all_weapons(character_id): #Ändert, dass keine Waffe ausgerüstet ist
    db.connection()
    db.cur.execute(f"""
        UPDATE CharakterWaffen
        SET Ausgeruestet = 0
        WHERE CharakterID = {character_id}
    """)
    db.conn.commit()

def equip_weapon(character_id, weapon_id): #Ändert, dass die ausgewählte Waffe ausgerüstet ist
    db.connection()
    db.cur.execute(f"""
        UPDATE CharakterWaffen
        SET Ausgeruestet = 1
        WHERE CharakterID = {character_id} AND WaffenID = {weapon_id}
    """)
    db.conn.commit()

def check_character_name_exists_for_player(name, spieler_id, exclude_character_id=None): # Zählt alle Charaktere, des Spielers
    db.connection()
    query = ""
    if exclude_character_id:
        query += f" AND CharakterID != {exclude_character_id}"
    db.cur.execute(f"""
        SELECT COUNT(*)
        FROM Charakter
        WHERE BINARY Name = '{name}' AND SpielerID = {spieler_id}
    """ + query)
    
    result = db.cur.fetchone()[0]
    return result > 0


def loadEnemie(enemieID, data):
    #Holt alle Daten für die Gegner
    data.cur.execute(f"""SELECT Gegner.Name, Gegner.LP, Gegner.GegnerID, Wuerfel.seiten
                        FROM Gegner JOIN Wuerfel ON Gegner.wuerfelID = Wuerfel.wuerfelID
                        WHERE GegnerID = {enemieID}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    return lis[0]

def loadHealingPotion(data, charac):
    #Holt alle Heiltränke des Charakters
    data.cur.execute(f"""SELECT Heiltraenke.Beschreibung, Heiltraenke.Heilung, CharakterHeiltraenke.Anzahl, Heiltraenke.HeilID
                        FROM Heiltraenke JOIN CharakterHeiltraenke ON Heiltraenke.HeilID = CharakterHeiltraenke.HeiltrankID
                        WHERE CharakterHeiltraenke.CharakterID = {charac.id}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    return lis

def loadWinItems(data, level):
    #Holt alle möglichen Waffen Gewinne
    data.cur.execute(f"""SELECT BeuteWaffen.WaffenID, BeuteWaffen.BeuteID
                        FROM Beute JOIN BeuteWaffen ON Beute.BeuteID = BeuteWaffen.BeuteID
                        WHERE Beute.StufenID = {level}""")
    
    lis = []
    for i in data.cur:
        lis.append((i[0],1))

    #Holt alle möglichen Rüstungs Gewinne
    data.cur.execute(f"""SELECT BeuteRuestungen.RuestungsID, BeuteRuestungen.BeuteID
                        FROM Beute JOIN BeuteRuestungen ON Beute.BeuteID = BeuteRuestungen.BeuteID
                        WHERE Beute.StufenID = {level}""")
    
    for i in data.cur:
        lis.append((i[0],2))

    return lis

def loadItems(data, charac):
    #Holt alle Waffen des Charakters
    data.cur.execute(f"""SELECT CharakterWaffen.WaffenID, CharakterWaffen.CharakterID
                        FROM CharakterWaffen
                        WHERE CharakterWaffen.CharakterID = {charac.id}""")
    
    lis = []
    for i in data.cur:
        it = (i[0],1)
        lis.append(it)

    #Holt alle Rüstungen des Charakters
    data.cur.execute(f"""SELECT CharakterRuestungen.RuestungsID, CharakterRuestungen.CharakterID
                        FROM CharakterRuestungen
                        WHERE CharakterRuestungen.CharakterID = {charac.id}""")
    
    for i in data.cur:
        it = (i[0],2)
        lis.append(it)

    return lis


def saveWin(data, charac, winItem):
    #Speichert den Gewinn des Charakters
    if winItem[1] == 1:
        data.cur.execute(f"""INSERT INTO CharakterWaffen (CharakterID, WaffenID, Ausgeruestet)
                         VALUES ('{charac.id}', '{winItem[0]}', '0')""")
    elif winItem[1] == 2:
        data.cur.execute(f"""INSERT INTO CharakterRuestungen (CharakterID, RuestungsID, Ausgeruestet)
                         VALUES ('{charac.id}', '{winItem[0]}', '0')""")
        
    data.conn.commit()


def loadWinExpirence(data, level, ep):
    #Holt die Gewinn EP zu dem passenden Dungeon
    data.cur.execute(f"""SELECT Stufe.winEP, Stufe.LevelEP
                        FROM Stufe
                        WHERE Stufe.StufenID = {level}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    #Holt die EP Daten für das nächste Level
    data.cur.execute(f"""SELECT Stufe.winEP, Stufe.LevelEP
                        FROM Stufe
                        WHERE Stufe.StufenID = {ep[1]+1}""")
    
    for i in data.cur:
        lis.append(i)

    return(lis)


def loadExpirence(data, charac):
    #Holt die EP, die Stufe und die LP des Charakters
    data.cur.execute(f"""SELECT Charakter.EP, Charakter.StufenID, Charakter.LP, Wuerfel.Seiten
                        FROM (Charakter JOIN Klassen ON Charakter.KlassenID = Klassen.KlassenID) JOIN Wuerfel ON Klassen.LPWuerfel = Wuerfel.WuerfelID
                        WHERE Charakter.CharakterID = {charac.id}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    return(lis[0])

def saveExpirence(data, charac, ep):
    #Speichert die EP, die Stufe und die LP des Charakters
    data.cur.execute(f"""UPDATE Charakter 
                    SET Charakter.EP = {ep[0]}, Charakter.StufenID = {ep[1]}, Charakter.LP =  {ep[2]}
                    WHERE Charakter.CharakterID = {charac.id}""")
        
    data.conn.commit()

def saveRating(data, rod, charac):
    #Speichert abgeschlossene Dungeon
    data.cur.execute(f"""INSERT INTO AbgeDungeon (StufenID, Runden, CharakterID)
                        VALUES ('{rod.level}', '{rod.roundNr}', '{charac.id}')""")
        
    data.conn.commit()


def loadCharacter(data, id):
    #Holt die Daten des Charakters
    data.cur.execute(f"""SELECT Klassen.Bewegungsrate, Charakter.StufenID, Charakter.LP, Charakter.KlassenID
                        FROM Charakter JOIN Klassen ON Charakter.KlassenID = Klassen.KlassenID
                        WHERE Charakter.CharakterID = {id}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)
    
    #Holt die ausgerüstete Waffe des Charakters
    data.cur.execute(f"""SELECT CharakterWaffen.WaffenID, Wuerfel.Seiten
                        FROM (CharakterWaffen JOIN Waffen ON CharakterWaffen.WaffenID = Waffen.WaffenID) JOIN Wuerfel ON Waffen.WuerfelID = Wuerfel.WuerfelID
                        WHERE CharakterWaffen.CharakterID = {id}
                        AND CharakterWaffen.Ausgeruestet = 1""")
    
    for i in data.cur:
        lis.append(i)

    #Holt die ausgerüstete Rüstung des Charakters
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

def loadClass(data, id):
    #Holt die KlassenID des Charakters
    data.cur.execute(f"""SELECT Charakter.KlassenID
                        FROM Charakter
                        WHERE Charakter.CharakterID = {id}""")
    
    lis = []
    for i in data.cur:
        lis.append(i)

    return(lis[0])

def LevelMenuDB(): # Holt die Stufen für DIe Level Auswahl Tabelle
    db.connection()
    db.cur.execute(f"""
        SELECT 'Schwierigkeits-Level',`StufenID`
        FROM `Stufe`
    """)
    return db.cur.fetchall()

def count_characters_for_player(player_id): # zählt charaktere die der spieler hat, für die maximale Anzahl
    db.connection()
    db.cur.execute(F"""SELECT COUNT(*) 
                   FROM Charakter 
                   WHERE SpielerID = {player_id}""")
    count = db.cur.fetchone()[0]
    return count

def get_character_rustung(character_id): # Holt Rüstung Tabelle für Character_screen
    db.connection()
    db.cur.execute(f"""
        SELECT cr.RuestungsID, r.Beschreibung, r.Schutz , cr.Ausgeruestet
        FROM CharakterRuestungen cr
        JOIN Ruestungen r ON cr.RuestungsID = r.RuestungsID
		WHERE cr.CharakterID = {character_id}
    """)
    return db.cur.fetchall()

def unequip_all_rustung(character_id): #Änderung alle Rüstungen auf 0, also nicht ausgerüstet setzen
    db.connection()
    db.cur.execute(f"""
        UPDATE CharakterRuestungen
        SET Ausgeruestet = 0
        WHERE CharakterID = {character_id}
    """)
    db.conn.commit()

def equip_rustung(character_id, rustung_id): # Ausgewählte Rustung auf Ausgerüstet setzten
    db.connection()
    db.cur.execute(f"""
        UPDATE CharakterRuestungen
        SET Ausgeruestet = 1
        WHERE CharakterID = {character_id} AND RuestungsID = {rustung_id}
    """)
    db.conn.commit()