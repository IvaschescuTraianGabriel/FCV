from pathlib import Path
from typing import Dict, Tuple
import cv2
import numpy as np

def make_output_dir(input_dir: Path) -> Path:
    """
    Create output directory next to input_dir, with '_aug' suffix.
    Example: /path/images -> /path/images_aug
    """
    output_dir = input_dir.parent / f"{input_dir.name}_aug"
    output_dir.mkdir(exist_ok=True)
    return output_dir


def save_augmented_image(
    image: np.ndarray,
    output_dir: Path,
    base_name: str,
    pipeline_name: str,
    counters: Dict[Tuple[str, str], int],
    ext: str = ".jpg",
) -> None:
    """
    Save augmented image:
      <base_name>_<pipeline_name>_<N>.jpg
    """
    key = (base_name, pipeline_name)
    count = counters.get(key, 0) + 1
    counters[key] = count

    safe_pipeline_name = pipeline_name.replace(" ", "").replace("|", "+")
    filename = f"{base_name}_{safe_pipeline_name}_{count}{ext}"
    out_path = output_dir / filename
    cv2.imwrite(str(out_path), image)
