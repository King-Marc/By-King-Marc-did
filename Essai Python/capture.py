import socket

# Créer un socket pour la communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Définir l'adresse IP et le port du serveur
host = '127.0.0.1'  # Adresse IP du serveur
port = 12345  # Port utilisé par le serveur

# Se connecter au serveur
s.connect((host, port))
print(f"Connecté au serveur {host}:{port}")

# Envoyer la commande "capture" pour capturer l'écran
s.sendall("capture".encode())

# Recevoir l'image capturée du serveur
data = b""
while True:
    chunk = s.recv(1024)
    if not chunk:
        break
    data += chunk

# Enregistrer l'image capturée
with open("screenshot.png", "wb") as file:
    file.write(data)

print("Capture d'écran reçue")

# Fermer la connexion
s.sendall("exit".encode())
s.close()
print("Connexion terminée")