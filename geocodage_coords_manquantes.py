# Import du module CSV
import csv
# Import du module Nominatim de la librairie Geopy pour pouvoir réaliser le géocodage
from geopy.geocoders import Nominatim

# GEOCODAGE DES COORDONNEES MANQUANTES DANS LE FICHIER CSV

# Documentation : Cours de Thibault Clérice - M2 TNAH de l'Ecole nationale des chartes : https://github.com/PonteIneptique/cours-python
# Documentation : https://blog.adrienvh.fr/2015/01/18/geocoder-en-masse-plusieurs-milliers-dadresses-avec-python-et-nominatim/
# Documentation : https://stackoverflow.com/questions/38480909/writing-into-certain-csv-columns-using-python

# Ce script a été écrit d'après le script utilisé pour le géocodage des adresses des autorités nommantes de l'Ark Alliance

csvfile= "data_annuaire_prepared.csv"
# On ouvre le fichier d'entrée en mode lecture (fin) et on ouvre un fichier de sortie en mode écriture (fout)
with open(csvfile, 'r') as fin, open('data_annuaire_prepared_output.csv', 'w') as fout:
    # Avec la méthode .reader() on lit le contenu du fichier d'entrée et on le stocke dans la variable
    # On définit le retour à la ligne comme fin de ligne et la virgule comme délimiteur entre les colonnes
    fichier = csv.reader(fin, lineterminator='\n', delimiter=',')
    # La méthode .writer() nous retourne un objet dans lequel on peut écrire
    # On définit le retour à la ligne comme fin de ligne et la virgule comme délimiteur entre les colonnes
    fichier_ecrit = csv.writer(fout, lineterminator='\n', delimiter=',')
    # Dans le fichier lu, on passe l'en-tête pour ne pas bloquer le calcul des coordonnées géographiques
    next(fichier)
    # Grâce au module Nominatim, on paramètre l'outil de géocodage
    geocoder = Nominatim(user_agent="essai2")
    # Dans le fichier dédié à l'écriture, on écrit la ligne d'en-tête comprenant le nom des différentes colonnes
    fichier_ecrit.writerow(['Nom_du_service', 'Identifiant_du_service', 'Courriel', 'Telephone', 'Adresse_postale', 'Adresse_du_service', 'Ville', 'Code_postal', 'Horaires_d_ouverture', 'Site_internet', 'Code_insee_commune', 
        'adresse_carte', 'Latitude', 'Longitude', 'Lien_FranceArchives', 'Categorie_de_service', 'Categorie', 'Service_de_rattachement'])
    

# Pour chaque colonne dans le fichier lu, on définit le champ de chaque colonne et son numéro d'index
    for row in fichier:
        org_id= row[0]
        nom= row[1]
        id_service= row[2]
        courriel= row[3]
        telephone= row[4]
        adresse_postale= row[5]
        adresse_service= row[6]
        ville= row[7]
        code_postal= row[8]
        horaires_ouverture= row[9]
        site_internet= row[10]
        code_insee= row[11]
        adresse_carte =row[12]
        latitude= row[13]
        longitude= row[14]
        lien_fa = row[15]
        categorie_service= row[16]
        categorie= row[17]
        service_de_rattachement= row[18]
        #  S'il n'y a pas de latitude dans la cellule de la colonne dédiée
        if not latitude:
            # Alors on récupère la valeur de la cellule correspondante dans la colonne "adresse_carte" pour la géocoder
            location = geocoder.geocode(adresse_carte)
            # Et à partir de cette localisation on récupère la latitude
            latitude = location.latitude
        # S'il n'y a pas de longitude dans la cellule de la colonne dédiée
        if not longitude:
            # Alors on récupère la valeur de la cellule correspondante dans la colonne "adresse_carte" pour la géocoder
            location = geocoder.geocode(adresse_carte)    
            # Et à partir de cette localisation on récupère la longitude
            longitude = location.longitude
            # Pour toutes ces données
        for i in zip([(latitude, longitude)]):
            # On (ré)écrit dans le fichier dédié à l'écriture le contenu de chaque colonne
            fichier_ecrit.writerow([nom, id_service, courriel, telephone, adresse_postale, adresse_service, ville, code_postal,
                horaires_ouverture, site_internet, code_insee, adresse_carte,  latitude, longitude, lien_fa, categorie_service, categorie,
                service_de_rattachement])
            # On affiche ces valeurs dans le terminal pour s'assurer du succès de l'opération de calcul
            print([org_id, nom, adresse_carte, latitude, longitude])