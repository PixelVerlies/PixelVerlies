import pygame
import textFunctions
import grid

def create_menu_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Title "Hauptmenü"
    texfield_list.append(textFunctions.textField("HAUPMENÜ", 14, 3, ueberschrift, 12))


    # Charakter button
    texfield_list.append(textFunctions.toggleButton("Charakter", 15, 8, textKoerper, 8, 1))
    # Dungeon button
    texfield_list.append(textFunctions.toggleButton("Dungeon", 15, 10, textKoerper, 8, 1))
    # Start button
    texfield_list.append(textFunctions.toggleButton("Start", 15, 12, textKoerper, 8, 1))
    # Abmelden button
    texfield_list.append(textFunctions.toggleButton("Abmelden", 15, 14, textKoerper, 8, 1))
    # Beenden button
    texfield_list.append(textFunctions.toggleButton("Beenden", 15, 16, textKoerper, 8, 1))
    # Credits button
    texfield_list.append(textFunctions.toggleButton("Credits", 15, 18, textKoerper, 8, 1))
    
    return {
        "fields": texfield_list,

    }

    
def handle_menu_events(event, menu_data, site):
    texfield_list = menu_data["fields"]

    
    return site