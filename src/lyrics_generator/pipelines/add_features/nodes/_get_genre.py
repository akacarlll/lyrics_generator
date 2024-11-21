import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Configuration pour accéder à l'API Spotify (remplace par tes propres identifiants)
CLIENT_ID = "c14b20ba16e147ffb6af73cc595b861a"
CLIENT_SECRET = '0e38f48d57264d06a5d6ec44af587f02'
REDIRECT_URI = 'https://github.com/akacarlll/Lyrics-Generator-'  # Assure-toi que cette URL est configurée dans ton application Spotify
SCOPE = 'user-library-read user-read-recently-played'

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
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="c14b20ba16e147ffb6af73cc595b861a", client_secret='0e38f48d57264d06a5d6ec44af587f02'))
    
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
    
    # Ajouter une colonne 'Genre' basée sur le dictionnaire des genres
    df['Genre'] = df['Artist'].map(artist_genres)
    
    return df
