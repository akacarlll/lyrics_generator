import spacy
import pandas as pd

# Charger le modèle linguistique français
# Note : Il faudra l'installer séparément avec : 
# python -m spacy download fr_core_news_sm
nlp = spacy.load('fr_core_news_sm')

def custom_tokenize(text: str) -> list:
        """
        Tokenise un texte en utilisant spaCy.
        
        - Traite le texte avec le modèle linguistique
        - Extrait les tokens (lemmatisés ou non selon les besoins)
        """
        # Traiter le texte avec le modèle linguistique
        doc = nlp(text)
        
        # Extraire les tokens (lemmatisés)
        # Vous pouvez choisir entre token.text (mot original) ou token.lemma_ (lemme)
        tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]
        
        return tokens

def tokenize_spacy(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tokenise les mots d'une colonne de texte dans une DataFrame en utilisant spaCy.

    Paramètres :
    - df : DataFrame contenant la colonne à tokeniser.

    Retourne :
    - DataFrame avec une nouvelle colonne contenant les tokens.
    """

    # Vérifier si la colonne 'Lyrics' existe
    if "Lyrics" not in df.columns:
        raise ValueError("La colonne 'Lyrics' est manquante dans la DataFrame.")
    
    # Appliquer la tokenisation personnalisée
    df['spacy_tokens'] = df["Lyrics"].apply(custom_tokenize)
    
    return df