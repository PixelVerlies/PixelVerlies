import sys
import pygame
import textFunctions
import grid
import sql

def create_menu_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Titel "Hauptmenü"
    texfield_list.append(textFunctions.textField("HAUPMENÜ", 3, 2, ueberschrift, 11))

    # Menu buttons
    texfield_list.append(textFunctions.toggleButton("Anleitung", 3, 6, textKoerper, 8, 1))
    create_new_char_button = textFunctions.toggleButton("Neuen Charakter", 3, 8, textKoerper, 8, 1)
    texfield_list.append(create_new_char_button)
    texfield_list.append(textFunctions.toggleButton("Charakter", 3, 10, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Level", 3, 12, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Spiel starten", 3, 14, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Abmelden", 3, 16, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Beenden", 3, 18, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Credits", 3, 20, textKoerper, 8, 1))
    
    
    # Character table überschriften
    character_data_headers = [
        ["NAME", "KLASSE", "STUFE"],
    ]
    #Klassen Table Überschriften
    Klasse_data_headers = [
        ["KlassenName","LP", "Bewegung" ],
    ]

    # Eingabefeld für neuen Charaktername (anfänglich unsichtbar)
    name_input_label = textFunctions.textField("Name eingeben:", 12, 6, textKoerper, 6)
    new_char_name_input = textFunctions.textInput(19, 6, textKoerper, 10, 1)
    # Button zum Speichern des neuen Charakters (anfänglich unsichtbar)
    save_new_char_button = textFunctions.toggleButton("Speichern", 32, 6, textKoerper, 6, 1) # Position angepasst
    
    # Error/Success Message Feld
    error_message_field = textFunctions.textField("", 19, 4, textKoerper, 15) # Position angepasst
    error_message_field.active = False # Anfänglich unsichtbar

    return {
        "fields": texfield_list,
        "character_data_headers": character_data_headers,
        "klasse_data_headers": Klasse_data_headers,
        "show_characters": False, # Zeigt die Charakterliste an/aus
        "show_new_char_input": False, # Zeigt die Eingabefelder für neuen Charakter an/aus
        "show_klasse_table": False, # Zeigt die Charakterliste an/aus
        "show_level_table": False, # Zeigt die Levelliste an/aus
        "table_rects": [], # Für Charakterauswahl
        "klasse_table_rects": [], # Für Klassenauswahl
        "level_table_rects": [], # Für Klassenauswahl
        "selected_character": None,
        "last_clicked_char": None,  # Für Doppelklick-Erkennung
        "last_click_time": 0,       # Zeitpunkt des letzten Klicks
        "selected_klasse_id": None, # Für die ausgewählte Klasse
        "selected_level_id": 1,  # Standardmäßig Level 1 ausgewählt
        "selected_level_id": None, #  Für die ausgewählte Klasse
        "create_new_char_button": create_new_char_button, 
        "name_input_label": name_input_label,
        "new_char_name_input": new_char_name_input,
        "save_new_char_button": save_new_char_button, # Neuer Charakter Speichern Button
        "error_message_field": error_message_field,
    }

def draw_character_table(menu_data, blockSize, SCREEN, current_player_id, textKoerper):
    # Zeichne die Charaktertabelle, wenn 'Charakter' Button geklickt wurde
    if menu_data["show_characters"]:
        db_data_raw = sql.CharakterMenuDB(current_player_id)
        
        db_data_display = []
        for row in db_data_raw:
            db_data_display.append([row[1], row[2], row[3], row[0]]) # Name, Klasse, Stufe, CharakterID
        
        full_data_to_display = menu_data["character_data_headers"] + [row[:-1] for row in db_data_display] # Ohne CharakterID für die Anzeige
        
        table_font = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 30) 

        menu_data["table_rects"] = [] #Leeren für die Charaktertabelle
        
        table_start_x = 14 #Startposition
        table_start_y = 9
        
        col_widths = [10, 7, 4] # Spaltenbreiten für Name, Klasse, Stufe
        
        for row_idx, row_data in enumerate(full_data_to_display):

            if row_idx == 0: # Überschriften
                text_color = (0, 0, 0)
                bg_color = (255, 255, 255)
            else: # Datenzeilen
                text_color = (255, 255, 255)
                char_id = db_data_display[row_idx-1][3]
                # Markiere ausgewählten Charakter in Grau
                bg_color = (137, 137, 137) if char_id == menu_data["selected_character"] else (0, 0, 0)

            for col_idx, col_width in enumerate(col_widths): #Tabelle aussehen
                x = table_start_x + sum(col_widths[:col_idx])
                y = table_start_y + row_idx * 2
                
                rect = pygame.Rect(
                    grid.gridCordinat(x, y, blockSize),
                    (col_width * blockSize, 2 * blockSize)
                )

                display_text_content = str(row_data[col_idx])
                text_surface = table_font.render(display_text_content, False, text_color)
                
                cell_surface = pygame.Surface(rect.size)
                cell_surface.fill(bg_color)
                
                text_rect = text_surface.get_rect(center=(rect.width / 2, rect.height / 2))
                cell_surface.blit(text_surface, text_rect)
                
                SCREEN.blit(cell_surface, rect.topleft)

                if row_idx >= 1: # Nur für Datenzeilen klickbare Rechtecke erstellen
                    if col_idx == 0: 
                        full_row_rect = pygame.Rect(
                            grid.gridCordinat(table_start_x, y, blockSize),
                            (sum(col_widths) * blockSize, 2 * blockSize)
                        )
                        menu_data["table_rects"].append((full_row_rect, db_data_display[row_idx-1][3])) # Letztes Element ist die CharakterID


    # Zeichne die Eingabefelder für neuen Charakter, den Save Button und die Klassentabelle, wenn 'show_new_char_input' True ist
    if menu_data["show_new_char_input"]:
        menu_data["name_input_label"].drawField(blockSize, SCREEN)
        menu_data["new_char_name_input"].drawField(blockSize, SCREEN)
        menu_data["save_new_char_button"].drawField(blockSize, SCREEN) 

        # Klassentabelle zeichnen
        db_data_raw_klasse = sql.KlassenMenuDB()
        db_data_display_klasse = []
        for row in db_data_raw_klasse:
            db_data_display_klasse.append([row[0], row[1], row[2], row[3]]) # KlassenName, LP, Bewegung, KlassenID
        
        full_data_to_display_klasse = menu_data["klasse_data_headers"] + [row[:-1] for row in db_data_display_klasse] # Ohne KlassenID für die Anzeige
        
        table_font_klasse = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 30) 

        menu_data["klasse_table_rects"] = [] # NEU: Separate Liste für Klassenauswahl-Rechtecke
        
        table_klasse_x = 14
        table_klasse_y = 9 # Startposition für Klassentabelle
        
        col_widths_klasse = [10, 4, 5] # Angepasste Spaltenbreiten für Klassen
        
        for row_idx, row_data in enumerate(full_data_to_display_klasse):
            if row_idx == 0: # Überschriften
                text_color = (0, 0, 0)
                bg_color = (255, 255, 255)
            else: # Datenzeilen
                text_color = (255, 255, 255)
                bg_color = (0, 0, 0)
                # Markiere ausgewählte Klasse
                if db_data_display_klasse[row_idx-1][3] == menu_data["selected_klasse_id"]: # Vergleiche mit KlassenID
                    bg_color = (137,137,137) # Grauer Hintergrund für ausgewählte Klasse
            for col_idx, col_width in enumerate(col_widths_klasse):
                x = table_klasse_x + sum(col_widths_klasse[:col_idx])
                y = table_klasse_y + row_idx * 2
                
                rect = pygame.Rect(
                    grid.gridCordinat(x, y, blockSize),
                    (col_width * blockSize, 2 * blockSize)
                )
                
                display_text_content = str(row_data[col_idx])
                text_surface = table_font_klasse.render(display_text_content, False, text_color)
                
                cell_surface = pygame.Surface(rect.size)
                cell_surface.fill(bg_color)
                
                text_rect = text_surface.get_rect(center=(rect.width / 2, rect.height / 2))
                cell_surface.blit(text_surface, text_rect)
                
                SCREEN.blit(cell_surface, rect.topleft)

                if row_idx >= 1: # Nur für Datenzeilen klickbare Rechtecke erstellen
                    if col_idx == 0: 
                        full_row_rect = pygame.Rect(
                            grid.gridCordinat(table_klasse_x, y, blockSize),
                            (sum(col_widths_klasse) * blockSize, 2 * blockSize)
                        )
                        menu_data["klasse_table_rects"].append((full_row_rect, db_data_display_klasse[row_idx-1][3])) # Letztes Element ist die KlassenID
    
    # Zeichne die Fehlermeldung, wenn sie aktiv ist
    if menu_data["error_message_field"].active:
        menu_data["error_message_field"].drawField(blockSize, SCREEN)


    # Zeichne die Level Auswahl Tabelle
    if menu_data["show_level_table"]:
        # LevelTabelle zeichnen
        db_data_raw_level = sql.LevelMenuDB()
        db_data_display_level = []
        for row in db_data_raw_level:
            db_data_display_level.append([row[0], row[1]]) # Levelname und StufenID
        
        table_font_level = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 30) 

        menu_data["level_table_rects"] = [] # Liste für klickbare Rechtecke der Level-Tabelle
        
        table_level_x = 14
        table_level_y = 9 # Startposition für Tabelle
        
        col_widths_level = [10, 4] # Spaltenbreiten für Levelname und ID
        
        for row_idx, row_data in enumerate(db_data_display_level):
            # Keine Überschriften mehr, direkt die Daten anzeigen
            text_color = (255, 255, 255)
            bg_color = (0, 0, 0)
            
            # Markiere ausgewähltes Level
            if row_data[1] == menu_data["selected_level_id"]: # Vergleiche mit StufenID
                bg_color = (137,137,137) # Grauer Hintergrund für ausgewähltes Level

            for col_idx, col_width in enumerate(col_widths_level):
                x = table_level_x + sum(col_widths_level[:col_idx])
                y = table_level_y + row_idx * 2
                
                rect = pygame.Rect(
                    grid.gridCordinat(x, y, blockSize),
                    (col_width * blockSize, 2 * blockSize)
                )
                
                display_text_content = str(row_data[col_idx])
                text_surface = table_font_level.render(display_text_content, False, text_color)
                
                cell_surface = pygame.Surface(rect.size)
                cell_surface.fill(bg_color)
                
                text_rect = text_surface.get_rect(center=(rect.width / 2, rect.height / 2))
                cell_surface.blit(text_surface, text_rect)
                
                SCREEN.blit(cell_surface, rect.topleft)

            # Klickbare Rechtecke für die ganze Zeile erstellen
            full_row_rect = pygame.Rect(
                grid.gridCordinat(table_level_x, table_level_y + row_idx * 2, blockSize),
                (sum(col_widths_level) * blockSize, 2 * blockSize)
            )
            menu_data["level_table_rects"].append((full_row_rect, row_data[1])) # StufenID speichern

                

 
