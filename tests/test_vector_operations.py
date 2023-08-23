import numpy
import unittest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import a_terrible_linear_algebra_library as atlab
from test_utils import gen_extreme_rand, gen_extreme_vector


# TODO: make the tests repeat with different numbers and vectors
# TODO: vector_operations tests
# TODO: comments
class TestVectorOperations(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        vector_length = int(gen_extreme_rand())
        vector1 = gen_extreme_vector(vector_length)
        vector2 = gen_extreme_vector(vector_length)
        self.assertEqual(
            atlab.vector_operations.add(vector1, vector2),
            numpy.add(vector1, vector2).tolist(),
        )


if __name__ == "__main__":
    unittest.main()
