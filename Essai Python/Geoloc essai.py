import requests

def geolocate_phone_number(phone_number):
    # Remplacez "YOUR_API_KEY" par votre clé d'API Google Maps
    api_key = "YOUR_API_KEY"
    
    # URL de l'API de géolocalisation de Google Maps
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={phone_number}&key={api_key}"
    
    # Envoi de la requête GET à l'API
    response = requests.get(url)
    
    # Analyse de la réponse JSON
    data = response.json()
    
    # Récupération des informations de localisation
    if data['status'] == 'OK':
        results = data['results']
        if results:
            location = results[0]['formatted_address']
            print(f"La localisation du téléphone {phone_number} est : {location}")
        else:
            print("Aucune localisation trouvée pour ce numéro de téléphone.")
    else:
        print("Une erreur s'est produite lors de la géolocalisation du numéro de téléphone.")

# Utilisation de la fonction pour géolocaliser un numéro de téléphone
geolocate_phone_number("=243828609709")