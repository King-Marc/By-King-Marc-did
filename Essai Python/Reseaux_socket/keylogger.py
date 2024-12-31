from pynput import keyboard

def on_key_press(key):
    print(f"Touche pressée : {key}")

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False  # Arrêter le keylogger

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

'''Ce code utilise la bibliothèque "pynput" pour surveiller les événements du clavier, 
en enregistrant les touches pressées et en affichant les informations correspondantes.'''