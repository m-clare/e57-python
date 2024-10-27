from typing import Any, Optional
from numpy.typing import NDArray
import numpy as np

class E57:
    """
    Class for E57 point cloud data

    Attributes:
        points: Point coordinates as Nx3 [x, y, z] array of float64 values.

        color: RGB color values as Nx3 array of float32 values, normalized to [0,1].
               Empty array if no color data present.

        intensity: Intensity values as Nx1 array of float32 values.
                   Empty array if no intensity data present.
    """
    points: NDArray[np.float64]  # Shape: (N, 3)
    color: NDArray[np.float32]   # Shape: (N, 3) or (0, 3)
    intensity: NDArray[np.float32]  # Shape: (N, 1) or (0, 1)

    def __init__(self) -> None: ...

def raw_xml(filepath: str) -> str:
    """
    Extracts the raw XML metadata from an E57 file.

    Args:
        filepath: Relative path to the E57 file.

    Returns:
        The XML content as a UTF-8 string.

    Raises:
        RuntimeError: If the file cannot be read or is invalid.
    """
    ...

def read_points(filepath: str) -> E57:
    """
    Reads point cloud data from an E57 file.

    The function automatically handles:
    - Conversion from spherical to Cartesian coordinates
    - Application of pose transformations
    - Normalization of intensity values

    Args:
        filepath: Path to the E57 file.

    Returns:
        An E57 object containing:
        - points: Nx3 array of [x, y, z] coordinates
        - color: Nx3 array of RGB values (if available)
        - intensity: Nx1 array of intensity values (if available)

    Raises:
        RuntimeError: If the file cannot be read or cannot be opened.
    """
    ...
