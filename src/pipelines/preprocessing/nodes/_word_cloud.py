from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re
from nltk.corpus import stopwords
import os


STOP_WORDS_FR = set([
    'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'au', 'aux', 'en', 'à', 'et', 'ou', 'mais', 'donc', 'or', 'ni', 'car', 
    'ce', 'cet', 'cette', 'ces', 'mon', 'ton', 'son', 'notre', 'votre', 'leur', 'ma', 'ta', 'sa', 'mes', 'tes', 'ses', 
    'nos', 'vos', 'leurs', 'je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'on', 
    'moi', 'toi', 'lui', 'elle', 'eux', 'le', 'la', 'les', 'se', 'me', 'te', 'nous', 'vous', 'leur',
    'être', 'avoir', 'faire', 'aller', 'pouvoir', 'vouloir', 'venir', 'voir', 'dire', 'prendre', 'mettre', 'savoir', 
    'y', 'en', 'par', 'avec', 'pour', 'sans', 'sous', 'dans', 'sur', 'chez', 'contre', 'de', 'du', 'des', 
    'est', 'sont', 'étaient', 'était', 'seront', 'étant', 'été', 'être', 'sera', 'au', 'aux', 'à', 'se', 'c’est', 'ça', 'ceci', 'cela', 
    'qui', 'que', 'quoi', 'dont', 'où', 'lorsque', 'quand', 'comme', 'si', 'tandis', 'puisque', 'afin', 'car', 'parce', 
    'oui', 'non', 'ne', 'pas', 'ni', 'n’est', 'plus', 'toujours', 'jamais'
])

def create_wordcloud(df, artist_name: str, num_songs=None, save_path="output_folder/"):
    """
    Crée un nuage de mots basé sur les paroles nettoyées d'un artiste dans une DataFrame.

    Paramètres :
    - df : DataFrame contenant les paroles (doit avoir une colonne 'cleaned_lyrics' et 'artist').
    - artist_name : Nom de l'artiste pour lequel créer le nuage de mots.
    - num_songs : Nombre de chansons (lignes) à utiliser. Si None, toutes les chansons de l'artiste seront utilisées.
    """
    
    # Filtrer la DataFrame pour l'artiste spécifié
    artist_lyrics = df[df['Artist'].str.lower() == artist_name.lower()]['Cleaned_Lyrics']
    
    # Limiter à 'num_songs' chansons si spécifié
    if num_songs:
        artist_lyrics = artist_lyrics.head(num_songs)
    
    # Combiner toutes les paroles en une seule chaîne de texte
    combined_lyrics = ' '.join(artist_lyrics)
    
    # Enlever les stop words de la liste de mots
    word_list = [word for word in combined_lyrics.split() if word not in STOP_WORDS_FR]
    
    # Compter les mots dans les paroles
    word_counts = Counter(word_list)
    
    # Générer le nuage de mots
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    
    filename = f"wordcloud_{artist_name.replace(' ', '_').lower()}.png"
    full_path = os.path.join(save_path, filename)
    
    # Enregistrer le nuage de mots dans le dossier spécifié
    os.makedirs(save_path, exist_ok=True)  # Crée le dossier si inexistant
    wordcloud.to_file(full_path)