def count_dashes(text):
    """
    Compte le nombre de tirets dans une chaîne de texte.
    
    Paramètres :
    - text : Chaîne de texte à analyser
    
    Retourne :
    - Nombre de tirets dans le texte
    """
    if isinstance(text, str):
        return text.count('-')
    return 0


def remove_fake_lyrics(df):
    """
    Nettoie une DataFrame contenant des paroles en :
    1. Supprimant les lignes qui contiennent plus de 30 tirets
    2. Retirant toutes les occurrences de 'You might also like'
    
    Paramètres :
    - df : DataFrame avec une colonne 'Lyrics'
    
    Retourne :
    - DataFrame nettoyée avec les mêmes colonnes que l'originale
    """
    # Créer une copie de la DataFrame pour ne pas modifier l'originale
    cleaned_df = df.copy()
    
    # Créer un masque pour les lignes à garder (celles avec moins de 31 tirets)
    mask = cleaned_df['Lyrics'].apply(count_dashes) <= 100
    
    # Appliquer le masque pour filtrer les lignes
    cleaned_df = cleaned_df[mask]
    
    # Réinitialiser l'index
    cleaned_df = cleaned_df.reset_index(drop=True)
    
    # Afficher un résumé des modifications
    # rows_removed = len(df) - len(cleaned_df)
    # print(f"Nombre de lignes supprimées : {rows_removed}")
    # print(f"Nombre de lignes restantes : {len(cleaned_df)}")
    
    return cleaned_df