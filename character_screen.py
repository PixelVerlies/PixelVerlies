import pygame
import textFunctions 
import grid         
import sql                

from textFunctions import textInput, toggleButton, textField #für die textfelder

def create_character_fields(ueberschrift, textKoerper, selected_character_id=None):
    texfield_list = [] #textfelder
    weapon_table_rects = [] #Waffentabelle
    armor_table_rects = []  # Für Rüstungstabelle
    
    texfield_list.append(textField("CHARAKTER MENÜ", 16, 2, ueberschrift, 12))
    
    # Fehlermeldungsfeld hinzufügen (unsichtbar initial)
    error_message = textField("", 2, 19, textKoerper, 25)#Anfangs ist die Meldung leer
    error_message.active = False #Damit unsichtbar
    texfield_list.append(error_message)

    character_details = None
    character_potions = [] #Für Heiltränke
    character_weapons = [] #Für Waffendaten
    character_armor = []  # Für Rüstungsdaten
    
    if selected_character_id:
        character_details = sql.get_character_details(selected_character_id) # Einige Charakter Daten laden
        character_potions = sql.get_character_potions(selected_character_id) #Heiltränke laden
        character_weapons = sql.get_character_weapons(selected_character_id) #Waffen lalden
        character_armor = sql.get_character_rustung(selected_character_id)  #Rüstungen laden

    char_name_input = None  #Input Name 
    show_armor_table = False  # Steuert welche Tabelle angezeigt wird

    if character_details:
        char_name_input = textInput(2, 5, textKoerper, 10, 1) #Für Namensänderung des CHarakters
        char_name_input.real_text = character_details[0] #Charakter Name
        char_name_input.text = char_name_input.real_text  
        texfield_list.append(char_name_input)
        
        texfield_list.append(textField(f"Klasse: {character_details[1]}", 2, 7, textKoerper, 10)) #Klassen Name
        texfield_list.append(textField(f"Bewegung: {character_details[4]}", 2, 9, textKoerper, 10)) #Bewegunsrate
        texfield_list.append(textField(f"Leben: {character_details[2]}", 2, 11, textKoerper, 10)) # LP = Lebenspunkte
        texfield_list.append(textField(f"Schaden: {character_details[6] if character_details[6] is not None else 'N/A'}", 2, 13, textKoerper, 10)) #Waffen Schaden Wuerfel,
        texfield_list.append(textField(f"Schutz: {character_details[8]}", 2, 15, textKoerper, 10)) # Rüstung Schutz
        texfield_list.append(textField(f"Level: {character_details[3]}", 2, 17, textKoerper, 5)) # StufenID als Level
        
        potion_y_start = 5 #Festen Y Wert für alle Heiltränke
        if character_potions:
            for i, (desc, count) in enumerate(character_potions):
                texfield_list.append(textField(f"{count}x {desc}", 13, potion_y_start + (i*2), textKoerper, 9)) # Menge an Feldern erstellen je nachdem wie viele verschieden es gibt.
        else:
            texfield_list.append(textField("Keine Heiltränke", 13, potion_y_start, textKoerper, 9))#Falls es keine gibt
        
        texfield_list.append(textField(f"Waffe: {character_details[5] if character_details[5] is not None else 'Keine Waffe'}", 13, 11, textKoerper, 9))#Aktuelle ausgerüstete Waffe anzeigen

        texfield_list.append(textField(f"Rustung:{character_details[7]}", 13, 13, textKoerper, 9)) #Aktuell Ausgerüstete Rüstung anzeigen

        tabelle_button = toggleButton("Rustungstabelle", 13, 15, textKoerper, 9, 1)  #Button für Switch mit den Tabellen Waffen und Rüstung
        texfield_list.append(tabelle_button)
    else:
        texfield_list.append(textField("Kein Charakter ausgewählt", 16, 7, textKoerper, 15))#sollte nicht passieren

    fertig_button = toggleButton("Fertig", 30, 21, textKoerper, 8, 1) #Zurück zum Menü und Speichern des Namens
    texfield_list.append(fertig_button)
    
    weapon_table_headers = [["Name", "Schaden", "Gerustet"]] #Spalten Namen extra

    # Setze Button-Text korrekt je nach Status
    if tabelle_button:
        tabelle_button.text = "Waffentabelle" if show_armor_table else "Rustungstabelle"

    #Rückgabe
    return {
        "fields": texfield_list,
        "char_name_input": char_name_input,
        "selected_character_id": selected_character_id,
        "fertig_button": fertig_button, 
        "weapon_table_headers": weapon_table_headers,
        "weapon_table_data": character_weapons, 
        "weapon_table_rects": weapon_table_rects, 
        "armor_table_headers": [["Name", "Schutz", "Gerustet"]], #Waffen Spalten
        "armor_table_data": character_armor,
        "armor_table_rects": armor_table_rects,
        "error_message": error_message,
        "show_armor_table": show_armor_table   
    }


