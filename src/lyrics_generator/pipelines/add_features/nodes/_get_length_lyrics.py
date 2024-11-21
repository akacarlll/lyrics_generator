import pandas as pd

def add_lyrics_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajoute deux colonnes à la DataFrame :
    - 'CharCount' : Nombre de caractères pour chaque chanson.
    - 'WordCount' : Nombre de mots pour chaque chanson.

    Paramètres :
    - df : DataFrame contenant une colonne avec les paroles des chansons.
    - 'Lyrics' : Nom de la colonne contenant les paroles des chansons.

    Retourne :
    - La DataFrame enrichie avec les colonnes 'CharCount' et 'WordCount'.
    """
    # Vérification que la colonne existe
    if "Lyrics" not in df.columns:
        raise ValueError("La colonne 'Lyrics' n'existe pas dans la DataFrame.")
    
    # Calcul du nombre de caractères et de mots
    df['CharCount'] = df['Lyrics'].apply(lambda x: len(x) if pd.notnull(x) else 0)
    df['WordCount'] = df['Lyrics'].apply(lambda x: len(x.split()) if pd.notnull(x) else 0)
    
    return df