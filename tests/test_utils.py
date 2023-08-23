import random
from typing import List

# TODO: docstrings


def gen_extreme_rand() -> float:
    """Generate a random float between -1000000000 and 1000000000."""
    return random.uniform(-1000000000, 1000000000)


def gen_extreme_vector(length: int) -> List[float]:
    """Generate a random vector with float components between -1000000000 and 1000000000."""
    return [random.uniform(-1000000000, 1000000000)] * length
