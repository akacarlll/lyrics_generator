import lyricsgenius as lg
import requests
import pandas as pd 
import random 
import time
import os
from top_20_artist_fr_list import scrape_top_20
from scrapping_wiki import clean_texts



GENIUS_API_TOKEN = '****'
genius = lg.Genius(GENIUS_API_TOKEN)


def _extracted_from_get_artist_id_(search_url, headers, artist_name):
    response = requests.get(search_url, headers=headers, timeout=120)
    response.raise_for_status()  # Vérifie les erreurs HTTP
    data = response.json()

    if 'response' in data and data['response']['hits']:
        return data['response']['hits'][0]['result']['primary_artist']['id']
    print(f"Aucune donnée trouvée pour l'artiste: {artist_name}")
    return None

def get_artist_id(artist_name):
    """Récupère l'ID d'un artiste en utilisant l'API Genius."""
    search_url = f"https://api.genius.com/search?q={artist_name}"
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}

    try:
        return _extracted_from_get_artist_id_(search_url, headers, artist_name)
    except Exception as e:
        print(f"Erreur lors de la récupération de l'ID pour {artist_name}: {e}")
        return None

def get_songs(artist_id, max_songs=500):
    """Récupère jusqu'à un nombre donné de chansons pour un artiste, triées par popularité."""
    songs = []
    page = 1
    
    while len(songs) < max_songs:
        url = f"https://api.genius.com/artists/{artist_id}/songs?page={page}"
        headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
        response = requests.get(url, headers=headers).json()
        songs_data = response['response']['songs']
        
        if not songs_data:
            break  # Sortir si aucune chanson n'est trouvée

        # Récupérer la popularité et ajouter les chansons à la liste
        for song in songs_data:
            if len(songs) < max_songs:  # Assurez-vous de ne pas dépasser max_songs
                songs.append({
                    'title': song['title'],
                    'popularity': song.get('stats', {}).get('pageviews', 0)  # Exemple de mesure de popularité
                })
            else:
                break  # Sortir de la boucle for si le maximum est atteint

        page += 1  # Passer à la page suivante
        time.sleep(random.uniform(1,3))
        
    # Trier manuellement par popularité
    sorted_songs = sorted(songs, key=lambda x: x['popularity'], reverse=True)
    return [song['title'] for song in sorted_songs[:max_songs]]  # Limiter le retour à max_songs

def download_lyrics(song_title, artist_name):
    """Télécharge les paroles d'une chanson donnée."""

    if song := genius.search_song(song_title, artist_name):
        try :
            paroles = song.lyrics
        except Exception as e :
            print(f"Erreur lors de la récupération des paroles : {e}")
            return None

        return paroles, artist_name, song_title
    return None

def all_artist_songs(artist_to_scrape):
    """Télécharge les paroles de toutes les chansons pour chaque artiste et les stocke dans un fichier CSV par artiste."""
    for artist in artist_to_scrape:
        artist_id = get_artist_id(artist)
        if artist_id is None:
            print(f"ID d'artiste non trouvé pour {artist}")

        elif songs := get_songs(artist_id):
            # Créer un répertoire pour l'artiste si il n'existe pas
            os.makedirs("Artiste", exist_ok=True)
            artist_lyrics = [] 
            num=1
            for song in songs:
                if lyrics_info := download_lyrics(song, artist):
                    lyrics, artist, song = lyrics_info
                    artist_lyrics.append({
                        'Artist': artist,
                        'Title': song,
                        'Lyrics': lyrics
                    }) 
                    print(f"Téléchargé : {song} de {artist}")
                    print(f"Chanson numéro : {num}")
                    num +=1
                    sleep_time = random.uniform(0.5,1.5)
                    print(f"Sleeping for {sleep_time:.2f} seconds before the next download...")
                    time.sleep(sleep_time)
                else:
                    print(f"Paroles non trouvées pour {song} de {artist}")

            df = pd.DataFrame(artist_lyrics)
            # Enregistrer le DataFrame dans un fichier CSV
            df.to_csv(f"Artiste/{artist}_songs.csv", index=False, encoding='utf-8')
            print(f"Fichier créé : {artist}/{artist}_songs.csv")
        else:
            print(f"Aucune chanson trouvée pour {artist}")

# Liste d'artistes à scraper
# Remplacez par votre liste d'artistes

#artist_to_scrape = scrape_top_20()
artist_to_scrape = clean_texts()
 


 
# if __name__ == "__main__":
all_artist_songs(artist_to_scrape)  
    