def draw_character_screen(character_data, blockSize, SCREEN, textKoerper):

    for field in character_data["fields"]:
        field.drawField(blockSize, SCREEN)


    # Nur die aktive Tabelle zeichnen
    if character_data.get("show_armor_table", False):
        draw_armor_inventory_table(character_data, blockSize, SCREEN, textKoerper)
    else:
        draw_weapon_inventory_table(character_data, blockSize, SCREEN, textKoerper)

def draw_armor_inventory_table(character_data, blockSize, SCREEN, textKoerper): #Rüstung Tabelle
    full_armor_data = character_data["armor_table_headers"] + character_data["armor_table_data"] #Daten laden
    
    table_font = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 20) #Schrift laden

    character_data["armor_table_rects"] = []  #Welche Tabelle geklickt wurde
    table_start_x = 23
    table_start_y = 5
    col_widths = [8, 3, 4]  # Breite für Name, Schutz, Gerüstet

    for row_idx, row_data in enumerate(full_armor_data): #Tabelle aussehen
        for col_idx, col_width in enumerate(col_widths):
            x = table_start_x + sum(col_widths[:col_idx]) #breite zuvor angegeben
            y = table_start_y + row_idx * 2 #Zwei blöcke hoch
            
            rect = pygame.Rect(
                grid.gridCordinat(x, y, blockSize),
                (col_width * blockSize, 2 * blockSize)
            )
            
            display_text = ""
            if row_idx == 0:  # Header
                display_text = str(row_data[col_idx])
            else:  # Datenzeilen
                if col_idx == 0: 
                    display_text = str(row_data[1])  # Name
                elif col_idx == 1: 
                    display_text = str(row_data[2])  # Schutz
                elif col_idx == 2: 
                    display_text = "Ja" if row_data[3] == 1 else "Nein"  # Gerüstet
            
            text_color = (0, 0, 0) if row_idx == 0 else (255, 255, 255) #Farbe für Header und für Daten
            bg_color = (255, 255, 255) if row_idx == 0 else (0, 0, 0) 
            
            text_surface = table_font.render(display_text, False, text_color) #Tabelle zeichnen
            cell_surface = pygame.Surface(rect.size)
            cell_surface.fill(bg_color)
            cell_surface.blit(text_surface, text_surface.get_rect(center=(rect.width/2, rect.height/2)))
            SCREEN.blit(cell_surface, rect.topleft)

            if row_idx >= 1 and col_idx == 0: #Datenzeilen klickbar
                full_row_rect = pygame.Rect(
                    grid.gridCordinat(table_start_x, y, blockSize),
                    (sum(col_widths) * blockSize, 2 * blockSize)
                )
                character_data["armor_table_rects"].append((full_row_rect, row_data[0]))  # Rüstungs-ID speichern

def draw_weapon_inventory_table(character_data, blockSize, SCREEN, textKoerper):
    full_weapon_data = character_data["weapon_table_headers"] + character_data["weapon_table_data"] #Daten laden
    
    table_font = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 20) #Schriftart

    character_data["weapon_table_rects"] = [] #Klick
    #Startecke der Tabelle
    table_start_x = 23
    table_start_y = 5
    #Größen der Spalten
    col_widths = [8, 3, 4]

    for row_idx, row_data in enumerate(full_weapon_data): #Tabelle aussehen
        for col_idx, col_width in enumerate(col_widths):
            x = table_start_x + sum(col_widths[:col_idx])
            y = table_start_y + row_idx * 2
            
            rect = pygame.Rect(
                grid.gridCordinat(x, y, blockSize),
                (col_width * blockSize, 2 * blockSize)
            )
            
            display_text = ""
            if row_idx == 0: 
                display_text = str(row_data[col_idx])
            else: 
                if col_idx == 0: 
                    display_text = str(row_data[1])  #Name
                elif col_idx == 1: 
                    display_text = str(row_data[2])  #Schaden
                elif col_idx == 2: 
                    display_text = "Ja" if row_data[3] == 1 else "Nein" #Ausgerüstet
            
            text_color = (0, 0, 0) if row_idx == 0 else (255, 255, 255) #Farben für Headen und Datenzeilen
            bg_color = (255, 255, 255) if row_idx == 0 else (0, 0, 0)
            
            text_surface = table_font.render(display_text, False, text_color) #Tabelle zeichnen
            cell_surface = pygame.Surface(rect.size)
            cell_surface.fill(bg_color)
            text_rect = text_surface.get_rect(center=(rect.width / 2, rect.height / 2))
            cell_surface.blit(text_surface, text_rect)
            SCREEN.blit(cell_surface, rect.topleft)

            if row_idx >= 1 and col_idx == 0: #Datenzeilen klickbar
                full_row_rect = pygame.Rect(
                    grid.gridCordinat(table_start_x, y, blockSize),
                    (sum(col_widths) * blockSize, 2 * blockSize)
                )
                character_data["weapon_table_rects"].append((full_row_rect, row_data[0]))


