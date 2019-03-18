import unittest

from vector import Vector


class TestVector(unittest.TestCase):

    def test_repr(self):
        v = Vector([1, 2, 3])

        self.assertEqual(str(v), "Vector([1, 2, 3])")
        self.assertEqual(repr(v), str(v))

        v = Vector([1.0, 2, 3.0])

        self.assertEqual(str(v), "Vector([1.0, 2, 3.0])")
        self.assertEqual(repr(v), str(v))

        v = Vector([-1, 2, 3.5, 10])

        self.assertEqual(str(v), "Vector([-1, 2, 3.5, 10])")
        self.assertEqual(repr(v), str(v))

    def test_add(self):
        v = Vector([1, 2])
        other_v = Vector([3, 4])

        self.assertEqual(v + other_v, Vector([4, 6]))

        v = Vector([1.0, 2.5, 3])
        other_v = Vector([2.3, -1.0, 2.3])

        self.assertEqual(v + other_v, Vector([3.3, 1.5, 5.3]))

        v = Vector([1, 2, 3])
        other_v = Vector([1, 1])
        with self.assertRaises(ValueError):
            print(v + other_v)

    def test_sub(self):
        v = Vector([1, 2])
        other_v = Vector([3, 4])

        self.assertEqual(v - other_v, Vector([-2, -2]))

        v = Vector([1.0, 2.5, 3])
        other_v = Vector([2.0, -1.0, 2])

        self.assertEqual(v - other_v, Vector([-1, 3.5, 1]))

        v = Vector([1, 2, 3])
        other_v = Vector([1, 1])
        with self.assertRaises(ValueError):
            print(v - other_v)

    def test_mul(self):
        v = Vector([1, 2])
        other_v = Vector([3, 4])

        self.assertEqual(v*other_v, Vector([3, 8]))

        v = Vector([1.0, 2.5, 3])
        other_v = Vector([2.0, -1.0, 2])

        self.assertEqual(v * other_v, Vector([2, -2.5, 6]))

        v = Vector([1, 2, 3])
        other_v = Vector([1, 1])
        with self.assertRaises(ValueError):
            print(v * other_v)

    def test_div(self):
        v = Vector([3, 2])
        other_v = Vector([1, 4])

        self.assertEqual(v / other_v, Vector([3, 0.5]))

        v = Vector([1.0, 2.5, 3])
        other_v = Vector([2.0, -1.0, 2])

        self.assertEqual(v / other_v, Vector([0.5, -2.5, 1.5]))

        v = Vector([1, 2, 3])
        other_v = Vector([1, 1])
        with self.assertRaises(ValueError):
            print(v / other_v)

    def test_eq(self):
        v = Vector([3, 2])
        other_v = Vector([3, 2])

        self.assertTrue(v == other_v)

        v = Vector([3.5, 2])
        other_v = Vector([3, 2])

        self.assertFalse(v == other_v)

        v = Vector([3, 2, 3])
        other_v = Vector([3, 2])

        self.assertFalse(v == other_v)

    def test_append(self):
        v = Vector([1, 2])
        v.append(3)

        self.assertEqual(str(v), 'Vector([1, 2, 3])')

        v = Vector([])
        v.append(1)

        self.assertEqual(str(v), 'Vector([1])')

        v = Vector([1.0, 3.5])
        v.append(3.7)

        self.assertEqual(str(v), 'Vector([1.0, 3.5, 3.7])')

    def test_len(self):
        v = Vector([1, 2])

        self.assertEqual(len(v), 2)

        v = Vector([])

        self.assertEqual(len(v), 0)

        v = Vector([1.5, -0.5, 8])

        self.assertEqual(len(v), 3)

    def test_ndim(self):
        v = Vector([1, 2])

        self.assertEqual(v.ndim(), 2)

        v = Vector([])

        self.assertEqual(v.ndim(), 0)

        v = Vector([1.5, -0.5, 8])

        self.assertEqual(v.ndim(), 3)

    def test_getitem(self):
        v = Vector([1, 2])

        self.assertEqual(v[1], 2)

        v = Vector([])

        with self.assertRaises(IndexError):
            print(v[0])

        v = Vector([1.5, -0.5, 8])

        with self.assertRaises(IndexError):
            print(v[3])

    def test_setitem(self):
        v = Vector([1, 2])
        v[-1] = 3

        self.assertEqual(str(v), 'Vector([1, 3])')

        v = Vector([1, 2])
        v[0] = 3

        self.assertEqual(str(v), 'Vector([3, 2])')

        v = Vector([3, 4])
        with self.assertRaises(IndexError):
            v[2] = 1

    def test_clear(self):
        v = Vector([1, 2, 3])
        v.clear()

        self.assertEqual(str(v), 'Vector([])')

        v = Vector([])
        v.clear()

        self.assertEqual(str(v), 'Vector([])')

        v = Vector([-1, 3.5])
        v.clear()

        self.assertTrue(not v)

    def test_reverse(self):
        v = Vector([1, 2, 3])
        v.reverse()

        self.assertEqual(str(v), 'Vector([3, 2, 1])')

        v = Vector([1.0, 3.5])
        v.reverse()

        self.assertEqual(str(v), 'Vector([3.5, 1.0])')

        v = Vector([1.0])
        v.reverse()

        self.assertEqual(str(v), 'Vector([1.0])')

    def test_abs(self):
        v = Vector([1, 2, 3])

        self.assertEqual(round(abs(v)), 4)

        v = Vector([1, 2, -3])

        self.assertEqual(round(abs(v)), 4)

        v = Vector([1.0, 2, -3])

        self.assertEqual(round(abs(v)), 4)

    def test_argmin(self):
        v = Vector([1, 2, 3])

        self.assertEqual(v.argmin(), 1)

        v = Vector([1, -2])

        self.assertEqual(v.argmin(), 1)

        v = Vector([1.0, -2])

        self.assertEqual(v.argmin(), 1)

    def test_argmax(self):
        v = Vector([1, 2, 3])

        self.assertEqual(v.argmax(), 1)

        v = Vector([1, -2])

        self.assertEqual(v.argmax(), 1)

        v = Vector([1.0, -2])

        self.assertEqual(v.argmax(), 1)

if __name__ == "__main__":
    unittest.main()
