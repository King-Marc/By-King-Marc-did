#1. Gestion des erreurs de connexion :
#Tu peux gérer les erreurs de connexion en utilisant des blocs try-except pour capturer les exceptions lors de la création ou de l'utilisation des sockets.

import socket
try:
    # Créer un socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('mauvais_host', 12345))
except socket.error as e:
    print(f"Erreur de connexion : {e}")
#2. Utilisation de context managers :
#Tu peux utiliser des context managers (with) pour gérer automatiquement l'ouverture et la fermeture des sockets.
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 12345))
    s.sendall(b'Hello, serveur')
