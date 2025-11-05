import numpy as np
import cv2
from ..base import Augmentation, register_augmentation

@register_augmentation("rotate")
class RotateAugmentation(Augmentation):
    """
    Rotation using OpenCV warpAffine.
    Params:
        angle: float, in degrees (positive = counter-clockwise)
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        angle = float(self.params.get("angle", 0.0))
        h, w = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(image, M, (w, h))
