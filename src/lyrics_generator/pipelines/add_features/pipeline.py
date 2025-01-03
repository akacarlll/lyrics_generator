from .nodes import add_lyrics_stats, add_genre_column, add_release_year_column, divide_genre
from kedro.pipeline import Pipeline, node
from lyrics_generator.pipelines.add_features.list import get_file_names

folder_path = r"C:\Users\carlf\Documents\GitHub\lyrics_generator\data\02_intermediate"


def create_pipeline2(folder_path, **kwargs):

    
    pipeline_nodes = []
    
    file_name = get_file_names(folder_path)
    
    
    for dataset_name in file_name: 
        pipeline_nodes.extend([
            node(
                func=add_genre_column,
                inputs=f"{dataset_name}#xlsx",
                outputs=f"____{dataset_name}",
                name=f"genred_{dataset_name}"
            ),
            node(
                func=add_release_year_column,
                inputs=f"____{dataset_name}",
                outputs=f"_____{dataset_name}",
                name=f"yeared_{dataset_name}"
            ),
            node(
                func=divide_genre,
                inputs=f"_____{dataset_name}",
                outputs=f"______{dataset_name}",
                name=f"separating_genre_{dataset_name}"
            ),
            node(
                func=add_lyrics_stats,
                inputs=f"______{dataset_name}",
                outputs=f"_{dataset_name}#xlsx",
                name=f"complete_{dataset_name}"
            ),
        ])


    return Pipeline(pipeline_nodes)
