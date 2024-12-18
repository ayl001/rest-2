
import json
import requests

def appel_api(ville, appid):

    uri = "https://api.openweathermap.org/data/2.5/forecast?q="
    uri += ville
    uri +="&appid="
    uri += appid

    return requests.get(uri)

CONVERSION_KELVIN_CELSIUS = 273.15
CKC = - CONVERSION_KELVIN_CELSIUS

appid = input("entrez votre clé API :")

for ville in ["Saint-Geours-de-Maremne","Toulouse" ]:
    sm = appel_api(ville, appid)
    texte = sm.text
    donnees = json.loads(texte)

    min_t = [373.5, 373.15, 373.15, 373.15, 373.15] #Hot isn't it ?
    max_t = [0, 0, 0, 0, 0] # Glagla

    # on récupère 40 enregistrement.
    # Pour calculer le min et le max par jour,
    # je récupère les enregistrement de 8 en 8
    # Les min/max seront alors à cheval sur 2 jours
    # Selon l'heure où on appelle le programme
    # Une solution serait de na pas tenir compte
    # des prmières et des dernières prévisions, et
    # de donner les min/max sur 4 jours seulement



    print(f"températures minima et maxima de {ville} sur 5 jours")
    for i in range(5):
        for j in range(8):
            indice = 8 * i + j
            # print(sg_json['list'][indice])
            temp_min = float(donnees['list'][indice]['main']['temp_min'])
            if temp_min < min_t[i]:
                min_t[i] = temp_min

            temp_max = float(donnees['list'][indice]['main']['temp_max'])
            if temp_max > max_t[i]:
                max_t[i] = temp_max

    for i in range(5):
        min_t[i] += CKC
        max_t[i] += CKC
        print(f" Température minimale : {min_t[i]}")
        print(f" Température maximale : {max_t[i]}")
