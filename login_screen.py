import pygame
import textFunctions
import sql
import hashlib

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

    # Neuer "Beenden" Button
    texfield_list.append(textFunctions.toggleButton("Beenden", 16, 15, textKoerper, 8, 1))
    
    # AUsgabe der eingabe und ausgabe
    return {
        "fields": texfield_list,
        "name_input": name_input,
        "password_field": password_field,
        "error_msg": error_msg
    }

def handle_login_events(event, login_data, current_site):
    name_input = login_data["name_input"]
    password_field = login_data["password_field"]
    error_msg = login_data["error_msg"]
    
    # Textfeld-Eingabe-Events unabhängig von Mausklick behandeln
    name_input.handle_event(event)
    password_field.handle_event(event)

    # Standard-Rückgabewert: Behalte den aktuellen Screen bei
    # Dies ist der Fall, wenn kein relevanter Event (Klick auf Button) stattfindet
    return_state = {'site': current_site, 'player_id': None}

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        # Logik zum Aktivieren/Deaktivieren der Textfelder
        if name_input.rec.collidepoint(posx, posy):
            name_input.active = True
            password_field.active = False
            error_msg.active = False # Fehlermeldung ausblenden bei Klick auf Feld
        elif password_field.rec.collidepoint(posx, posy):
            password_field.active = True
            name_input.active = False
            error_msg.active = False # Fehlermeldung ausblenden bei Klick auf Feld
        else: # Klick außerhalb der Textfelder und Buttons
            name_input.active = False
            password_field.active = False

        # Button-Handling
        for field in login_data["fields"]:
            if isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Passwort Anzeigen":
                    password_field.show_password = not password_field.show_password
                    error_msg.active = False # Fehlermeldung ausblenden, da keine Aktion, die Fehler verursacht
                    # return_state bleibt current_site
                elif field.text == "Registrieren":
                    error_msg.active = False # Fehlermeldung ausblenden beim Wechsel
                    return_state['site'] = 2 # Signal für main.py: Wechsel zu Site 2 (Registrierung)
                    return return_state # Gib den aktualisierten Zustand zurück
                elif field.text == "Anmelden":
                    username = name_input.text.strip()
                    password = password_field.real_text.strip()
                    
                    if not username and not password:
                        error_msg.update_text("Bitte Name UND Passwort EINGEBEN")
                        error_msg.active = True
                        error_msg.set_color((255, 0, 0))
                        # return_state bleibt current_site
                    elif not username:
                        error_msg.update_text("Bitte Name EINGEBEN")
                        error_msg.active = True
                        error_msg.set_color((255, 0, 0))
                        # return_state bleibt current_site
                    elif not password:
                        error_msg.update_text("Bitte Passwort EINGEBEN")
                        error_msg.active = True
                        error_msg.set_color((255, 0, 0))
                        # return_state bleibt current_site
                    else:
                        player_id = sql.LoginDB(username, hashlib.sha256(password.encode()).hexdigest())
                        
                        if player_id is not None:
                            error_msg.active = False
                            name_input.text = ""
                            password_field.real_text = ""
                            password_field.text = ""
                            name_input.active = False
                            password_field.active = False
                            login_data["login_attempts"] = 0 # Zähler zurücksetzen
                            return {'site': 3, 'player_id': player_id} # WICHTIG: Direkt das neue Site- und ID-Objekt zurückgeben
                        else:
                            login_data["login_attempts"] = login_data.get("login_attempts", 0) + 1
                            error_msg.update_text(f"Fehlversuch {login_data['login_attempts']}/3")
                            error_msg.active = True
                            error_msg.set_color((255, 0, 0))
                        
                            if login_data["login_attempts"] >= 3:
                                print("DEBUG: 3 Fehlversuche. Beende Spiel.") # Debugging
                                return "QUIT" # Signal zum Beenden des Spiels an main.py
                            # return_state bleibt current_site bei Login-Fehler
                    return return_state # Gib den aktualisierten Zustand zurück
                
                elif field.text == "Beenden": # Neuer Beenden-Button
                    print("DEBUG: 'Beenden' geklickt.") # Debugging
                    return "QUIT" # Signal zum Beenden des Spiels an main.py

    # Wenn kein relevanter Event (Klick auf Button) stattfindet,
    # wird der ursprüngliche return_state (aktuelle Site) zurückgegeben.
    return return_state