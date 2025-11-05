from typing import List
from augmentations.base import create_augmentation, Augmentation
from .config_loader import PipelineConfig

def build_pipelines(configs: List[PipelineConfig]) -> List[List[Augmentation]]:
    """
    From list of PipelineConfig (operation configs), build actual augmentation objects.
    """
    pipelines: List[List[Augmentation]] = []
    for pipeline_conf in configs:
        pipeline: List[Augmentation] = []
        for op_conf in pipeline_conf:
            aug = create_augmentation(op_conf.name, **op_conf.params)
            pipeline.append(aug)
        pipelines.append(pipeline)
    return pipelines


def pipeline_name_from_config(pipeline_conf: PipelineConfig) -> str:
    """
    Build a descriptive name from operations in the pipeline.
    Example: ["contrast", "resize"] -> "contrast+resize"
    """
    return "+".join(op.name for op in pipeline_conf)
