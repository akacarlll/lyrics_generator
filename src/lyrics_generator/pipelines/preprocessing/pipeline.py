from .nodes import clean_lyrics_column, is_french, remove_fake_lyrics, tokenize_nltk,tokenize_gpt2
from kedro.pipeline import Pipeline, node
from lyrics_generator.pipelines.preprocessing.list import get_file_names

folder_path = r"C:\Users\carlf\Documents\GitHub\lyrics_generator\data\01_raw"

def create_pipeline(folder_path, **kwargs):   
    pipeline_nodes = []    
    file_name = get_file_names(folder_path)   
    
    for dataset_name in file_name :
        pipeline_nodes.extend([
            node(
                func=clean_lyrics_column,
                inputs=f"{dataset_name}#csv",
                outputs=f"_{dataset_name}",
                name=f"cleaning_{dataset_name}"
            ), 
            node(
                func=remove_fake_lyrics,
                inputs=f"_{dataset_name}",
                outputs=f"__{dataset_name}",
                name=f"removing_{dataset_name}_rows"
            ), 
            node(
                func=tokenize_nltk,
                inputs=f"__{dataset_name}",
                outputs=f"___{dataset_name}",
                # outputs=f"{dataset_name}",
                name=f"tokenizenltk_{dataset_name}"
            ), 
            node(
                func=tokenize_gpt2,
                inputs=f"___{dataset_name}",
                outputs=f"{dataset_name}#xlsx",
                # outputs=f"{dataset_name}",
                name=f"tokenizegpt2_{dataset_name}"
            ), 
                
        ])
    return Pipeline(pipeline_nodes)