import pygame
import textFunctions
import grid

def create_character_fields(ueberschrift, textKoerper, character_data=None):
    texfield_list = []
    
    # Title "Charakter Menü"
    texfield_list.append(textFunctions.textField("CHARAKTER MENÜ", 16, 3, ueberschrift, 12))
    
    # Charakterdaten anzeigen wenn vorhanden
    if character_data:
        texfield_list.append(textFunctions.textField(f"Name: {character_data[0]}", 16, 7, textKoerper, 15))
        texfield_list.append(textFunctions.textField(f"Klasse: {character_data[1]}", 16, 9, textKoerper, 15))
        texfield_list.append(textFunctions.textField(f"Stufe: {character_data[2]}", 16, 11, textKoerper, 15))
    else:
        texfield_list.append(textFunctions.textField("Kein Charakter ausgewählt", 16, 7, textKoerper, 15))
    
    # Zurück-Button
    texfield_list.append(textFunctions.toggleButton("Zuruck", 16, 15, textKoerper, 8, 1))
    
    return {
        "fields": texfield_list
    }

def handle_character_events(event, char_data, site):
    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        for field in char_data["fields"]:
            if isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Zuruck":
                    site = 3  # Zurück zum Hauptmenü
    
    return site