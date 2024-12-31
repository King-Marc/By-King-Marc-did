'''Utilisation de threads pour la gestion de plusieurs connexions simultanées
'''

import socket
import threading

def handle_client(conn):
    data = conn.recv(1024)
    conn.sendall(data)
    conn.close()

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('localhost', 12345))
serveur.listen(5)

while True:
    conn, addr = serveur.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn,))
    client_thread.start()
