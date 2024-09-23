from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import spotipy
from lyricsgenius import Genius
import lyricsgenius as lg
import json

genius = lg.Genius(token)

# Rechercher une chanson et obtenir les paroles
song_title = "NO HOOK"  # Remplacer par le titre de la chanson
artist_name = "La Fève"  # Remplacer par le nom de l'artiste

# Récupérer la chanson
song = genius.search_song(song_title, artist_name)

# Afficher les paroles
if song:
    print(song.lyrics)
else:
    print("Paroles non trouvées.")



from lyricsgenius import Genius
import os

# Ton token Genius
token = "votre_token_genius"

# Créer un objet Genius avec un délai d'attente
genius = Genius(token, timeout=10)

# Rechercher l'album
album = genius.search_album("J.E. Heartbreak", "Jagged Edge")

# Spécifier le chemin de sauvegarde
save_path = r"C:\Users\carlf\OneDrive\Bureau\Advanced Programming\Projet\Artiste"

# Créer le dossier s'il n'existe pas
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Sauvegarder les paroles manuellement
lyrics_file = os.path.join(save_path, f"{album.name}_lyrics.txt")

with open(lyrics_file, 'w', encoding='utf-8') as f:
    for track in album.tracks:
        song = track.song
        f.write(f"{song.title}\n\n{song.lyrics}\n\n{'-'*40}\n\n")

print(f"Paroles de l'album '{album.name}' sauvegardées dans '{lyrics_file}'.")