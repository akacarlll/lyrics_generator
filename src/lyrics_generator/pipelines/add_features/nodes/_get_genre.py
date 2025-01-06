import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import time 
import random
from lyrics_generator.pipelines.add_features.sp_settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE

# Configuration pour accéder à l'API Spotify (remplace par tes propres identifiants)
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET


def add_genre_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajoute une colonne 'Genre' à la DataFrame contenant les genres musicaux
    associés à chaque artiste dans la colonne 'Artist'.

    Paramètres :
    - df : DataFrame contenant une colonne 'Artist' avec les noms des artistes.
    - client_id : ID client pour l'API Spotify.
    - client_secret : Secret client pour l'API Spotify.
    
    Retourne :
    - La DataFrame avec une nouvelle colonne 'Genre'.
    """
    # Authentification avec Spotify
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
    
    # Extraire les noms uniques d'artistes
    unique_artists = df['Artist'].unique()
    
    # Dictionnaire pour stocker les genres de chaque artiste
    artist_genres = {}
    
    for artist_name in unique_artists:
        try:
            # Recherche de l'artiste sur Spotify
            results = sp.search(q='artist:' + artist_name, type='artist')
            items = results['artists']['items']
            
            if items:
                # Récupération des genres du premier résultat
                artist_genre = items[0].get('genres', [])
                artist_genres[artist_name] = ", ".join(artist_genre) if artist_genre else "Genre inconnu"
            else:
                artist_genres[artist_name] = "Genre inconnu"
                
        except Exception as e:
            print(f"Erreur pour l'artiste {artist_name}: {e}")
            artist_genres[artist_name] = "Erreur"
        
    wait = random.uniform(0.005,0.01)
    time.sleep(wait)    
    # Ajouter une colonne 'Genre' basée sur le dictionnaire des genres
    df['Genre'] = df['Artist'].map(artist_genres)
    
    return df
