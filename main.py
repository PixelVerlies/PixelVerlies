import pygame
import grid
import login_screen
import registration_screen
import menu_screen
import credits_screen
import anleitung_screen
import character_screen
import sys
from database import database
import dungeonEnd
import map
import createDungeon


data = database()
data.connection()

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()
ueberschrift = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 45)
textKoerper = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 25)

blockSize = 25
fild_leng = int(WIDTH / blockSize)
fild_high = int(HEIGHT / blockSize)

# 1 = Login, 2 = Registration, 3 = Main Menu, 4 = Credits, 5 = Anleitung, 6 = Start, 7 = Character
current_site = 1 # Startet immer auf dem Login-Screen

wall = grid.importImage("Images/Dungeon/wall.png", blockSize)

run = True

rod = None
charac = None
door_list = None
all_rooms = None
created = False
counter = 90
chr_id = 0
level_id = 0

# Initialisiere alle Screen-Daten
login_data = login_screen.create_login_fields(ueberschrift, textKoerper)
registration_data = registration_screen.create_registration_fields(ueberschrift, textKoerper)
# menu_data wird erst bei erfolgreichem Login erstellt, um die current_player_id zu nutzen
menu_data = None 
credits_data = credits_screen.create_credits_fields(ueberschrift, textKoerper)
anleitung_data = anleitung_screen.create_anleitung_fields(ueberschrift, textKoerper)

character_data = {
    "fields": [],
    "char_name_input": None,
    "selected_character_id": None,
    "fertig_button": None,
    "character_image_path": None,
    "weapon_table_headers": [],
    "weapon_table_data": [],
    "weapon_table_rects": []
}

current_player_id = None # Initialisiere mit None, da noch kein Spieler eingeloggt ist

while run:
    # Temporäre Variable für den nächsten Screen-Zustand.
    # Standardmäßig bleibt es der aktuelle Screen, es sei denn ein Handler ändert es explizit.
    next_site_state = {'site': current_site, 'player_id': current_player_id}

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: 
            run = False
            break 
        
        if current_site == 1:  # Login-Screen
            # handle_login_events gibt jetzt ein Dictionary mit 'site' und ggf. 'player_id' zurück
            # oder ein Signal zum Beenden
            action_result = login_screen.handle_login_events(event, login_data, current_site)
            
            if action_result == "QUIT": # Signal zum Beenden des Spiels
                run = False
                break
            elif isinstance(action_result, dict): # Ergebnis eines Handlers ist ein Dictionary
                if action_result.get('site') == 3: # Erfolgreicher Login
                    next_site_state['site'] = 3
                    next_site_state['player_id'] = action_result.get('player_id')
                    current_player_id = next_site_state['player_id'] # Update globale ID
                    # Menüdaten hier erstellen, nachdem current_player_id bekannt ist
                    menu_data = menu_screen.create_menu_fields(ueberschrift, textKoerper)
                elif action_result.get('site') == 2: # Wechsel zur Registrierung
                    next_site_state['site'] = 2
                # Ansonsten (wenn action_result.get('site') == 1), bleibt next_site_state['site'] 1, was korrekt ist.
            
        elif current_site == 2:  # Registration-Screen
            result_site = registration_screen.handle_registration_events(event, registration_data, current_site)
            next_site_state['site'] = result_site
        
        elif current_site == 3: # Main Menu Screen
            if menu_data is not None:
                prev_selected_character_id = menu_data["selected_character"]
                result_site, chr_id, level_id = menu_screen.handle_menu_events(event, menu_data, current_site, current_player_id)
                next_site_state['site'] = result_site
                if next_site_state['site'] == 7 and menu_data["selected_character"] != prev_selected_character_id:
                    character_data = character_screen.create_character_fields(ueberschrift, textKoerper, menu_data["selected_character"])
                elif next_site_state['site'] == 3 and prev_selected_character_id is not None:
                    menu_data["selected_character"] = None
            else:
                # Dies sollte nicht passieren, wenn der Flow korrekt ist, aber als Fallback
                print("DEBUG: Fehler: menu_data ist None auf Site 3. Rückkehr zum Login.")
                next_site_state['site'] = 1 # Zurück zum Login

        elif current_site == 4: # Credits Screen
            result_site = credits_screen.handle_credits_events(event, credits_data, current_site)
            next_site_state['site'] = result_site

        elif current_site == 5: # Anleitung Screen
            result_site = anleitung_screen.handle_credits_events(event, anleitung_data, current_site)
            next_site_state['site'] = result_site

        elif current_site == 7: # Character Screen
            result_site = character_screen.handle_character_events(event, character_data, current_site)
            next_site_state['site'] = result_site
            if next_site_state['site'] == 3:
                # Menüdaten neu laden, wenn vom Charakterbildschirm zurück ins Menü
                menu_data = menu_screen.create_menu_fields(ueberschrift, textKoerper)
    

    current_site = next_site_state['site']
    current_player_id = next_site_state['player_id'] # Stelle sicher, dass player_id auch aktualisiert wird
    
    SCREEN.fill(BLACK)
    grid.drawGrid(WIDTH, HEIGHT, blockSize, SCREEN, wall)

    # Zeichne den aktuellen Screen basierend auf dem 'current_site' Wert
    if current_site == 1:
        for field in login_data["fields"]:
            field.drawField(blockSize, SCREEN)
    elif current_site == 2:
        for field in registration_data["fields"]:
            field.drawField(blockSize, SCREEN)
    elif current_site == 3:
        created = False
        if menu_data is not None: # Sicherstellen, dass menu_data existiert
            for field in menu_data["fields"]:
                field.drawField(blockSize, SCREEN)
            menu_screen.draw_character_table(menu_data, blockSize, SCREEN, current_player_id, textKoerper)
    elif current_site == 7: 
        character_screen.draw_character_screen(character_data, blockSize, SCREEN, textKoerper)
    elif current_site == 4:
        for field in credits_data["fields"]:
            field.drawField(blockSize, SCREEN)
    elif current_site == 5:
        for field in anleitung_data["fields"]:
            field.drawField(blockSize, SCREEN)
    elif current_site == 6:
        if created == False:
            rod, charac, door_list, all_rooms = createDungeon.create(data, blockSize, fild_leng, fild_high, level_id, chr_id)
            created = True
            counter = 90
        if rod.end == 0:
            rod.roundRun(events, charac, door_list, all_rooms)
            map.drawGamefild(rod, charac, SCREEN, blockSize, textKoerper)
        else:
            counter, current_site = dungeonEnd.dungeonEnd(rod, fild_leng, fild_high, SCREEN, blockSize, ueberschrift, counter, data, charac, current_site)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()