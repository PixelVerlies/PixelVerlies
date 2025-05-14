import pygame
import textFunctions
import grid

def create_menu_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Title "Hauptmenü"
    texfield_list.append(textFunctions.textField("HAUPMENÜ", 14, 3, ueberschrift, 12))


    # Charakter button
    texfield_list.append(textFunctions.toggleButton("Charakter", 16, 8, textKoerper, 8, 1))
    # Dungeon button
    texfield_list.append(textFunctions.toggleButton("Dungeon", 16, 10, textKoerper, 8, 1))
    # Start button
    texfield_list.append(textFunctions.toggleButton("Start", 16, 12, textKoerper, 8, 1))
    # Abmelden button
    texfield_list.append(textFunctions.toggleButton("Abmelden", 16, 14, textKoerper, 8, 1))
    # Beenden button
    texfield_list.append(textFunctions.toggleButton("Beenden", 16, 16, textKoerper, 8, 1))
    # Credits button
    texfield_list.append(textFunctions.toggleButton("Credits", 16, 18, textKoerper, 8, 1))
    
    return {
        "fields": texfield_list,

    }

    
def handle_menu_events(event, menu_data, site):
    texfield_list = menu_data["fields"]

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        for field in texfield_list:
            if isinstance(field, textFunctions.textInput):
                if field.rec.collidepoint(posx, posy):
                    field.active = True
                else:
                    field.active = False
                    
            elif isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Charakter":
                    site = 1
                elif field.text == "Dungeon":
                    site = 1  # Back to login
                elif field.text == "Start":
                    site = 1  # Back to login
                elif field.text == "Abmelden":
                    site = 1  # Back to login
                elif field.text == "Beenden":
                    pygame.quit() # Beenden Komplett
                elif field.text == "Credits":
                    site = 4  # Go to Credits

    
    return site