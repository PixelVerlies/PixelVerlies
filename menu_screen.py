import sys
import pygame
import textFunctions
import grid
import sql

def create_menu_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Title "Hauptmenü"
    texfield_list.append(textFunctions.textField("HAUPMENÜ", 3, 3, ueberschrift, 12))

    # Menu buttons
    texfield_list.append(textFunctions.toggleButton("Charakter", 3, 8, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Dungeon", 3, 10, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Start", 3, 12, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Abmelden", 3, 14, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Beenden", 3, 16, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("Credits", 3, 18, textKoerper, 8, 1))
    
    # Character table überschriften
    character_data = [
        ["NAME", "KLASSE", "STUFE"],
    ]
    
    
    return {
        "fields": texfield_list,
        "character_data": character_data,
        "show_characters": False,
        "table_rects": [],  # Hier werden die klickbaren Rechtecke gespeichert
        "selected_character": None  # Initial kein Charakter ausgewählt
    }

def draw_character_table(menu_data, blockSize, SCREEN):
    if not menu_data["show_characters"]:
        menu_data["table_rects"] = []
        return
        
    # Daten aus der Datenbank holen (SpielerID 1 als Beispiel)
    db_data = sql.CharakterMenuDB(1)
    
    # Überschriften + DB-Daten kombinieren
    full_data = menu_data["character_data"] + db_data
    
    textKoerper = pygame.font.Font("Arcade-Classic-Font/ARCADECLASSIC.TTF", 20)
    menu_data["table_rects"] = []
    
    # Table position
    table_start_x = 12
    table_start_y = 8
    
    # Column widths
    col_widths = [8, 8, 5]
    
    # zeichne tabelle für charakter
    for row in range(len(full_data)):
        for col, width in enumerate(col_widths):
            x = table_start_x + sum(col_widths[:col])
            y = table_start_y + row * 2
            
            rect = pygame.Rect(
                grid.gridCordinat(x, y, blockSize),
                (width * blockSize, 2 * blockSize)
            )
            
            # Klickbare Rechtecke für alle Datenzeilen erstellen (ab row 1)
            if row >= 1 and col == 0:
                full_row_rect = pygame.Rect(
                    grid.gridCordinat(table_start_x, y, blockSize),
                    (sum(col_widths) * blockSize, 2 * blockSize)
                )
                menu_data["table_rects"].append(full_row_rect)
            
            # Farben um tabelle zu erkennen
            if row == 0:
                color = (150, 150, 150)
            else:
                if row % 2 == 1:
                    color = (200, 200, 200) if col != 1 else (180, 180, 180)
                else:
                    color = (255, 255, 255) if col != 1 else (230, 230, 230)
            
            pygame.draw.rect(SCREEN, color, rect)
            pygame.draw.rect(SCREEN, (100, 100, 100), rect, 1)
    
    # Tabellen text
    for row, row_data in enumerate(full_data):
        for col, (cell, width) in enumerate(zip(row_data, col_widths)):
            x = table_start_x + sum(col_widths[:col])
            y = table_start_y + row * 2
            
            # Zelleninhalt in String umwandeln (falls nicht schon String)
            cell_text = str(cell)
            text = textKoerper.render(cell_text, False, (0, 0, 0))
            text_x, text_y = text.get_size()
            pos = grid.gridCordinat(x, y, blockSize)
            text_pos = (
                pos[0] + (width * blockSize - text_x) // 2,
                pos[1] + (2 * blockSize - text_y) // 2
            )
            SCREEN.blit(text, text_pos)


def handle_menu_events(event, menu_data, site):
    texfield_list = menu_data["fields"]

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        # Check buttons first
        for field in texfield_list:
            if isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Charakter":
                    menu_data["show_characters"] = not menu_data["show_characters"]
                elif field.text == "Dungeon":
                    site = 4
                elif field.text == "Start":
                    site = 4
                elif field.text == "Abmelden":
                    site = 1
                elif field.text == "Beenden":
                    pygame.quit()
                    sys.exit()
                elif field.text == "Credits":
                    site = 4
                return site
        
        # Check character table clicks
        if menu_data["show_characters"]:
            for i, rect in enumerate(menu_data["table_rects"]):
                if rect.collidepoint(posx, posy):
                    db_data = sql.CharakterMenuDB(1)  # SpielerID 1 als Beispiel
                    if i < len(db_data):
                        menu_data["selected_character"] = db_data[i] + (db_data[i][2],)  # CharakterID hinzufügen
                        site = 7
                        return site
    
    return site