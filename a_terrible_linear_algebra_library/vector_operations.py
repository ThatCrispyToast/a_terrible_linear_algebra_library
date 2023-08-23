from typing import List
from math import sqrt

# TODO: comments?


def add(vector_a: List[float], vector_b: List[float]) -> List[float] | None:
    """Add two vectors. Return None if vectors are of different sizes."""
    return (
        [vector_a[i] + vector_b[i] for i in range(len(vector_a))]
        if len(vector_a) == len(vector_b)
        else None
    )


def subtract(vector_a: List[float], vector_b: List[float]) -> List[float] | None:
    """Subtract two vectors. Return None if vectors are of different sizes."""
    return (
        [vector_a[i] - vector_b[i] for i in range(len(vector_a))]
        if len(vector_a) == len(vector_b)
        else None
    )


def multiply_scalor_by_vector(scalar: float, vector: List[float]) -> List[float]:
    """Multiply a scalar by a vector."""
    return [scalar * i for i in vector]


def calculate_dot_product(vector_a: List[float], vector_b: List[float]) -> float | None:
    """Calculate the dot product of two vectors. Return None if vectors are of different sizes."""
    return (
        sum([vector_a[i] * vector_b[i] for i in range(len(vector_a))])
        if len(vector_a) == len(vector_b)
        else None
    )


def calculate_cross_product(
    vector3d_a: List[float], vector3d_b: List[float]
) -> List[float] | None:
    """Calculate the dot product of two vectors. Return None if vectors are not three dimensional."""
    if len(vector3d_a) != 3 or len(vector3d_b) != 3:
        return None
    return [
        vector3d_a[1] * vector3d_b[2] - vector3d_a[2] * vector3d_b[1],
        vector3d_a[2] * vector3d_b[0] - vector3d_a[0] * vector3d_b[2],
        vector3d_a[0] * vector3d_b[1] - vector3d_a[1] * vector3d_b[0],
    ]


def calculate_vector_magnitude(vector: list) -> float:
    "Calculate the magnitude of a vector."
    return sqrt(sum([i**2 for i in vector]))
