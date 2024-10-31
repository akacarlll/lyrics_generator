from lyricsgenius import Genius
import lyricsgenius as lg
import requests
import requests
import pandas as pd 
import numpy as np
import random 
from bs4 import BeautifulSoup

from tqdm import tqdm 
import os


class ArtistLyricsScraper:
    def __init__(self, GENIUS_API_TOKEN, artist_to_scrape) :
        self.GENIUS_API_TOKEN = GENIUS_API_TOKEN
        self.genius = lg.Genius(GENIUS_API_TOKEN)
        self.artist_to_scrape = artist_to_scrape
        
    def get_artist_id(self, artist_name):
        """Récupère l'ID d'un artiste en utilisant l'API Genius."""
        search_url = f"https://api.genius.com/search?q={artist_name}"
        headers = {'Authorization': 'Bearer ' + self.GENIUS_API_TOKEN}
        
        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()  # Vérifie les erreurs HTTP
            data = response.json()
            
            # Vérifie si la réponse contient la clé 'response'
            if 'response' in data and data['response']['hits']:
                return data['response']['hits'][0]['result']['primary_artist']['id']
            
            print(f"Aucune donnée trouvée pour l'artiste: {artist_name}")
            return None
        except Exception as e:
            print(f"Erreur lors de la récupération de l'ID pour {artist_name}: {e}")
            return None

    def get_songs(self, artist_id, max_songs=100):
        """Récupère jusqu'à un nombre donné de chansons pour un artiste, triées par popularité."""
        songs = []
        page = 1
        while len(songs) < max_songs:
            url = f"https://api.genius.com/artists/{artist_id}/songs?page={page}"
            headers = {'Authorization': 'Bearer ' + self.GENIUS_API_TOKEN}
            response = requests.get(url, headers=headers).json()
            songs_data = response['response']['songs']
            if not songs_data:
                break

            # Récupérer la popularité et trier manuellement (si disponible)
            for song in songs_data:
                if len(songs) >= max_songs:  # Stopper si on atteint la limite
                    break
                songs.append({
                    'title': song['title'],
                    'popularity': song.get('stats', {}).get('pageviews', 0)  # Exemple de mesure de popularité
                })

            page += 1

        # Trier manuellement par popularité
        sorted_songs = sorted(songs, key=lambda x: x['popularity'], reverse=True)
        return [song['title'] for song in sorted_songs]

    def download_lyrics(self, song_title, artist_name):
        """Télécharge les paroles d'une chanson donnée."""

        song = genius.search_song(song_title, artist_name)
        if song : 
            try :
                paroles = song.lyrics
                year = song.release_date.year if song.release_date else None
            except Exception as e :
                return None
        
            return paroles, artist_name, song_title, year 
        return None

    def all_artist_songs(self):
        """Télécharge les paroles de toutes les chansons pour 
        chaque artiste et les stocke dans un fichier par artiste."""
        for artist in self.artist_to_scrape:
            artist_id = self.get_artist_id(artist)
            if artist_id is not None:
                songs = self.get_songs(artist_id)
                if songs:
                    # Créer un répertoire pour l'artiste si il n'existe pas
                    os.makedirs(artist, exist_ok=True)
                    artist_lyrics = []  # Liste pour stocker les paroles de toutes les chansons

                    for song in songs:
                        lyrics = self.download_lyrics(song, artist)
                        if lyrics:
                            artist_lyrics.append(f"{song}\n{lyrics}\n")  # Ajouter les paroles au contenu de l'artiste
                            print(f"Téléchargé : {song} de {artist}")
                        else:
                            print(f"Paroles non trouvées pour {song} de {artist}")

                    # Créer un fichier texte pour l'artiste contenant toutes les chansons
                    with open(f"{artist}/{artist}_songs.txt", 'w', encoding='utf-8') as file:
                        file.write("\n".join(artist_lyrics))
                        print(f"Fichier créé : {artist}/{artist}_songs.txt")
                else:
                    print(f"Aucune chanson trouvée pour {artist}")
            else:
                print(f"ID d'artiste non trouvé pour {artist}")

# Liste d'artistes à scraper
# Remplacez par votre liste d'artistes
"""
artist_to_scrape = ['GIMS',
 'TIAKOLA',
 'GUY2BEZBAR',
 'LETO',
 'SDM',
 'CARBONNE',
 'BOOBA',
 'NINHO & NISKA',
 'SEVDALIZA, PABLLO VITTAR, YSEULT',
 'LACRIM',
 'LAYLOW',
 'AMK',
 'KEBLACK',
 'FLOYYMENOR, CRIS MJ',
 'KAROL G',
 'DISTURBED',
 'THEODORT',
 'BOUSS',
 'SABRINA CARPENTER']"""
 
    
#if __name__ == "__main__":
    #all_artist_songs(artist_to_scrape)  # Code à exécuter uniquement lors de l'exécution directe
    


