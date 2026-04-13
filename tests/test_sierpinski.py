"""Unit tests for find_midpoint and sierpinski (draw_triangle mocked)."""

import os
import unittest

# Headless pygame before importing the module under test
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame

import sierpinski


def _triangle_draws_for_degree(degree: int) -> int:
    """Closed form: T(0)=1; T(k)=1+3*T(k-1) => T(d)=(3**(d+1)-1)/2."""
    return (3 ** (degree + 1) - 1) // 2


class TestFindMidpoint(unittest.TestCase):
    def test_axis_aligned(self):
        self.assertEqual(sierpinski.find_midpoint([0, 0], [10, 20]), [5.0, 10.0])

    def test_returns_list_of_floats(self):
        m = sierpinski.find_midpoint([-1.0, 2.0], [3.0, 6.0])
        self.assertIsInstance(m, list)
        self.assertEqual(len(m), 2)
        self.assertEqual(m, [1.0, 4.0])


class TestSierpinskiRecursion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.Surface((640, 640))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def _count_draws(self, degree, p1, p2, p3):
        calls = []
        orig = sierpinski.draw_triangle

        def capture(*args, **kwargs):
            calls.append(1)

        sierpinski.draw_triangle = capture
        try:
            sierpinski.sierpinski(degree, p1, p2, p3, sierpinski.BLACK, 1, self.screen)
        finally:
            sierpinski.draw_triangle = orig
        return len(calls)

    def test_degree_0_single_draw(self):
        n = self._count_draws(0, [0.0, 0.0], [100.0, 0.0], [50.0, 80.0])
        self.assertEqual(n, 1)

    def test_degree_matches_expected_counts(self):
        p1, p2, p3 = [0.0, 0.0], [100.0, 0.0], [50.0, 80.0]
        for d in range(0, 5):
            with self.subTest(degree=d):
                self.assertEqual(
                    self._count_draws(d, p1, p2, p3),
                    _triangle_draws_for_degree(d),
                )


if __name__ == "__main__":
    unittest.main()