def handle_menu_events(event, menu_data, site, current_player_id, current_site, char_id, level_id):
    # Event-Handling für Textfelder (Charaktername Eingabe)
    if menu_data["show_new_char_input"] and isinstance(menu_data["new_char_name_input"], textFunctions.textInput):
        menu_data["new_char_name_input"].handle_event(event) # Immer handle_event aufrufen, wenn sichtbar

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos() 
        last_selected = menu_data.get("last_clicked_char", None)
        current_time = pygame.time.get_ticks()

        # Aktiviere/Deaktiviere das Textfeld "new_char_name_input"
        if menu_data["show_new_char_input"] and isinstance(menu_data["new_char_name_input"], textFunctions.textInput):
            if menu_data["new_char_name_input"].rec.collidepoint(posx, posy):
                menu_data["new_char_name_input"].active = True
                menu_data["error_message_field"].active = False # Fehlermeldung ausblenden bei Klick auf Feld
            else:
                if menu_data["new_char_name_input"].active: # Deaktivieren nur wenn aktiv und außerhalb geklickt
                    menu_data["new_char_name_input"].active = False

        # Standard Menu Buttons
        for field in menu_data["fields"]:
            if isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                # Behandlung für den "Charakter" Button
                if field.text == "Charakter":
                    menu_data["show_characters"] = not menu_data["show_characters"]
                    # Beim Umschalten des Charakter-Buttons, Eingabefelder für neuen Char ausblenden
                    menu_data["show_new_char_input"] = False 
                    menu_data["error_message_field"].active = False # Fehlermeldung ausblenden
                    menu_data["new_char_name_input"].active = False # Textfeld deaktivieren
                    menu_data["selected_klasse_id"] = None # Auswahl zurücksetzen
                    menu_data["show_level_table"] = False  #Level-Tabelle ausblenden

                # Behandlung für den "Neuen Charakter" Button
                elif field.text == "Neuen Charakter":
                    # Prüfen ob bereits 5 Charaktere vorhanden sind
                    char_count = sql.count_characters_for_player(current_player_id)
                    if char_count >= 5:
                        menu_data["error_message_field"].update_text("Maximale Anzahl von 5 erreicht.")
                        menu_data["error_message_field"].active = True
                        menu_data["error_message_field"].set_color((255, 0, 0))
                        menu_data["show_new_char_input"] = False  # Eingabefelder nicht anzeigen
                        return site,0,0
                    
                    # Nur wenn weniger als 5 Charaktere vorhanden sind:
                    menu_data["show_new_char_input"] = not menu_data["show_new_char_input"] # Umschalten der Sichtbarkeit
                    menu_data["show_characters"] = False # Charakterliste ausblenden
                    menu_data["error_message_field"].active = False # Fehlermeldung ausblenden
                    menu_data["new_char_name_input"].real_text = "" # Textfeld leeren
                    menu_data["new_char_name_input"].text = "" # Textfeld leeren
                    menu_data["show_level_table"] = False  #Level-Tabelle ausblenden
                    menu_data["selected_klasse_id"] = None # Auswahl zurücksetzen
                    if menu_data["show_new_char_input"]:
                        menu_data["new_char_name_input"].active = True # Textfeld aktivieren
                    else:
                        menu_data["new_char_name_input"].active = False

                # Behandlung für den "Level" Button
                elif field.text == "Level":
                    menu_data["show_level_table"] = not menu_data["show_level_table"]
                    # Andere Tabellen ausblenden
                    menu_data["show_characters"] = False
                    menu_data["show_new_char_input"] = False
                    menu_data["show_klasse_table"] = False
                    return site,0,0


                # Weitere Menü-Buttons
                elif field.text == "Anleitung": 
                    site = 5
                elif field.text == "Spiel starten":
                    if menu_data["selected_character"] is None: #Muss Charakter ausgewählt werden mit dem man spielen will
                        menu_data["error_message_field"].update_text("Bitte wähle Charakter aus.")
                        menu_data["error_message_field"].active = True
                        menu_data["error_message_field"].set_color((255, 0, 0))
                        return site, 0, 0
                    
                    char_id = menu_data["selected_character"]
                    
                    # Fehlermeldung wenn kein Level ausgewählt ist (sollte nicht passieren, da Standard 1)
                    if menu_data["selected_level_id"] is None:
                        menu_data["selected_level_id"] = 1  # Sicherheitsfall
                        
                    
                    level_id = menu_data['selected_level_id']
                    site = 6
                    return site, char_id, level_id
                elif field.text == "Abmelden":
                    site = 1  
                elif field.text == "Beenden":
                    pygame.quit()
                    sys.exit()
                elif field.text == "Credits":
                    site = 4
                return site,0,0
        
        # Event-Handling für den "Speichern" Button des neuen Charakters
        if menu_data["show_new_char_input"] and menu_data["save_new_char_button"].rec.collidepoint(posx, posy):
            #Prüfung der Charakteranzahl auch beim Speichern
            char_count = sql.count_characters_for_player(current_player_id)
            if char_count >= 5:
                menu_data["error_message_field"].update_text("Maximale Anzahl von 5 erreicht.")
                menu_data["error_message_field"].active = True
                menu_data["error_message_field"].set_color((255, 0, 0))
                return site,0,0
    
        

            char_name = (menu_data["new_char_name_input"]).text.strip() # .real_text verwenden für den echten Text
            
            if not char_name:
                menu_data["error_message_field"].update_text("Bitte Namen eingeben.")
                menu_data["error_message_field"].active = True
                menu_data["error_message_field"].set_color((255, 0, 0)) # Rot für Fehler
            elif menu_data["selected_klasse_id"] is None: # NEU: Prüfen, ob Klasse ausgewählt wurde
                menu_data["error_message_field"].update_text("Bitte eine Klasse auswählen.")
                menu_data["error_message_field"].active = True
                menu_data["error_message_field"].set_color((255, 0, 0)) # Rot für Fehler
            elif sql.check_character_name_exists_for_player(char_name, current_player_id):
                menu_data["error_message_field"].update_text("Charaktername existiert bereits!")
                menu_data["error_message_field"].active = True
                menu_data["error_message_field"].set_color((255, 0, 0)) # Rot für Fehler
            else:
                # Charakter erstellen, jetzt mit der ausgewählten Klasse
                success = sql.create_character(char_name, menu_data["selected_klasse_id"], current_player_id) # KlasseID übergeben
                if success:
                    menu_data["error_message_field"].update_text("Charakter erfolgreich erstellt!")
                    menu_data["error_message_field"].active = True
                    menu_data["error_message_field"].set_color((0, 255, 0)) # Grün für Erfolg
                    menu_data["new_char_name_input"].real_text = ""
                    menu_data["new_char_name_input"].text = ""
                    menu_data["new_char_name_input"].active = False 
                    menu_data["selected_klasse_id"] = None # NEU: Auswahl zurücksetzen nach erfolgreicher Erstellung
                else:
                    menu_data["error_message_field"].update_text("Fehler beim Erstellen des Charakters.")
                    menu_data["error_message_field"].active = True
                    menu_data["error_message_field"].set_color((255, 0, 0)) # Rot für Fehler

        # NEU: Check clicks on class table (if visible)
        if menu_data["show_new_char_input"]:
            for rect, klasse_id in menu_data["klasse_table_rects"]: 
                if rect.collidepoint(posx, posy): 
                    menu_data["selected_klasse_id"] = klasse_id # KlasseID speichern
                    menu_data["error_message_field"].active = False # Fehlermeldung ausblenden bei Klassenauswahl
                    return site,0,0 # Bleibe auf dem gleichen Bildschirm

        # Check character table clicks (if visible)
        if menu_data["show_characters"]:      
            for rect, char_id in menu_data["table_rects"]:
                if rect.collidepoint(posx, posy):
                    # Doppelklick-Erkennung
                    if menu_data["selected_character"] == char_id:
                        # Zweiter Klick - Character Screen öffnen
                        return 7, char_id, 0
                    else:
                        # Erster Klick - Charakter auswählen
                        menu_data["selected_character"] = char_id
                        return site, 0, 0
                
        # Check clicks on level table (if visible)
        if menu_data["show_level_table"]:
            for rect, level_id in menu_data["level_table_rects"]: 
                if rect.collidepoint(posx, posy): 
                    menu_data["selected_level_id"] = level_id # StufenID speichern
                    return site,0,0 # Bleibe auf dem gleichen Bildschirm  
        

    return site,0,0