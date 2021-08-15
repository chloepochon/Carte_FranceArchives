# Carte des services partenaires de _FranceArchives_

  :world_map: **Présentation du projet**

Cette carte a été développée durant mon stage réalisé au SIAF dans le cadre de ma deuxième année de master "Technologies numériques appliquées à l'Histoire" de l'Ecole nationale des chartes.
La carte représente l'ensemble des services d'archives partenaires de _FranceArchives_ au 12 juillet 2021 et indique leurs informations pratiques. Elle devrait remplacer celle (encore disponible actuellement) [https://francearchives.fr/fr/annuaire/departements] sur le portail.


 
:gear: **Les fonctionnalités**

Le projet comprend :
* Le fichier CSV reprenant l'ensemble des données de l'annuaire qui ont été enrichies.
* Un script Python permettant le calcul des coordonnées géographiques manquantes dans le fichier CSV.
* Un script Python permettant le formatage de l'ensemble des données en GeoJSON.
* Un fichier CSS et un fichier JavaScript dans leur dossier respectif pour le panneau latéral.
* Les différents fichiers GeoJSON :
  - Un pour les différents pays du monde.
  - Un pour la métropole.
  - Un pour les départements métropolitains.
  - Un pour les départements d'outre mer.
  - Un pour les marqueurs indiquant l'emplacement des services.
* Deux fichiers HTML :
  - L'un pour l'affichage de la carte seule.
  - L'autre pour l'affichage de la carte dans l'environnement graphique du portail _FranceArchives_.


  
:desktop_computer: **Installation et lancement**
 
 * Via son terminal, l'utilisateur-ice doit créer un environement virtuel dans un dossier de son choix : `virtualenv env -p python3`
 * L'utilisateur-ice devra installer des packages et libraries : 
  1. Pour cela il doit sourcer son environnement virtuel 
    -> dans le dossier choisi faire la commande `source env/bin/activate` 
  2.  Puis : 
       - Geopy : `pip install geopy`
       - GeoJSON : `pip install geojson`
       
  OU installer les packages nécessaires directement avec la commande `pip install -r requirements.txt`
  
  3. Vérifier que tout est bien installé : `pip freeze`
  4. Désactiver l'environnement : `deactivate`
 
 * Enfin l'utilisateur-ice devra cloner le dossier : `git clone https://github.com/chloepochon/Carte_FranceArchives`
 
 * Il pourra alors lancer la carte : 
    - Via le terminal dans le dossier du projet, simuler le serveur HTTP : `python3 -m http.server`
    - Aller sur http://0.0.0.0:8000/ 
    - Cliquer sur Carte_FA_seule.html pour visualiser la carte seule ou Carte_FranceArchives.html pour visualiser la carte telle qu'elle pourrait être publiée sur le portail _FranceArchives_.
  
