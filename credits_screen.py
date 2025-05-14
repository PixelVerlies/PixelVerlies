import pygame
import textFunctions
import grid

def create_credits_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Title "Hauptmenü"
    texfield_list.append(textFunctions.textField("Credits", 14, 3, ueberschrift, 12))

    textwars = """Lastenheft Projektarbeit:

Pixel-Verlies 

Ein Dungeon Crawler Spiel 
mit Pygame entwickeln 
und in Pixel Art gehalten.

Schüler:
Julian Daum,
Sven Thienel

Klasse:
WIV2426"""

    #Textfeld Starwars
    texfield_list.append(textFunctions.textField(textwars, 16, 8, textKoerper, 8,5))

    # Charakter button
    texfield_list.append(textFunctions.toggleButton("Zuruck", 16, 18, textKoerper, 8, 1))

    
    return {
        "fields": texfield_list,

    }

    
def handle_credits_events(event, credits_data, site):
    texfield_list = credits_data["fields"]

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        for field in texfield_list:
            if isinstance(field, textFunctions.textInput):
                if field.rec.collidepoint(posx, posy):
                    field.active = True
                else:
                    field.active = False
                    
            elif isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Zuruck":
                    site = 3


    
    return site