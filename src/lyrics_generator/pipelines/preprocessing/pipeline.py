from .nodes import clean_lyrics_column, is_french, concatenate, remove_fake_lyrics, tokenize
from kedro.pipeline import Pipeline, node
from lyrics_generator.pipelines.preprocessing.list import get_file_names

folder_path = r"C:\Users\carlf\Documents\GitHub\lyrics_generator\data\01_raw"

def create_pipeline(folder_path, **kwargs):
    pipeline_nodes = []
    file_name = get_file_names(folder_path)
    french_datasets = []
    for dataset_name in file_name :
        pipeline_nodes.extend([
            node(
                func=clean_lyrics_column,
                inputs=f"{dataset_name}#csv",
                outputs=f"{dataset_name}",
                name=f"cleaning_{dataset_name}"
            ), 
            node(
                func=remove_fake_lyrics,
                inputs=f"{dataset_name}",
                outputs=f"cleaned_{dataset_name}",
                name=f"removing_{dataset_name}_rows"
            ), 
        ]
        )
    #     # Ajoute le nœud de vérification de langue
    #     french_output = f"french_{dataset_name}"
    #     pipeline_nodes.append(
    #         node(
    #             func=is_french,
    #             inputs=f"cleaned_{dataset_name}",
    #             outputs=french_output,
    #             name= f"french_{dataset_name}"
    #         )
    #     )
    #     french_datasets.append(french_output)

    # # Ajoute le nœud de concaténation pour tous les jeux de données en français
    # pipeline_nodes.append(
    #     node(
    #         func=concatenate,
    #         inputs=french_datasets,  # Utilisation de tous les noms de datasets en entrée
    #         outputs="all_lyrics",
    #         name="concatenate_all_lyrics"
    #     )
    # )
    return Pipeline(pipeline_nodes)