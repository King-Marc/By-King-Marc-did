import tkinter as tk
import cv2

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Ouvrir la source vidéo
        self.vid = MyVideoCapture(video_source)

        # Créer un canvas de la taille de la vidéo
        self.canvas = tk.Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Mettre à jour l'affichage de la vidéo
        self.update()

        # Bouton pour prendre une capture d'écran
        self.snapshot_button = tk.Button(window, text="Capture", command=self.snapshot, font=('Arial',15), bg= '#4286f4', 
        fg= 'white', relief= 'flat', padx= 10)
        self.snapshot_button.pack()

        self.window.mainloop()

    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = tk.PhotoImage(data=cv2.imencode('.ppm', frame)[1].tobytes())
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)

    def snapshot(self):
        ret, frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Impossible d'ouvrir la source vidéo", video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

# Créer une fenêtre et la passer à l'objet Application
App(tk.Tk(), "Capture vidéo avec Tkinter et OpenCV")
