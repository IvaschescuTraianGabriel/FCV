from pathlib import Path
from typing import List, Dict, Tuple
import cv2
import numpy as np

from augmentations.base import Augmentation
from .config_loader import PipelineConfig
from utils.io_utils import make_output_dir, save_augmented_image

def process_directory(
    input_dir: Path,
    pipeline_configs: List[PipelineConfig],
    pipelines: List[List[Augmentation]],
) -> None:
    """
    For each .jpg image in input_dir, applies each pipeline and saves results
    in <input_dir>_aug.
    """
    output_dir = make_output_dir(input_dir)
    counters: Dict[Tuple[str, str], int] = {}

    # Precompute pipeline names based on config
    from .pipeline import pipeline_name_from_config
    pipeline_names = [
        pipeline_name_from_config(cfg) for cfg in pipeline_configs
    ]

    image_paths = sorted(input_dir.glob("*.jpg"))

    if not image_paths:
        print(f"No .jpg images found in {input_dir}")
        return

    for img_path in image_paths:
        print(f"Processing {img_path.name}...")
        image = cv2.imread(str(img_path))
        if image is None:
            print(f"  Warning: could not read {img_path}")
            continue

        base_name = img_path.stem

        for pipeline_conf, pipeline, pname in zip(pipeline_configs, pipelines, pipeline_names):
            augmented: np.ndarray = image.copy()
            for aug in pipeline:
                augmented = aug.apply(augmented)
            save_augmented_image(
                augmented,
                output_dir,
                base_name,
                pname,
                counters,
                ext=img_path.suffix,  # keep extension (.jpg)
            )

    print(f"Done. Output saved in: {output_dir}")
