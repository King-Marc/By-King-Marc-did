import cv2
import numpy as np

# Dimensions du bouton (y1, y2, x1, x2)
bouton = [20, 60, 50, 250]

# Fonction qui gère les clics de souris
def process_click(event, x, y, flags, params):
    # Vérifie si le clic est à l'intérieur des dimensions du bouton
    if event == cv2.EVENT_LBUTTONDOWN:
        if y > bouton[0] and y < bouton[1] and x > bouton[2] and x < bouton[3]:
            print('Clic sur le bouton !')

# Crée une fenêtre et attache un rappel de souris
cv2.namedWindow('Contrôle')
cv2.setMouseCallback('Contrôle', process_click)

# Boucle principale pour la capture vidéo
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    # Vérifie si la touche "q" est pressée pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère la capture et ferme la fenêtre
cap.release()
cv2.destroyAllWindows()
