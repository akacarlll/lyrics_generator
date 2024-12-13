from .nodes import concatenate
from kedro.pipeline import Pipeline, node
from lyrics_generator.pipelines.add_features.list import get_file_names


folder_path = r"C:\Users\carlf\Documents\GitHub\lyrics_generator\data\03_advanced"


def create_pipeline4(folder_path, **kwargs):
    
    pipeline_nodes = []
    df_list = []
    
    
    file_name = get_file_names(folder_path)
    
    for dataset_name in file_name:
        df_list.append(f"_{dataset_name}#xlsx")
        
    pipeline_nodes.append(
        node(
            func=concatenate,
            inputs=df_list,
            outputs="lyrics_genius.xlsx",
            name="concatenate_dfs",
        )
    )

    return Pipeline(pipeline_nodes)
