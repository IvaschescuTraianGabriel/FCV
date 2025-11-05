from abc import ABC, abstractmethod
from typing import Dict, Type, Any
import numpy as np

class Augmentation(ABC):
    """
    Base class for all augmentations.
    """

    def __init__(self, **params: Any):
        self.params = params

    @abstractmethod
    def apply(self, image: np.ndarray) -> np.ndarray:
        """Apply augmentation to image and return the augmented image."""
        pass


# Registry for augmentation classes
AUGMENTATION_REGISTRY: Dict[str, Type[Augmentation]] = {}


def register_augmentation(name: str):
    """
    Decorator to register an augmentation under a given name.
    """
    def decorator(cls: Type[Augmentation]):
        AUGMENTATION_REGISTRY[name] = cls
        return cls
    return decorator


def create_augmentation(name: str, **params: Any) -> Augmentation:
    """
    Factory: create an augmentation instance by name.
    """
    cls = AUGMENTATION_REGISTRY.get(name)
    if cls is None:
        raise ValueError(f"Unknown augmentation: {name}")
    return cls(**params)
