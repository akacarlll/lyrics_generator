import pandas as pd

# Fonction pour diviser les genres et créer des colonnes dynamiques
def split_genres(genre_str):
    # Séparer les genres et enlever les espaces
    genres = [g.strip() for g in genre_str.split(",")]
    
    # Créer un dictionnaire de résultats
    result = {}
    for i, genre in enumerate(genres, 1):
        result[f'Genre{i}'] = genre
    
    return result

def divide_genre(df):
    if "Genre" not in df.columns:
        raise ValueError("La colonne 'Genre' n'existe pas dans le DataFrame")
    
    # Appliquer la fonction à chaque ligne
    genres_df = df["Genre"].apply(split_genres).apply(pd.Series)
    
    # Combiner le DataFrame original avec les nouvelles colonnes de genres
    return pd.concat([df.drop(columns=["Genre"]), genres_df], axis=1)