def handle_character_events(event, character_data, site, current_player_id):
    if character_data is None:
        return site
        
    # Name Input Handling
    if character_data["char_name_input"] and isinstance(character_data["char_name_input"], textFunctions.textInput):
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()
            if character_data["char_name_input"].rec.collidepoint(posx, posy):
                character_data["char_name_input"].active = True
                # Fehlermeldung ausblenden wenn Name bearbeitet wird
                character_data["error_message"].active = False
            else:
                if character_data["char_name_input"].active: 
                    character_data["char_name_input"].active = False

        character_data["char_name_input"].handle_event(event)

    # Event Handling
    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()

        # Umschalt-Button für Tabellen
        for field in character_data["fields"]:
            #Text ändern von Button jenachdem welceh angezeigt wird/ welcher Name im feld ist
            if isinstance(field, textFunctions.toggleButton) and field.text == "Rustungstabelle" and field.rec.collidepoint(posx, posy):
                character_data["show_armor_table"] = not character_data.get("show_armor_table", False)
                field.text = "Waffentabelle" if character_data["show_armor_table"] else "Rustungstabelle"
                return site
            if isinstance(field, textFunctions.toggleButton) and field.text == "Waffentabelle" and field.rec.collidepoint(posx, posy):
                character_data["show_armor_table"] = not character_data.get("show_armor_table", False)
                field.text = "Waffentabelle" if character_data["show_armor_table"] else "Rustungstabelle"
                return site
        
        # Fertig-Button Handling
        if character_data.get("fertig_button") and character_data["fertig_button"].rec.collidepoint(posx, posy):
            if character_data["char_name_input"] and character_data["selected_character_id"]:
                new_name = character_data["char_name_input"].text.strip()
                current_name = sql.get_character_details(character_data["selected_character_id"])[0] #SQL für Namen des CHarakters
                
                # Wenn Name unverändert, einfach zurückkehren
                if new_name == current_name:
                    return 3
                
                # Prüfe auf leeren Namen
                if not new_name:
                    character_data["error_message"].update_text("Name darf nicht leer sein!")
                    character_data["error_message"].active = True
                    character_data["error_message"].set_color((255, 0, 0))
                    return site
                
                # Prüfe auf doppelten Namen
                if sql.check_character_name_exists_for_player(new_name, current_player_id, character_data["selected_character_id"]):
                    character_data["error_message"].update_text("Du hast bereits einen Charakter mit diesem Namen.")
                    character_data["error_message"].active = True
                    character_data["error_message"].set_color((255, 0, 0))
                    return site
                
                # Name ist gültig und eindeutig - aktualisieren
                character_data["char_name_input"].real_text = new_name
                sql.update_character_name(character_data["selected_character_id"], new_name)
                character_data["error_message"].update_text("Name erfolgreich geändert!")
                character_data["error_message"].active = True
                character_data["error_message"].set_color((0, 255, 0))  # Grün für Erfolg
            
            return 3  # Zurück zum Menü

        # Rüstungs-Tabelle Handling
        if character_data.get("show_armor_table", False):
            for rect, armor_id in character_data.get("armor_table_rects", []):
                if rect.collidepoint(posx, posy):
                    selected_char_id = character_data["selected_character_id"]
                    if selected_char_id:
                        sql.unequip_all_rustung(selected_char_id)
                        sql.equip_rustung(selected_char_id, armor_id)
                        
                        # Daten neu laden und aktualisieren
                        new_character_data = create_character_fields(
                            character_data["fields"][0].font, 
                            character_data["char_name_input"].font, 
                            character_data["selected_character_id"]
                        )
                        # Zustand des Umschalt-Buttons beibehalten
                        new_character_data["show_armor_table"] = character_data["show_armor_table"]
                        character_data.update(new_character_data)
                        character_data["show_armor_table"] = new_character_data["show_armor_table"]
                        # Toggle-Button-Text aktualisieren
                        for field in character_data["fields"]:
                            if isinstance(field, textFunctions.toggleButton) and field.text in ("Waffentabelle", "Rustungstabelle"):
                                field.text = "Waffentabelle" if character_data["show_armor_table"] else "Rustungstabelle"

                        return site
                    break
        else:
            # Waffen-Tabelle Handling
            for rect, weapon_id in character_data.get("weapon_table_rects", []):
                if rect.collidepoint(posx, posy):
                    selected_char_id = character_data["selected_character_id"] #waffen zu dem charakter
                    if selected_char_id:
                        sql.unequip_all_weapons(selected_char_id) #Sql alle waffen auf nicht ausgerüstet
                        sql.equip_weapon(selected_char_id, weapon_id) #waffe ausrüsten neue
                    
                        new_character_data = create_character_fields(
                            character_data["fields"][0].font, 
                            character_data["char_name_input"].font, 
                            character_data["selected_character_id"]
                        )
                        character_data.update(new_character_data)
                        character_data["show_armor_table"] = new_character_data["show_armor_table"]
                        # Toggle-Button-Text aktualisieren
                        for field in character_data["fields"]:
                            if isinstance(field, textFunctions.toggleButton) and field.text in ("Waffentabelle", "Rustungstabelle"):
                                field.text = "Waffentabelle" if character_data["show_armor_table"] else "Rustungstabelle"
                        return site
                    break
            
    return site