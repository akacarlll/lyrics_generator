from .nodes import create_wordcloud
from kedro.pipeline import Pipeline, node
from lyrics_generator.pipelines.data_analysis.list import get_file_names


folder_path = r"C:\Users\carlf\Documents\GitHub\lyrics_generator\data\03_advanced"

def create_pipeline3(folder_path, **kwargs):
    pipeline_nodes = []
    
    file_name = get_file_names(folder_path)
    for dataset_name in file_name: 
        pipeline_nodes.extend([
            node(
                func=create_wordcloud,
                inputs=f"_{dataset_name}#xlsx",
                outputs=f"wordcloud_{dataset_name}",
                name=f"{dataset_name}_wordcloud"
            ),
    ])

    return Pipeline(pipeline_nodes)