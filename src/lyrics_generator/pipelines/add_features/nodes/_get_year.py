import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import time 
import random
from conf.local.settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE

# Configuration pour accéder à l'API Spotify (remplace par tes propres identifiants)
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET
 

def add_release_year_column(df):
    """
    Ajoute une colonne 'Release_Year' au DataFrame contenant les années de sortie des chansons.
    
    Paramètres :
    - df : DataFrame contenant les colonnes 'Artist' et 'Title' pour les noms d'artistes et les titres de chansons.
    - client_id : ID client pour l'API Spotify.
    - client_secret : Secret client pour l'API Spotify.
    
    Retourne :
    - Le DataFrame avec une nouvelle colonne 'Release_Year'.
    """
    
    # Authentification avec Spotify
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="c14b20ba16e147ffb6af73cc595b861a", client_secret='0e38f48d57264d06a5d6ec44af587f02'))
    
    # Liste pour stocker les années de sortie
    release_years = []
    
    for index, row in df.iterrows():
        artist_name = row['Artist']
        track_name = row['Title']
        
        try:
            # Recherche de la chanson sur Spotify
            results = sp.search(q=f'artist:{artist_name} track:{track_name}', type='track', limit=1)
            items = results['tracks']['items']
            
            if items:
                # Récupérer l'année de sortie de la première piste trouvée
                release_date = items[0].get('album', {}).get('release_date', None)
                if release_date:
                    # Extraire uniquement l'année
                    release_year = release_date.split("-")[0]
                    release_years.append(release_year)
                else:
                    release_years.append("Date inconnue")
            else:
                release_years.append("Non trouvé")
                
        except Exception as e:
            print(f"Erreur pour le titre '{track_name}' de l'artiste {artist_name}: {e}")
            release_years.append("Erreur")
        wait = random.uniform(0.001,0.02)
        time.sleep(wait)
    # Ajouter la colonne 'Release_Year' au DataFrame
    df['Release_Year'] = release_years
    
    return df
