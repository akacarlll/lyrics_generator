import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import time 
import random
from lyrics_generator.pipelines.add_features.sp_settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE


# Configuration pour accéder à l'API Spotify (remplace par tes propres identifiants)
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET

def add_release_year_column(df):
    """
    Ajoute une colonne 'Release_Year' au DataFrame contenant les années de sortie des chansons.

    Paramètres :
    - df : DataFrame contenant les colonnes 'Artist' et 'Title' pour les noms d'artistes et les titres de chansons.

    Retourne :
    - Le DataFrame avec une nouvelle colonne 'Release_Year'.
    - Le nombre total d'appels API effectués.
    """

    # Authentification avec Spotify
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

    # Liste pour stocker les années de sortie
    release_years = []
    api_call_count = 0  # Compteur d'appels API
    consecutive_not_found = 0  # Compteur d'appels "Non trouvé" consécutifs

    for idx, row in df.iterrows():
        artist_name = row['Artist']
        track_name = row['Title']
        query = f'artist:{artist_name} track:{track_name}'

        try:
            # Faire la requête API
            results = sp.search(q=query, type='track', limit=1)
            api_call_count += 1  # Incrémenter le compteur d'appels API
            items = results['tracks']['items']

            if items:
                # Récupérer la date complète de sortie de la première piste trouvée
                release_date = items[0].get('album', {}).get('release_date', None)
                if release_date:
                    release_years.append(release_date)  # Garder la date complète
                    consecutive_not_found = 0  # Réinitialiser le compteur si une date est trouvée
                else:
                    release_years.append("Date inconnue")
                    consecutive_not_found += 1
            else:
                release_years.append("Non trouvé")
                consecutive_not_found += 1

        except Exception as e:
            print(f"Erreur lors de la requête pour {query} : {e}")
            release_years.append("Erreur")
            consecutive_not_found += 1

        # Vérifier si 25 appels consécutifs n'ont pas trouvé de résultat
        if consecutive_not_found >= 25:
            print("25 appels consécutifs sans résultat, remplissage par 'Non trouvé'.")
            release_years.extend(["Non trouvé"] * (len(df) - len(release_years)))
            break

        # Délai pour éviter de dépasser les limites de l'API
        if api_call_count % 60 == 0:
            time.sleep(150) 
        else:
            time.sleep(random.uniform(1, 1.8))
            
    # Ajouter la colonne 'Release_Year' au DataFrame
    df['Release_Year'] = release_years

    return df
