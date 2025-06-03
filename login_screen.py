import pygame
import textFunctions
import grid
import sql
import hashlib
import sys

def create_login_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Titel "ANMELDUNG"
    texfield_list.append(textFunctions.textField("ANMELDUNG", 14, 3, ueberschrift, 12))
    
    # Name field
    texfield_list.append(textFunctions.textField("Name", 12, 7, textKoerper, 5))
    name_input = textFunctions.textInput(19, 7, textKoerper, 10, 1)
    texfield_list.append(name_input)
    
    # Passwort field
    texfield_list.append(textFunctions.textField("Passwort", 12, 9, textKoerper, 5))
    password_field = textFunctions.textInput(19, 9, textKoerper, 10, 1)
    password_field.is_password = True
    password_field.show_password = False
    texfield_list.append(password_field)
    
    # Passwort anzeigen button
    texfield_list.append(textFunctions.toggleButton("Passwort Anzeigen", 30, 9, textKoerper, 8, 1))
    
    # Error message (leer anfangs)
    error_msg = textFunctions.textField("---", 12, 11, textKoerper, 17)
    error_msg.color = (255, 0, 0)  # Rote Farbe für Text
    texfield_list.append(error_msg)
    
    # Register und Anmelde buttons
    texfield_list.append(textFunctions.toggleButton("Registrieren", 12, 13, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Anmelden", 21, 13, textKoerper, 8, 1))
    
    # AUsgabe der eingabe und ausgabe
    return {
        "fields": texfield_list,
        "name_input": name_input,
        "password_field": password_field,
        "error_msg": error_msg
    }

def handle_login_events(event, login_data, site):
    texfield_list = login_data["fields"]
    name_input = login_data["name_input"]
    password_field = login_data["password_field"]
    error_msg = login_data["error_msg"]
    

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        for field in texfield_list:
            if isinstance(field, textFunctions.textInput):
                if field.rec.collidepoint(posx, posy):
                    field.active = True
                else:
                    field.active = False
                    
            elif isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Passwort Anzeigen":
                    # Password sichtbar button funktion
                    for input_field in texfield_list:
                        if isinstance(input_field, textFunctions.textInput) and input_field.is_password:
                            input_field.show_password = not input_field.show_password
                elif field.text == "Registrieren":
                    site = 2  # zu Registrieren springen
                    error_msg.text = "---"  # dabei den error löschen
                elif field.text == "Anmelden":
                    # Überprüfen des Logins
                    if not name_input.text.strip() and not password_field.real_text.strip():
                        error_msg.text = "Bitte Name UND Passwort EINGEBEN"
                    elif not name_input.text.strip() :
                        error_msg.text = "Bitte Name EINGEBEN"
                    elif not password_field.real_text.strip():
                        error_msg.text = "Bitte Passwort EINGEBEN"
                    #Passwort in Hash umwandeln und im Sql überpfrüfen.
                    elif sql.LoginDB(name_input.text.strip(), hashlib.sha256(password_field.real_text.strip().encode()).hexdigest()):
                        site = 3  # Login erfolgreich
                        error_msg.text = "---"  # Error Löschen
                        name_input.text = ""
                        password_field.real_text = ""
                        login_data["login_attempts"] = 0
                    else:
                        login_data["login_attempts"] = login_data.get("login_attempts", 0) + 1 #fehlversuche zählen
                        error_msg.text = f"Fehlversuch {login_data['login_attempts']}/3" #ausgabe zähler
            
                        if login_data["login_attempts"] >= 3: #bei mehr als 3 falschen versuchen, abbruch?!?! wait
                            #timer = pygame.time.wait(6000)
                            #error_msg.text = f"Warte bitte {timer}"
                            pygame.quit()
                            sys.exit()
                        
    
    if event.type == pygame.KEYDOWN:
        for field in texfield_list:
            if isinstance(field, textFunctions.textInput) and field.active:
                if event.key == pygame.K_BACKSPACE: #backspace/löschen taste löscht im text immer ein Zeichen
                    field.text = field.text[:-1]
                    if field.is_password:
                        field.real_text = field.real_text[:-1]
                elif event.key == pygame.K_TAB:
                    field.text = field.text + ""#beim tab nichts machen #nice to have ins nächste feld springen.
                else: #umlaute/sinderzeichen ersetzen, für das font, und leerzeichen nicht ermöglichen
                    char = event.unicode.replace("ü", "u").replace("ö", "o").replace("ä", "a").replace("ß", "ss").replace("Ü", "U").replace("Ö", "O").replace("Ä", "A").replace(" ", "")
                    if field.is_password:
                        field.real_text += char
                        field.text += "*" if not field.show_password else char
                    else:
                        field.text += char
    
    return site