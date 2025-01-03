import nltk
from nltk.tokenize import word_tokenize
import pandas as pd

# Assurez-vous de télécharger les ressources nécessaires si c'est la première fois que vous utilisez nltk

def tokenize_nltk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tokenise les mots d'une colonne de texte dans une DataFrame.

    Paramètres :
    - df : DataFrame contenant la colonne à tokeniser.
    - text_column : Nom de la colonne à tokeniser.

    Retourne :
    - DataFrame avec une nouvelle colonne contenant les tokens.
    """
    df = df.dropna()
    
    if "Lyrics" not in df.columns:
        raise ValueError("La colonne 'Lyrics' est manquante dans la DataFrame.")
    
    df['nltk_tokens'] = df["Lyrics"].apply(word_tokenize)
    return df
