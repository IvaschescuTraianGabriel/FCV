import numpy as np
from ..base import Augmentation, register_augmentation

@register_augmentation("brightness_manual")
class ManualBrightness(Augmentation):
    """
    Low-level brightness adjustment implemented with direct pixel manipulation.
    Param:
        delta: int, added to each channel [-255, 255]
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        delta = int(self.params.get("delta", 0))
        # Convert to int16 to avoid overflow, then clip back to [0, 255]
        h, w, c = image.shape
        result = np.empty_like(image)
        for y in range(h):
            for x in range(w):
                for ch in range(c):
                    val = int(image[y, x, ch]) + delta
                    if val < 0:
                        val = 0
                    elif val > 255:
                        val = 255
                    result[y, x, ch] = val
        return result
