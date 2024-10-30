# src/<your_project>/nodes/concatenation.py

import pandas as pd

def concatenate(dfs: list) -> pd.DataFrame:
    """
    Concatène une liste de DataFrames en un seul DataFrame.

    Paramètres :
    - dfs : Liste de DataFrames à concaténer.

    Retourne :
    - DataFrame concaténé.
    """
    # Vérifier que la liste n'est pas vide
    if not dfs:
        raise ValueError("La liste des DataFrames ne doit pas être vide.")
    
    # Concaténer les DataFrames
    concatenated_df = pd.concat(dfs, ignore_index=True)
    return concatenated_df
