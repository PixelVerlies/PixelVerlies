import pygame
import textFunctions 
import grid         
import sql                

from textFunctions import textInput, toggleButton, textField

def create_character_fields(ueberschrift, textKoerper, selected_character_id=None):
    texfield_list = []
    weapon_table_rects = [] 
    
    texfield_list.append(textField("CHARAKTER MENÜ", 16, 2, ueberschrift, 12))
    
    character_details = None
    character_potions = []
    character_weapons = []
    
    if selected_character_id:
        character_details = sql.get_character_details(selected_character_id)
        character_potions = sql.get_character_potions(selected_character_id)
        character_weapons = sql.get_character_weapons(selected_character_id)
        
    char_name_input = None 

    if character_details:
        char_name_input = textInput(2, 5, textKoerper, 10, 1)
        char_name_input.real_text = character_details[0] 
        char_name_input.text = char_name_input.real_text 
        texfield_list.append(char_name_input)
        
        texfield_list.append(textField(f"Klasse: {character_details[1]}", 2, 7, textKoerper, 10))
        
        texfield_list.append(textField(f"Bewegung: {character_details[4]}", 2, 9, textKoerper, 10))
        texfield_list.append(textField(f"Leben: {character_details[2]}", 2, 11, textKoerper, 10))
        texfield_list.append(textField(f"Schaden: {character_details[6] if character_details[6] is not None else 'N/A'}", 2, 13, textKoerper, 10))
        texfield_list.append(textField(f"Schutz: 5", 2, 15, textKoerper, 10))
        
        texfield_list.append(textField(f"Level: {character_details[3]}", 2, 17, textKoerper, 5))
        
        potion_y_start = 5 
        if character_potions:
            for i, (desc, count) in enumerate(character_potions):
                texfield_list.append(textField(f"{count}x {desc}", 14, potion_y_start + (i*2), textKoerper, 10))
        else:
            texfield_list.append(textField("Keine Heiltränke", 14, potion_y_start, textKoerper, 10))
        
        texfield_list.append(textField(f"Waffe: {character_details[5] if character_details[5] is not None else 'Keine Waffe'}", 14, 11, textKoerper, 10))

    else:
        texfield_list.append(textField("Kein Charakter ausgewählt", 16, 7, textKoerper, 15))

    fertig_button = toggleButton("Fertig", 30, 21, textKoerper, 8, 1) 
    texfield_list.append(fertig_button)
    
    weapon_table_headers = [["Name", "Schaden", "Ausgeruestet"]]
    
    return {
        "fields": texfield_list,
        "char_name_input": char_name_input,
        "selected_character_id": selected_character_id,
        "fertig_button": fertig_button, 
        "weapon_table_headers": weapon_table_headers,
        "weapon_table_data": character_weapons, 
        "weapon_table_rects": weapon_table_rects 
    }

def draw_character_screen(character_data, blockSize, SCREEN, textKoerper):
    for field in character_data["fields"]:
        field.drawField(blockSize, SCREEN)
    
    draw_weapon_inventory_table(character_data, blockSize, SCREEN, textKoerper)

def draw_weapon_inventory_table(character_data, blockSize, SCREEN, textKoerper):
    full_weapon_data = character_data["weapon_table_headers"] + character_data["weapon_table_data"]
    
    table_font = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 20)

    character_data["weapon_table_rects"] = []

    table_start_x = 14
    table_start_y = 13
    
    col_widths = [5, 5, 5]

    for row_idx, row_data in enumerate(full_weapon_data):
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
                    display_text = str(row_data[1]) 
                elif col_idx == 1: 
                    display_text = str(row_data[2]) 
                elif col_idx == 2: 
                    display_text = "Ja" if row_data[3] == 1 else "Nein" 
            
            text_color = (0, 0, 0) if row_idx == 0 else (255, 255, 255)
            bg_color = (255, 255, 255) if row_idx == 0 else (0, 0, 0)
            
            text_surface = table_font.render(display_text, False, text_color)
            
            cell_surface = pygame.Surface(rect.size)
            cell_surface.fill(bg_color)
            
            text_rect = text_surface.get_rect(center=(rect.width / 2, rect.height / 2))
            cell_surface.blit(text_surface, text_rect)
            
            SCREEN.blit(cell_surface, rect.topleft)

            if row_idx >= 1 and col_idx == 0: 
                full_row_rect = pygame.Rect(
                    grid.gridCordinat(table_start_x, y, blockSize),
                    (sum(col_widths) * blockSize, 2 * blockSize)
                )
                character_data["weapon_table_rects"].append((full_row_rect, row_data[0]))


def handle_character_events(event, character_data, site):
    if character_data["char_name_input"] and isinstance(character_data["char_name_input"], textFunctions.textInput):
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()
            if character_data["char_name_input"].rec.collidepoint(posx, posy):
                character_data["char_name_input"].active = True
            else:
                if character_data["char_name_input"].active: 
                    character_data["char_name_input"].active = False
                    if character_data["selected_character_id"]:
                         sql.update_character_name(character_data["selected_character_id"], character_data["char_name_input"].real_text)
        
        character_data["char_name_input"].handle_event(event) 

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        if character_data["fertig_button"].rec.collidepoint(posx, posy):
            if character_data["char_name_input"] and character_data["selected_character_id"]:
                 if character_data["char_name_input"].real_text != sql.get_character_details(character_data["selected_character_id"])[0]:
                    sql.update_character_name(character_data["selected_character_id"], character_data["char_name_input"].real_text)
            site = 3 
            return site 

        for rect, weapon_id in character_data["weapon_table_rects"]:
            if rect.collidepoint(posx, posy):
                selected_char_id = character_data["selected_character_id"]
                if selected_char_id:
                    sql.unequip_all_weapons(selected_char_id)
                    sql.equip_weapon(selected_char_id, weapon_id)
                    
                    new_character_data = create_character_fields(
                        character_data["fields"][0].font, 
                        character_data["char_name_input"].font, 
                        character_data["selected_character_id"]
                    )
                    character_data.update(new_character_data) 
                    return site 
                break

    return site