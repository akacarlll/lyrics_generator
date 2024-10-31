import requests
from bs4 import BeautifulSoup
import re

def rappers_list():
    # Envoyer une requête GET pour récupérer le contenu de la page
    response = requests.get("https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Rappeur_fran%C3%A7ais")
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Parser le contenu HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trouver toutes les divs avec la classe spécifiée
        categories = soup.find_all("div", class_="mw-category-group")
        
        # Liste pour stocker tous les textes récupérés
        texts = []
        
        # Itérer sur chaque groupe de catégorie pour extraire les textes
        for category in categories:
            # Récupérer le titre de la catégorie
            title = category.find("h3").text
            texts.append(title)  # Ajouter le titre à la liste

            # Récupérer tous les éléments <li> dans la catégorie
            items = category.find_all("li")
            for item in items:
                link = item.find("a")
                if link:
                    texts.append(link.text)  # Ajouter le texte du lien à la liste
        for i in texts:
            if len(i) <=2 :
                texts.remove(i)
        return texts
    else:
        print(f"Erreur lors de la récupération de la page : {response.status_code}")
        return []

def clean_texts():
    texts = rappers_list()
    cleaned_texts = []
    for text in texts:
        # Supprimer les espaces à la fin
        text = text.rstrip()
        # Supprimer les mots "artistes" et "rappeur"
        text = re.sub(r'\s*\(?artistes\)?\s*|\s*\(?rappeur\)?\s*', '', text, flags=re.IGNORECASE)
        # Ajouter le texte nettoyé à la liste
        cleaned_texts.append(text.strip())  # Également supprimer les espaces restants
    return cleaned_texts