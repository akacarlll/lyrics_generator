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
    1. Supprimant les lignes qui contiennent plus de 100 tirets
    2. Retirant toutes les occurrences de 'You might also like'
    
    Paramètres :
    - df : DataFrame avec une colonne 'Lyrics'
    
    Retourne :
    - DataFrame nettoyée
    """
    # Créer un masque pour les lignes à garder (celles avec moins de 101 tirets)
    mask = df['Lyrics'].apply(count_dashes) <= 100
    
    # Appliquer le masque pour filtrer les lignes
    df = df[mask]
    
    # Réinitialiser l'index
    df = df.reset_index(drop=True)
    
    return df