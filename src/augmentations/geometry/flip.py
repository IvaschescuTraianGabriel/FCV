import numpy as np
import cv2
from ..base import Augmentation, register_augmentation

@register_augmentation("flip_horizontal_manual")
class ManualHorizontalFlip(Augmentation):
    """
    Low-level horizontal flip implemented with direct pixel access.
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        h, w, c = image.shape
        result = np.empty_like(image)
        for y in range(h):
            for x in range(w):
                result[y, w - 1 - x] = image[y, x]
        return result


@register_augmentation("flip")
class FlipOpenCV(Augmentation):
    """
    Flip using OpenCV.
    Params:
        direction: "horizontal" | "vertical"
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        direction = self.params.get("direction", "horizontal")
        if direction == "horizontal":
            code = 1
        elif direction == "vertical":
            code = 0
        else:
            raise ValueError(f"Unknown flip direction: {direction}")
        return cv2.flip(image, code)
