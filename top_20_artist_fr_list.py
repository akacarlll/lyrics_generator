
import pandas as pd 
import numpy as np
import random 
from bs4 import BeautifulSoup
import requests 

url ="https://www.officialcharts.com/charts/french-singles-chart/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers = headers)
page_content = response.content

soup = BeautifulSoup(page_content, 'html.parser')

top_20 =[]

chart_items = soup.find_all('div', class_='chart-item-content')

for item in chart_items:
    try:
        # Extraire la position de la chanson
        #position = item.find('span', class_='digits1 chart-key font-bold').strong.text
        
        # Extraire le titre de la chanson
        song_title = item.find('a', class_='chart-name').span.text
        
        # Extraire le nom de l'artiste
        artist = item.find('a', class_='chart-artist').span.text

        # Extraire le lien vers l'image de couverture (la petite version ici)
        #cover_img = item.find('img', class_='chart-image-small')['src']
        
        # Extraire le lien de l'aperçu audio
        #audio_preview = item.find('audio')['src']
        top_20.append({          
            'Artiste': artist,
            "Titre" : song_title
            })
    except (NoneType, KeyboardInterrupt) as e :
        None

else:
    print(f"Erreur lors de la récupération de la page, code statut : {req.status_code}")

df = pd.DataFrame(top_20)
df

artist_to_scrape = df["Artiste"]

