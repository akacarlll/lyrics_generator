import pandas as pd
from transformers import GPT2Tokenizer

def tokenize_gpt2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tokenise les paroles dans une DataFrame et ajoute une nouvelle colonne avec les tokens.

    Paramètre:
    - df (DataFrame) : La DataFrame contenant la colonne 'Lyrics' à tokeniser.

    Retourne:
    - DataFrame avec une nouvelle colonne 'tokens' contenant les textes tokenisés.
    """
    df = df.dropna()
    # Vérifier si la colonne 'Lyrics' existe dans la DataFrame
    if 'Lyrics' not in df.columns:
        raise ValueError("La DataFrame doit contenir une colonne 'Lyrics'.")

    # Charger le tokenizer GPT2
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    
    # Définir le token de padding comme étant le token de fin de phrase (eos_token)
    tokenizer.pad_token = tokenizer.eos_token

    # Tokeniser les paroles et ajouter la nouvelle colonne 'tokens'
    df['tokens_gpt2'] = df['Lyrics'].apply(lambda x: tokenizer(x, return_tensors="pt", truncation=True, padding=True))

    return df