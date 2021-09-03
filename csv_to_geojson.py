# On importe les modules CSV et JSON
import csv, json
# Import de la librairie GeoJSON et des différents modules pour permettre le formatage des données en GeoJSON
from geojson import Feature, FeatureCollection, Point




# Documentation : https://stackoverflow.com/questions/48586647/python-script-to-convert-csv-to-geojson
# On définit une liste vide de propriétés
features = []
# On ouvre le fichier CSV de l'annuaire dont les données ont été harmonisées
with open('data_annuaire_prepared_output.csv', newline='') as csvfile:
    # Avec la méthode .reader() on retourne un objet : le fichier lu
    reader = csv.reader(csvfile, delimiter=',')
    # Pour chaque colonne dans le fichier lu, on définit le champ de chaque colonne et son numéro d'index
    for row in reader :
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
        # Pour chacun de ces champs   
        for numero, nom, id_service, courriel, telephone, adresse_postale, adresse_service, ville, departement, pays, code_postal, horaires_ouverture, site_internet, code_insee, adresse_carte, latitude, longitude, lien_fa, categorie_service, categorie, service_de_rattachement in reader:
            # les latitudes et longitudes sont définies comme des coordonnées géographiques et des 'float' (décimaux)
            latitude, longitude = map(float, (latitude, longitude))
            # On ajoute à la liste des propriétés
            features.append(
                # Une propriété (Feature) ou chaque "Feature" représente une ligne/institution différente
                Feature(
                    # La latitude et la longitude sont définies comme des coordonnées de type "Point"
                    geometry = Point((longitude, latitude)),
                    # On définit pour chaque propriété ses caractéristiques selon la syntaxe JSON : une clé (key") associée à la valeur de la cellule dans chaque colonne
                    # définie en amont
                    properties = {
                        'Id': numero,
                        'Nom_du_service': nom,
                        'Identifiant_du_service': id_service, 
                        'Courriel': courriel , 
                        'Telephone' : telephone, 
                        'Adresse_postale' : adresse_postale, 
                        'Adresse_du_service': adresse_service,
                        'Ville': ville,
                        'Departement': departement, 
                        'Pays': pays, 
                        'Code_postal': code_postal, 
                        'Horaires_d_ouverture' : horaires_ouverture, 
                        'Site_internet': site_internet, 
                        'Code_insee_commune': code_insee, 
                        'adresse_carte': adresse_carte,
                        'Lien_FranceArchives' : lien_fa, 
                        'Categorie_de_service' : categorie_service, 
                        'Categorie' : categorie, 
                        'Service_de_rattachement': service_de_rattachement
                    }
                )
            )

# On ajoute l'ensemble de ces propriétés dans une "collection de propriétés"
collection = FeatureCollection(features)
# on ouvre un fichier GeoJSON en mode écriture
with open("data_annuaire.geojson", "w") as f:
    # On écrit dans ce fichier le contenu de cette "collection de propriétés"
    f.write('%s' % collection)