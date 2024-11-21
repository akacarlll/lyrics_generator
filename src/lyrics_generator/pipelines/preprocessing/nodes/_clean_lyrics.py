import re 
import pandas as pd


def clean_lyrics(lyrics):
    """Nettoie les paroles en deux étapes."""
    # Étape 1: Supprimer tout avant la première occurrence de "Lyrics"
    lyrics = re.sub(r'^.*?Lyrics\s*', '', lyrics, flags=re.DOTALL).strip()
    # Étape 2: Supprimer le mot "Lyrics"
    lyrics = re.sub(r'\bLyrics\b', '', lyrics).strip()
    
    # Supprimer le mot "Embed" à la fin
    lyrics = re.sub(r'\s*Embed$', '', lyrics).strip()
    
    # Supprimer les annotations entre crochets
    lyrics = re.sub(r'\[.*?\]', '', lyrics)
    
    # Supprimer les caractères spéciaux, mais garder les lettres et les espaces
    lyrics = re.sub(r'[^a-zA-ZÀ-ÿ0-9\s,.!?\'-]', '', lyrics)
    
    # Supprimer les espaces supplémentaires
    lyrics = re.sub(r'\s+', ' ', lyrics).strip()
    
    lyrics = lyrics.replace('You might also like', '')
    
    # Retirer les espaces multiples
    lyrics = ' '.join(lyrics.split())
    
    return lyrics

def clean_lyrics_column(df:pd.DataFrame)-> pd.DataFrame:
    """Nettoie les paroles dans la colonne 'lyrics' de chaque ligne du DataFrame."""
    df['Lyrics'] = df['Lyrics'].apply(clean_lyrics)
    return df
