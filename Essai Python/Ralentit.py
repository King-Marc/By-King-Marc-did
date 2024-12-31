import cv2

# Ouvrir la vidéo d'entrée
input_video = cv2.VideoCapture("D:\VIDEOS/Bizarre.mp4")

# Obtenir les dimensions de la vidéo
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = input_video.get(cv2.CAP_PROP_FPS)

# Créer un objet VideoWriter pour écrire la vidéo de sortie
output_video = cv2.VideoWriter("D:\VIDEOS/Bizarre.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps*0.02, (width, height))

# Lire chaque image de la vidéo d'entrée et l'écrire dans la vidéo de sortie
while True:
    ret, frame = input_video.read()
    if not ret:
        break

    # Écrire le même frame 50 fois pour ralentir la vidéo à ×0.02
    for _ in range(50):
        output_video.write(frame)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break

# Libérer les ressources
input_video.release()
output_video.release()
cv2.destroyAllWindows()