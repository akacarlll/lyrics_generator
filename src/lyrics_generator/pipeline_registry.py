"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from typing import Dict
from kedro.pipeline import Pipeline
from  lyrics_generator.pipelines.preprocessing.pipeline import create_pipeline
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
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # Chemin du dossier contenant vos fichiers CSV
    folder_path = "C:/Users/carlf/Documents/GitHub/lyrics_generator/data/01_raw"

    # Crée le pipeline
    pipelines = {
        "my_pipeline": create_pipeline(folder_path)
    }

    # Définit le pipeline par défaut comme étant `my_pipeline`
    pipelines["__default__"] = pipelines["my_pipeline"]
    
    return pipelines
