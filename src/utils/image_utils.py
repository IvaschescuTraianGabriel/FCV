import numpy as np

def ensure_uint8(image: np.ndarray) -> np.ndarray:
    """
    Ensure image is uint8.
    """
    if image.dtype != np.uint8:
        image = np.clip(image, 0, 255).astype(np.uint8)
    return image
