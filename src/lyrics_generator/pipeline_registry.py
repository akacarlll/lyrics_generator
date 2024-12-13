"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from typing import Dict
from kedro.pipeline import Pipeline
from  lyrics_generator.pipelines.preprocessing.pipeline import create_pipeline
from  lyrics_generator.pipelines.add_features.pipeline import create_pipeline2
from  lyrics_generator.pipelines.data_analysis.pipeline import create_pipeline3
from  lyrics_generator.pipelines.concatenate.pipeline import create_pipeline4

  # Importer create_pipeline
# from .pipelines import data_cleaning as dc_pipeline


# def register_pipelines() -> Dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     pipelines = find_pipelines()
#     pipelines["__default__"] = sum(pipelines.values())
#     return pipelines

def register_pipelines() -> Dict[str, Pipeline]:
    """
    Register the project's pipelines by combining multiple pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # Chemins des dossiers contenant les fichiers CSV
    folder_path1 = "C:/Users/carlf/Documents/GitHub/lyrics_generator/data/01_raw"
    folder_path2 = "C:/Users/carlf/Documents/GitHub/lyrics_generator/data/02_intermediate"
    folder_path3 = "C:/Users/carlf/Documents/GitHub/lyrics_generator/data/03_advanced"

    # Créer les pipelines individuels
    pipeline1 = create_pipeline(folder_path1)
    pipeline2 = create_pipeline2(folder_path2)
    pipeline3 = create_pipeline3(folder_path3)
    pipeline4 = create_pipeline4(folder_path3)

    # Fusionner les pipelines
    combined_pipeline = pipeline1 + pipeline2 + pipeline3 + pipeline4

    # Définir les pipelines
    pipelines = {
        "my_pipeline": pipeline1,
        "second_pipeline": pipeline2,
        "third_pipeline": pipeline3,
        "fourth_pipeline": pipeline4,
        "combined_pipeline": combined_pipeline,
        "__default__": combined_pipeline
    }
    
    return pipelines
