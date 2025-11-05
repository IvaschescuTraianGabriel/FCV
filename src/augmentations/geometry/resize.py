import numpy as np
import cv2
from ..base import Augmentation, register_augmentation

@register_augmentation("resize")
class ResizeAugmentation(Augmentation):
    """
    Resize using OpenCV.
    Params:
        scale: float, scale factor for both width and height
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        scale = float(self.params.get("scale", 1.0))
        h, w = image.shape[:2]
        new_w = max(1, int(w * scale))
        new_h = max(1, int(h * scale))
        return cv2.resize(image, (new_w, new_h))
