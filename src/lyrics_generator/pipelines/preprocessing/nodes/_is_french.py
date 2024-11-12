
import pandas as pd
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

def is_french(dfs:pd.DataFrame, text_column="Lyrics"):
    """
    Ajoute une colonne `is_french` dans chaque DataFrame de la liste `dfs` 
    pour indiquer si le texte dans `text_column` est en français.
    
    Paramètres :
    - dfs : Liste de DataFrames à traiter.
    - text_column : Nom de la colonne contenant le texte à analyser.
    
    Retourne :
    - Liste de DataFrames avec une nouvelle colonne `is_french`.
    """
    for df in dfs:
        # Fonction auxiliaire pour détecter si le texte est en français
        def detect_french(text):
            try:
                return detect(text) == 'fr'
            except LangDetectException:
                return False  # En cas d'erreur de détection, on retourne False

        # Application de la détection de langue et ajout de la colonne `is_french`
        df['is_french'] = df[text_column].apply(detect_french)
    
    return dfs
