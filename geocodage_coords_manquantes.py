# Import du module CSV
import csv
# Import du module Nominatim de la librairie Geopy pour pouvoir réaliser le géocodage
from geopy.geocoders import Nominatim

# GÉOCODAGE DES COORDONNÉES MANQUANTES DANS LE FICHIER CSV

# Documentation : Cours de Thibault Clérice - M2 TNAH de l'École nationale des chartes : https://github.com/PonteIneptique/cours-python
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
    fichier_ecrit.writerow(['Id', 'Nom_du_service', 'Identifiant_du_service', 'Courriel', 'Telephone', 'Adresse_postale', 'Adresse_du_service', 'Ville', 'Departement', 'Pays', 'Code_postal', 'Horaires_d_ouverture', 'Site_internet', 'Code_insee_commune', 
        'adresse_carte', 'Latitude', 'Longitude', 'Lien_FranceArchives', 'Categorie_de_service', 'Categorie', 'Service_de_rattachement'])
    

# Pour chaque colonne dans le fichier lu, on définit le champ de chaque colonne et son numéro d'index
    for row in fichier:
        numero=row[0]
        nom= row[1]
        id_service= row[2]
        courriel= row[3]
        telephone= row[4]
        adresse_postale= row[5]
        adresse_service= row[6]
        ville= row[7]
        departement = row[8]
        pays = row[9]
        code_postal= row[10]
        horaires_ouverture= row[11]
        site_internet= row[12]
        code_insee= row[13]
        adresse_carte =row[14]
        latitude= row[15]
        longitude= row[16]
        lien_fa = row[17]
        categorie_service= row[18]
        categorie= row[19]
        service_de_rattachement= row[20]
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
        if not nom :
            nom= "Non communiqué"
        if not id_service :
            id_service= "Non communiqué"
        if not courriel :
            courriel= "Non communiqué"
        if not telephone :
            telephone= "Non communiqué"
        if not adresse_postale :
            adresse_postale= "Non communiqué"
        if not adresse_service:
            adresse_service= "Non communiqué"
        if not ville :
            ville= "Non communiqué"
        if not departement :
            departement = "Non communiqué"
        if not pays :
            pays = "Non communiqué"
        if not code_postal :
            code_postal= "Non communiqué"
        if not horaires_ouverture :
            horaires_ouverture= "Non communiqué"
        if not site_internet :
            site_internet= "Non communiqué"
        if not code_insee :
            code_insee= "Non communiqué"
        if not adresse_carte :
            adresse_carte ="Non communiqué"
        if not lien_fa :
            lien_fa = "Non communiqué"
        if not categorie_service :
            categorie_service= "Non communiqué"
        if not categorie :
            categorie= "Non communiqué"
        if not service_de_rattachement:
            service_de_rattachement= "Non communiqué"
            # Pour toutes ces données
        for i in zip([(latitude, longitude)]):
            # On (ré)écrit dans le fichier dédié à l'écriture le contenu de chaque colonne
            fichier_ecrit.writerow([numero, nom, id_service, courriel, telephone, adresse_postale, adresse_service, ville, departement, pays,code_postal,
                horaires_ouverture, site_internet, code_insee, adresse_carte,  latitude, longitude, lien_fa, categorie_service, categorie,
                service_de_rattachement])
            # On affiche ces valeurs dans le terminal pour s'assurer du succès de l'opération de calcul
            print([numero, nom, adresse_carte, latitude, longitude])