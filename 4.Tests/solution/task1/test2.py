import unittest

from task2 import discriminant, solution


class TestQuadraticEquation(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(discriminant(1, 8, 15), 4)
        self.assertEqual(discriminant(1, -13, 12), 121)
        self.assertEqual(discriminant(-4, 28, -49), 0)
        self.assertEqual(discriminant(1, 1, 1), -3)


def test_solution(self):
    import sys
    from io import StringIO

    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)

    output = captured_output.getvalue().strip().split("\n")

    self.assertEqual(output, ["корней нет", "-3.0", "12.0 1.0", "3.5"])


if __name__ == "__main__":
    unittest.main()
