#1. Créer un serveur TCP :
import socket
# Créer un socket TCP/IP
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Lier le socket à l'adresse et au port souhaités
serveur.bind(('localhost', 12345))
# Attendre les connexions entrantes
serveur.listen(1)
# Accepter une connexion
connexion, adresse = serveur.accept()
# Recevoir des données
donnees = connexion.recv(1024)
# Fermer la connexion
connexion.close()

#2. Créer un client TCP :
import socket
# Créer un socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se connecter au serveur
client.connect(('localhost', 12345))
# Envoyer des données
client.sendall(b'Hello, serveur')
# Fermer la connexion
client.close()
