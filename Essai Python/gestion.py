import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

class EmployeeManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion du Personnel")
        self.setGeometry(100, 100, 600, 400)

        # Connexion à la base de données SQLite
        self.conn = sqlite3.connect("entreprise.db")
        self.cursor = self.conn.cursor()

        # Création de la table "employes"
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employes (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            heure_arrivee TEXT,
            heure_depart TEXT,
            contrat TEXT
        )
    """)
        self.conn.commit()

        # Interface utilisateur
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        self.label = QLabel("Nom de l'employé:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name_input)

        self.add_button = QPushButton("Ajouter Employé")
        self.add_button.clicked.connect(self.add_employee)
        self.layout.addWidget(self.add_button)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def add_employee(self):
        nom = self.name_input.text()
        # Ajoutez ici la logique pour enregistrer l'employé dans la base de données
        # (heure d'arrivée, heure de départ, contrat, etc.)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeManagementApp()
    window.show()
    sys.exit(app.exec_())
