import pygame
import textFunctions
import grid

def create_registration_fields(ueberschrift, textKoerper):
    texfield_list = []
    
    # Title "REGISTRIERUNG"
    texfield_list.append(textFunctions.textField("REGISTRIERUNG", 14, 3, ueberschrift, 12))
    
    # Name field
    texfield_list.append(textFunctions.textField("Name", 12, 7, textKoerper, 5))
    name_input = textFunctions.textInput(19, 7, textKoerper, 10, 1)
    texfield_list.append(name_input)
    
    # Password field
    texfield_list.append(textFunctions.textField("PASSWORT", 12, 9, textKoerper, 5))
    password_field = textFunctions.textInput(19, 9, textKoerper, 10, 1)
    password_field.is_password = True
    password_field.show_password = False
    texfield_list.append(password_field)
    
    # Repeat password field
    texfield_list.append(textFunctions.textField("PASSWORT WIEDERHOLEN", 8, 11, textKoerper))
    repeat_field = textFunctions.textInput(19, 11, textKoerper, 10, 1)
    repeat_field.is_password = True
    repeat_field.show_password = False
    texfield_list.append(repeat_field)
    
    # Show password button
    texfield_list.append(textFunctions.toggleButton("PASSWORT ANZEIGEN", 30, 9, textKoerper, 8, 1))
    
    # Error message (initially hidden)
    error_msg = textFunctions.textField("---", 12, 13, textKoerper, 17)
    error_msg.color = (255, 0, 0)  # Red color for error
    texfield_list.append(error_msg)
    
    # Back and Register buttons
    texfield_list.append(textFunctions.toggleButton("ZURUCK", 12, 15, textKoerper, 8, 1))
    texfield_list.append(textFunctions.toggleButton("REGISTRIEREN", 21, 15, textKoerper, 8, 1))
    
    return {
        "fields": texfield_list,
        "name_input": name_input,
        "password_field": password_field,
        "repeat_field": repeat_field,
        "error_msg": error_msg
    }

def handle_registration_events(event, registration_data, site):
    texfield_list = registration_data["fields"]
    name_input = registration_data["name_input"]
    password_field = registration_data["password_field"]
    repeat_field = registration_data["repeat_field"]
    error_msg = registration_data["error_msg"]

    if event.type == pygame.MOUSEBUTTONDOWN:
        posx, posy = pygame.mouse.get_pos()
        
        for field in texfield_list:
            if isinstance(field, textFunctions.textInput):
                if field.rec.collidepoint(posx, posy):
                    field.active = True
                else:
                    field.active = False
                    
            elif isinstance(field, textFunctions.toggleButton) and field.rec.collidepoint(posx, posy):
                if field.text == "PASSWORT ANZEIGEN":
                    # Toggle password visibility for all password fields
                    for input_field in texfield_list:
                        if isinstance(input_field, textFunctions.textInput) and input_field.is_password:
                            input_field.show_password = not input_field.show_password
                elif field.text == "ZURUCK":
                    site = 1  # Back to login
                elif field.text == "REGISTRIEREN":
                    # Validate registration
                    if not name_input.text.strip():
                        error_msg.text = "NAME EINGEBEN"
                    elif not password_field.real_text.strip():
                        error_msg.text = "PASSWORT EINGEBEN"
                    elif password_field.real_text != repeat_field.real_text:
                        error_msg.text = "PASSWORTER STIMMEN NICHT UEBEREIN"
                    else:
                        # Add actual registration logic here
                        site = 3  # Go to main menu
    
    if event.type == pygame.KEYDOWN:
        for field in texfield_list:
            if isinstance(field, textFunctions.textInput) and field.active:
                if event.key == pygame.K_BACKSPACE:
                    field.text = field.text[:-1]
                    if field.is_password:
                        field.real_text = field.real_text[:-1]
                else:
                    char = event.unicode.replace("ü", "u").replace("ö", "o").replace("ä", "a").replace("ß", "ss").replace("Ü", "U").replace("Ö", "O").replace("Ä", "A")
                    if field.is_password:
                        field.real_text += char
                        field.text += "*" if not field.show_password else char
                    else:
                        field.text += char
    
    return site