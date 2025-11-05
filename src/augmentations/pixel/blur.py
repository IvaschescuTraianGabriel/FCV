import numpy as np
import cv2
from ..base import Augmentation, register_augmentation

@register_augmentation("blur")
class BlurAugmentation(Augmentation):
    """
    Gaussian blur.
    Params:
        ksize: odd int, kernel size (e.g., 3, 5, 7)
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        ksize = int(self.params.get("ksize", 3))
        if ksize % 2 == 0:
            ksize += 1  # ensure odd
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
