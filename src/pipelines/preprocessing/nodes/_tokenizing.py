# src/<your_project>/nodes/tokenization.py

import nltk
from nltk.tokenize import word_tokenize
import pandas as pd

# Assurez-vous de télécharger les ressources nécessaires si c'est la première fois que vous utilisez nltk
nltk.download('punkt')

def tokenize(df: pd.DataFrame, text_column: str) -> pd.DataFrame:
    """
    Tokenise les mots d'une colonne de texte dans une DataFrame.

    Paramètres :
    - df : DataFrame contenant la colonne à tokeniser.
    - text_column : Nom de la colonne à tokeniser.

    Retourne :
    - DataFrame avec une nouvelle colonne contenant les tokens.
    """
    df['tokens'] = df[text_column].apply(word_tokenize)
    return df
