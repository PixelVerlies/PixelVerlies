import pygame
import textFunctions
import grid
import sql

def create_character_fields(ueberschrift, textKoerper, selected_char=None):
    texfield_list = []
    
    # Titel "CHARAKTER"
    texfield_list.append(textFunctions.textField("CHARAKTER", 16, 3, ueberschrift, 12))
    
    if selected_char:
        # Linke Seite: Charakterdaten
        char_name = textFunctions.textInput(16, 7, textKoerper, 10, 1)
        char_name.text = selected_char[0]  # Name aus DB
        texfield_list.append(char_name)
        
        # Bild einfügen (warrior.png)
        try:
            char_image = pygame.image.load("warrior.png")
            char_image = pygame.transform.scale(char_image, (150, 150))
            texfield_list.append(("image", char_image, 16, 10))
        except:
            pass
        
        # Attribute
        texfield_list.append(textFunctions.textField(f"Bewegung: {selected_char[3]}", 16, 16, textKoerper, 10))
        texfield_list.append(textFunctions.textField(f"Leben: {selected_char[4]}", 16, 18, textKoerper, 10))
        texfield_list.append(textFunctions.textField(f"Schaden: 5", 16, 20, textKoerper, 10))
        texfield_list.append(textFunctions.textField(f"Schutz: 5", 16, 22, textKoerper, 10))
        
        # Rechte Seite: Waffenliste
        texfield_list.append(textFunctions.textField("WAFFEN", 30, 7, ueberschrift, 8))
        
        # Waffen aus DB holen
        weapons = sql.get_character_weapons(selected_char[5])  # CharakterID
        
        for i, weapon in enumerate(weapons):
            weapon_text = f"{weapon[1]} {'(ausgerüstet)' if weapon[2] else ''}"
            weapon_btn = textFunctions.toggleButton(weapon_text, 30, 9 + i*2, textKoerper, 12, 1)
            weapon_btn.weapon_id = weapon[0]  # WaffenID speichern
            texfield_list.append(weapon_btn)
        
        # Fertig-Button
        texfield_list.append(textFunctions.toggleButton("Fertig", 30, 22, textKoerper, 8, 1))
    
    return {
        "fields": texfield_list,
        "selected_char": selected_char
    }

def handle_character_events(event, char_data, site):
    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        for field in char_data["fields"]:
            if isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Fertig":
                    # Name in DB aktualisieren
                    for f in char_data["fields"]:
                        if isinstance(f, textFunctions.textInput):
                            sql.update_character_name(char_data["selected_char"][5], f.text)  # CharakterID
                    
                    site = 3  # Zurück zum Hauptmenü
                elif hasattr(field, 'weapon_id'):
                    # Waffe ausrüsten
                    sql.equip_weapon(char_data["selected_char"][5], field.weapon_id)  # CharakterID
    
    return site