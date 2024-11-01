import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

def get_release_year(df, client_id, client_secret):
    """
    Récupère l'année de sortie pour chaque titre dans la DataFrame.
    
    Paramètres :
    - df : DataFrame contenant les colonnes 'Artist' et 'Track' pour les noms d'artistes et les titres de chansons.
    - client_id : ID client pour l'API Spotify.
    - client_secret : Secret client pour l'API Spotify.
    
    Retourne :
    - Un dictionnaire avec les titres comme clés et leurs années de sortie comme valeurs.
    """
    
    # Authentification avec Spotify
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    
    # Dictionnaire pour stocker l'année de sortie de chaque chanson
    track_release_years = {}
    
    for index, row in df.iterrows():
        artist_name = row['Artist']
        track_name = row['Track']
        
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
                    track_release_years[(artist_name, track_name)] = release_year
                else:
                    track_release_years[(artist_name, track_name)] = "Date inconnue"
            else:
                track_release_years[(artist_name, track_name)] = "Non trouvé"
                
        except Exception as e:
            print(f"Erreur pour le titre '{track_name}' de l'artiste {artist_name}: {e}")
            track_release_years[(artist_name, track_name)] = "Erreur"
    
    return track_release_years
