import pygame
import textFunctions
import grid

def create_credits_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Title "Hauptmenü"
    texfield_list.append(textFunctions.textField("Credits", 14, 3, ueberschrift, 12))

    #Textfeld komplett
    texfield_list.append(textFunctions.textweiß("Lastenheft Projektarbeit:", 15, 6, textKoerper, 10,1))
    texfield_list.append(textFunctions.textweiß("Pixel-Verlies ", 15, 7, textKoerper, 10,1))
    texfield_list.append(textFunctions.textweiß("Ein Dungeon Crawler Spiel", 15, 8, textKoerper, 10,1))
    texfield_list.append(textFunctions.textweiß("mit Pygame entwickeln ", 15, 9, textKoerper, 10,1))
    texfield_list.append(textFunctions.textweiß("und in Pixel Art gehalten. ", 15, 10, textKoerper, 10,1))
    texfield_list.append(textFunctions.textweiß("Schüler:", 15, 11, textKoerper, 10,1))
    texfield_list.append(textFunctions.textweiß("Julian Daum, Sven Thienel", 15, 12, textKoerper, 10,1))
    texfield_list.append(textFunctions.textweiß("Klasse: WIV2426", 15, 13, textKoerper, 10,1))

    # zurück button
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
                    site = 3 #zurück zum hauptmenü


    
    return site