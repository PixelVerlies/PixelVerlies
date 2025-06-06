import pygame
import textFunctions
import grid

def create_anleitung_fields(ueberschrift, textKoerper, site):
    texfield_list = []
    
    # Title "Hauptmenü"
    texfield_list.append(textFunctions.textField("Anleitung", 14, 2, ueberschrift, 12))

    #Textfeld komplett

    match site:
        case 1:
            texfield_list.append(textFunctions.textField("Charakter erstellen", 5, 6, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("1. Namen Eingeben", 5, 8, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("2. Klasse Wählen", 5, 9, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("3. Speichern", 5, 10, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("Charakter bearbeiten", 5, 13, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("1. Charakter doppelt anklicken", 5, 15, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("2. Waffe kann durch das anklicken einer anderen gewechselt werden", 5, 16, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("3. Mit Fertig kann die Seite verlassen werden", 5, 17, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.toggleButton("Seite 2", 33, 21, textKoerper, 5, 1))
        case 2:
            texfield_list.append(textFunctions.textField("Spiel starten", 5, 6, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("1. Charakter mit dem gespielt werden soll einmal anklicken", 5, 8, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("2. Level auswählen", 5, 9, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("3. Start anklicken", 5, 10, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("Spielablauf", 5, 13, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("- Das Spiel läuft Rundenbasiert ab", 5, 15, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("- Pro Runde kann man einmal angriefen und einen Heiltrank nehmen", 5, 16, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("- Nach dem Charakter sind die einzelnen Gegner dran", 5, 17, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("- Der Dungeon ist gewonnen wenn alle Gegner besiegt sind", 5, 18, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.toggleButton("Seite 1", 2, 21, textKoerper, 5, 1))
            texfield_list.append(textFunctions.toggleButton("Seite 3", 33, 21, textKoerper, 5, 1))
        case 3:
            texfield_list.append(textFunctions.textField("Steuerung ", 5, 6, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("- Mit WASD oder den Pfeiltasten kann der Charakter gesteuert werden", 5, 8, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("- Um einen Gegner anzugreifen, mache einen Schritt auf ihn zu", 5, 9, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("während du direkt neben ihm stehst", 5, 10, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.textField("- Die Heiltränke können über die Tasten 1,2,3 genommen werden", 5, 11, textKoerper, 30, 1, 1))
            texfield_list.append(textFunctions.toggleButton("Seite 2", 2, 21, textKoerper, 5, 1))

    # zurück button
    texfield_list.append(textFunctions.toggleButton("Zuruck", 16, 21, textKoerper, 8, 1))

    
    return {
        "fields": texfield_list,

    }

    
def handle_anleitung_events(event, anleitung_data, site, text_site):
    texfield_list = anleitung_data["fields"]

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        for field in texfield_list:                    
            if isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "Zuruck":
                    site = 3 #zurück zum hauptmenü
                if field.text == "Seite 1":
                    text_site = 1 
                if field.text == "Seite 2":
                    text_site = 2 
                if field.text == "Seite 3":
                    text_site = 3

    return site, text_site