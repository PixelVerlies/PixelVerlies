import pygame
import textFunctions
import grid

def create_anleitung_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Title "Hauptmenü"
    texfield_list.append(textFunctions.textField("Anleitung", 14, 2, ueberschrift, 12))

    #Textfeld komplett
    texfield_list.append(textFunctions.textweiß("Anleitung zum Spielen, bitte sorgfältig lesen !", 5, 6, textKoerper, 20,1))
    texfield_list.append(textFunctions.textweiß("1. Einen neuen harakter erstellen.", 5, 7, textKoerper, 20,1))
    texfield_list.append(textFunctions.textweiß("2. Der Charakter hat Anfangsstände", 5, 8, textKoerper, 20,1))
    texfield_list.append(textFunctions.textweiß("3. Spiel starten.", 5, 9, textKoerper, 20,1))
    texfield_list.append(textFunctions.textweiß("Das Ziel des Spiels alle gegner erledigen.", 5, 10, textKoerper, 20,1))
    texfield_list.append(textFunctions.textweiß("Mit den Pfeiltasten bewegen oder WASD", 5, 11, textKoerper, 20,1))
    texfield_list.append(textFunctions.textweiß("ANgriff durch bewegen zum Monster", 5, 12, textKoerper, 20,1))
    texfield_list.append(textFunctions.textweiß("Heiltraenke einsetzen mit Zahlentasten: 1, 2, oder 3", 5, 13, textKoerper, 20,1))

    # zurück button
    texfield_list.append(textFunctions.toggleButton("Zuruck", 16, 18, textKoerper, 8, 1))

    
    return {
        "fields": texfield_list,

    }

    
def handle_credits_events(event, anleitung_data, site):
    texfield_list = anleitung_data["fields"]

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