import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import socket

class ScreenshotApp(App):
    def build(self):
        # Créer un socket pour la communication
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Définir l'adresse IP et le port du serveur
        self.host = '127.0.0.1'  # Adresse IP du serveur
        self.port = 12345  # Port utilisé par le serveur

        # Créer la disposition de l'interface utilisateur
        layout = BoxLayout(orientation='vertical')

        # Créer un bouton pour capturer l'écran
        capture_button = Button(text='Capture', size_hint=(1, 0.2))
        capture_button.bind(on_release=self.capture_screen)
        layout.add_widget(capture_button)

        # Créer une image pour afficher la capture d'écran
        self.image = Image()
        layout.add_widget(self.image)

        return layout

    def capture_screen(self, instance):
        try:
            # Se connecter au serveur
            self.s.connect((self.host, self.port))

            # Envoyer la commande "capture" pour capturer l'écran
            self.s.sendall("capture".encode())

            # Recevoir l'image capturée du serveur
            data = b""
            while True:
                chunk = self.s.recv(1024)
                if not chunk:
                    break
                data += chunk

            # Enregistrer l'image capturée
            with open("screenshot.png", "wb") as file:
                file.write(data)

            # Afficher l'image capturée
            self.image.source = "screenshot.png"

            # Fermer la connexion
            self.s.sendall("exit".encode())
            self.s.close()

        except Exception as e:
            # Afficher une fenêtre contextuelle avec l'erreur
            popup = Popup(title='Erreur', content=Label(text=str(e)), size_hint=(None, None), size=(400, 400))
            popup.open()

if __name__ == '__main__':
    ScreenshotApp().run()