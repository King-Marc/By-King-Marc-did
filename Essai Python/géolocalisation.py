import phonenumbers
from phonenumbers import geocoder

def geolocate_phone_number(phone_number):
    # Vérifier si le numéro de téléphone est valide
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return "Numéro de téléphone invalide"
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Numéro de téléphone invalide"

    # Obtenir le code du pays à partir du numéro de téléphone
    country_code = phonenumbers.region_code_for_country_code(parsed_number.country_code)

    # Obtenir les informations de géolocalisation à partir du code du pays
    location = geocoder.description_for_valid_number(parsed_number, country_code)

    return location

# Exemple d'utilisation
phone_number = "+243822736690"  # Numéro de téléphone à géolocaliser
location = geolocate_phone_number(phone_number)
print(f"Géolocalisation du numéro {phone_number}: {location}")