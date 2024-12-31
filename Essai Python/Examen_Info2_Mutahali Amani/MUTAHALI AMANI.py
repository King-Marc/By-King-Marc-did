def get_statistics(self, date):
        # convertir date string en datetime object
        date_obj = datetime.strptime(date, '%d %m %Y')

        # Filtrer les données par date(j’ai vu sur YouTube hein jsavais pas
        data_filtered = [line.split(';') for line in self.data if line.startswith(date_obj.strftime('%d/%m/%Y'))]

        # Pour calculer le stat
        global_active_power = sum([float(line[2]) for line in data_filtered]) / len(data_filtered)
        global_reactive_power = max([float(line[4]) for line in data_filtered])
        voltage = sum([float(line[5]) for line in data_filtered]) / len(data_filtered)
        time_max_voltage = max(data_filtered, key=lambda x: float(x[5]))[0]

        # Afficher le stat du dico
        return {
            'Date': date,
            'La moyenne de Global_active_power': global_active_power,
            'La plus grande valeur du Global_reactive_power pour cette date': global_reactive_power,
            'Le voltage moyen pour cette date': voltage,
            'Leur a laquelle le voltage était plus élevé durant cette date': time_max_voltage
        }
#pour faire appel au fichier essaie ça 
p = ('Power.txt')
stats = p.get_statistics(16 12 2006)
print(stats)

    