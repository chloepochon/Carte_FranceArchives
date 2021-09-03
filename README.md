# Carte des services partenaires de _FranceArchives_

  :world_map: **Présentation du projet**

Cette carte a été développée par Chloé Pochon durant le stage réalisé au Service interministériel des Archives de France (SIAF), dans le cadre de la deuxième année de master "Technologies numériques appliquées à l'histoire" de l'École nationale des chartes.
La carte représente l'ensemble des services d'archives partenaires de _FranceArchives_ au 12 juillet 2021 et indique leurs informations pratiques. Il s'agit d'une maquette en vue de la refonte de la carte [encore disponible actuellement](https://francearchives.fr/fr/annuaire/departements) sur le portail.


 
:gear: **Les fonctionnalités**

Le projet comprend :
* Le fichier CSV de données brutes et harmonisées : `data_annuaire_prepared.csv`
* Le script Python permettant le calcul des coordonnées géographiques manquantes dans le premier fichier CSV : `geocodage_coords_manquantes.py`
* Le fichier CSV  de sortie reprenant l'ensemble des données de l'annuaire : `data_annuaire_prepared_output.csv`
* Un script Python permettant le formatage de l'ensemble de ces données en GeoJSON : `csv_to_geojson.py`
* Un fichier CSS et un fichier JavaScript dans leur dossier respectif pour le panneau latéral.
* Les différents fichiers GeoJSON :
  - Un pour les différents pays du monde : `geojson_layers/world_medium_without_france2.json`
  - Un pour la métropole : `geojson_layers/metropole.geojson`
  - Un pour les départements métropolitains : `geojson_layers/departements.geojson`
  - Un pour les départements d'outre-mer : `geojson_layers/departements_outre_mer_uniquement.json`
  - Un pour les marqueurs indiquant l'emplacement des services : `data_annuaire.geojson`
* Deux fichiers HTML :
  - L'un pour l'affichage de la carte seule : `Carte_FA_seule.html`
  - L'autre pour l'affichage de la carte dans l'environnement graphique du portail _FranceArchives_ : `Carte_FranceArchives.html`

  
:desktop_computer: **Installation et lancement**
 
 * Via son terminal, l'utilisateur doit créer un environement virtuel dans un dossier de son choix : `virtualenv env -p python3`
 * L'utilisateur devra installer des packages et libraries : 
  1. Pour cela il doit sourcer son environnement virtuel 
    -> dans le dossier choisi faire la commande `source env/bin/activate` 
  2.  Puis : 
       - Geopy : `pip install geopy`
       - GeoJSON : `pip install geojson`
       
  OU installer les packages nécessaires directement avec la commande `pip install -r requirements.txt`
  
  3. Vérifier que tout est bien installé : `pip freeze`
  4. Désactiver l'environnement : `deactivate`
 
 * Enfin l'utilisateur devra cloner le dossier : `git clone https://github.com/chloepochon/Carte_FranceArchives`
 
 * Il pourra alors lancer la carte : 
    - Via le terminal dans le dossier du projet, simuler le serveur HTTP : `python3 -m http.server`
    - Aller sur http://0.0.0.0:8000/ 
    - Cliquer sur `Carte_FA_seule.html` pour visualiser la carte seule ou `Carte_FranceArchives.html` pour visualiser la carte telle qu'elle pourrait être publiée sur le portail _FranceArchives_.



* Si l'utilisateur souhaite utiliser la fonction de géocodage, dans le terminal :
   - Sourcer l'environnement virtuel : `source env/bin/activate`
   - Pour le géocodage : `python geocodage_coords_manquantes.py`
   - Pour le formatage en GeoJSON : `python csv_to_geojson.py`
  
