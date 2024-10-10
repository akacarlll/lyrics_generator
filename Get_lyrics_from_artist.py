from lyricsgenius import Genius
import lyricsgenius as lg
import requests
import requests
import pandas as pd 
import numpy as np
import random 
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm 
import os


token = 'vEuhOt5S8b7JMcQuXZhlSNouoVIPQruY6a0bsie-lifgyPxsx_dPVzDSZools0pG'
GENIUS_API_TOKEN = 'vEuhOt5S8b7JMcQuXZhlSNouoVIPQruY6a0bsie-lifgyPxsx_dPVzDSZools0pG'
genius = lg.Genius(token)



def get_artist_id(artist_name):
    """Récupère l'ID d'un artiste en utilisant l'API Genius."""
    search_url = f"https://api.genius.com/search?q={artist_name}"
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    
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

def get_songs(artist_id):
    """Récupère les titres des chansons d'un artiste donné."""
    timeout_duration = 20
    songs = []
    page = 1
    max_songs = 100
    while True:
        url = f"https://api.genius.com/artists/{artist_id}/songs?page={page}"
        headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
        response = requests.get(url, headers=headers).json()
        songs_data = response['response']['songs']
        try:
            response = requests.get(url, headers=headers, timeout=timeout_duration).json()
            songs_data = response['response']['songs']
        except requests.exceptions.Timeout:
            print(f"Requête timeout pour la page {page}, tentative de nouvelle requête...")
            continue  # Réessayer la requête pour cette page
        except requests.exceptions.RequestException as e:
            print(f"Erreur de connexion : {e}")
            break  # Quitter la boucle en cas d'erreur de connexion
        if not songs_data:
            break
        
        for song in songs_data:
            if len(songs) >= max_songs:
                return songs
            songs.append(song['title'])
        
        page += 1
    return songs

def download_lyrics(song_title, artist_name):
    """Télécharge les paroles d'une chanson donnée."""

    song = genius.search_song(song_title, artist_name)
    if song : 
        try :
            paroles = song.lyrics
        except Exception as e :
            return None
    
        return paroles
    return None

def all_artist_songs(artist_to_scrape):
    """Télécharge les paroles de toutes les chansons pour chaque artiste et les stocke dans un fichier par artiste."""
    for artist in artist_to_scrape:
        artist_id = get_artist_id(artist)
        if artist_id is not None:
            songs = get_songs(artist_id)
            if songs:
                # Créer un répertoire pour l'artiste si il n'existe pas
                os.makedirs(artist, exist_ok=True)
                artist_lyrics = []  # Liste pour stocker les paroles de toutes les chansons

                for song in songs:
                    lyrics = download_lyrics(song, artist)
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
#   # Remplacez par votre liste d'artistes
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
 'SABRINA CARPENTER']
# Appeler la fonction pour télécharger les paroles
#for artist in artist_to_scrape:
    #artist_id = get_artist_id(artist)
    #print(f"ID pour {artist}: {artist_id}")
    
    
all_artist_songs(artist_to_scrape)
