import requests

response = requests.get('https://ipinfo.io')
data = response.json()
print("Adresse IP :", data['ip'])
print("Ville :", data['city'])
print("Région :", data['region'])
print("Pays :", data['country'])
'''Ce code utilise le module requests pour effectuer une requête à l'API ipinfo.io et 
récupérer des informations sur l'adresse IP actuelle, y compris la ville, la région et le pays.'''