from .nodes import clean_lyrics, create_wordcloud, get_genre, get_release_year
from kedro.pipeline import Pipeline, node


def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=clean_df,
            inputs="raw_data",  # Remplace "raw_data" par le dataset approprié
            outputs="cleaned_data",  # Le nom du dataset de sortie
            name="clean_df_node"
        )
    ])