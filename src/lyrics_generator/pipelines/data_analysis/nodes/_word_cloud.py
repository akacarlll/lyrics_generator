from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re
from nltk.corpus import stopwords
import os
import pandas as pd

STOP_WORDS_FR = set([
    'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'au', 'aux', 'en', 'à', 'et', 'ou', 'mais', 'donc', 'or', 'ni', 'car', 
    'ce', 'cet', 'cette', 'ces', 'mon', 'ton', 'son', 'notre', 'votre', 'leur', 'ma', 'ta', 'sa', 'mes', 'tes', 'ses', 
    'nos', 'vos', 'leurs', 'je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'on', 
    'moi', 'toi', 'lui', 'elle', 'eux', 'le', 'la', 'les', 'se', 'me', 'te', 'nous', 'vous', 'leur',
    'être', 'avoir', 'faire', 'aller', 'pouvoir', 'vouloir', 'venir', 'voir', 'dire', 'prendre', 'mettre', 'savoir', 
    'y', 'en', 'par', 'avec', 'pour', 'sans', 'sous', 'dans', 'sur', 'chez', 'contre', 'de', 'du', 'des', 
    'est', 'sont', 'étaient', 'était', 'seront', 'étant', 'été', 'être', 'sera', 'au', 'aux', 'à', 'se', "c'est", 'ça', 'ceci', 'cela', 
    'qui', 'que', 'quoi', 'dont', 'où', 'lorsque', 'quand', 'comme', 'si', 'tandis', 'puisque', 'afin', 'car', 'parce', 
    'oui', 'non', "ouais", "nan", "yeah","bah","ok","is", "cur","oh" 'ne', 'pas', 'ni', "n'est", 'plus', 'toujours', 'jamais',"fait","fais", "peux", "ma","qu",
    "pe","as","ai","vais", "va","my", "là","j'ai", "j'suis", "ne","suis","sont","suis","sont","y'a","t'es","j'vais", "j'suis", "j'fais","qu'on","jai", "cest","quon", "jsuis",
    "ya", "jfais", "jvais", "yen", "jpeux", "jai", "jpeux", "jvais",
    ])

def clean_text(text : str ) -> str:
    """
    Cleans the text by removing special characters, punctuation, 
    and converting everything to lowercase.
    
    Args:
    - text (str): The input text to clean.

    Returns:
    - str: The cleaned text.
    """
    # Convertir en minuscules
    text = text.lower()

    # Supprimer les ponctuations
    text = re.sub(r"[^\w\s']", '', text)  # Garde les mots, espaces et apostrophes

    # Remplacer les espaces multiples par un seul espace
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def create_wordcloud(df:pd.DataFrame):
    """
    Crée un nuage de mots basé sur les paroles nettoyées d'un artiste dans une DataFrame.

    Paramètres :
    - df : DataFrame contenant les paroles (doit avoir une colonne 'cleaned_lyrics' et 'artist').
    - artist_name : Nom de l'artiste pour lequel créer le nuage de mots.
    - num_songs : Nombre de chansons (lignes) à utiliser. Si None, toutes les chansons de l'artiste seront utilisées.
    - save_path : Chemin où sauvegarder le nuage de mots généré.
    """
    # Filtrer la DataFrame pour l'artiste spécifié
    artist_lyrics = df["Lyrics"]

    # Combiner toutes les paroles en une seule chaîne de texte et nettoyer
    artist_lyrics = artist_lyrics.dropna().astype(str)
    combined_lyrics = ' '.join(artist_lyrics)
    cleaned_lyrics = clean_text(combined_lyrics)
    
    # Créer une liste de mots en excluant les stop words
    word_list = []
    
    for word in cleaned_lyrics.split():
        # Vérifier que le mot n'est pas dans la liste des stop words
        # et qu'il a une longueur minimum de 2 caractères
        if word.lower() not in STOP_WORDS_FR and len(word) > 1:
            word_list.append(word)
    
    # Compter les mots dans les paroles
    word_counts = Counter(word_list)
    
    # Créer le nuage de mots avec des paramètres personnalisés
    wordcloud = WordCloud(
        width=1200,
        height=800,
        background_color='white',
        max_words=150,
        min_font_size=10,
        max_font_size=150,
        random_state=42  # Pour la reproductibilité
    ).generate_from_frequencies(word_counts)
    
    image = wordcloud.to_image()
    
    return image 