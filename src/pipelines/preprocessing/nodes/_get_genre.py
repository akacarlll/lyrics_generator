
import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

def get_genre(df, client_id, client_secret):
    """
    Récupère le genre musical pour chaque artiste unique dans la colonne 'Artist' d'une DataFrame.

    Paramètres :
    - df : DataFrame contenant une colonne 'Artist' avec les noms des artistes.
    - client_id : ID client pour l'API Spotify.
    - client_secret : Secret client pour l'API Spotify.
    
    Retourne :
    - Un dictionnaire avec les artistes comme clés et leurs genres respectifs comme valeurs.
    """
    
    # Authentification avec Spotify
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    
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
                # Récupération du genre du premier résultat
                artist_genre = items[0].get('genres', [])
                artist_genres[artist_name] = artist_genre
            else:
                # Si aucun résultat n'est trouvé, on enregistre une liste vide
                artist_genres[artist_name] = []
                
        except Exception as e:
            print(f"Erreur pour l'artiste {artist_name}: {e}")
            artist_genres[artist_name] = []

    return artist_genres
