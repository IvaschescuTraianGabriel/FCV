import numpy as np
import cv2
from ..base import Augmentation, register_augmentation

@register_augmentation("contrast")
class ContrastAdjustment(Augmentation):
    """
    Contrast + brightness using OpenCV:
        new = alpha * image + beta
    Params:
        alpha: float (contrast)
        beta: float (brightness shift)
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        alpha = float(self.params.get("alpha", 1.0))
        beta = float(self.params.get("beta", 0.0))
        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
