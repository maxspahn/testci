import unittest

from summation.addTwoInt import add

class AddTwoIntTest(unittest.TestCase):

    def test_1plus1(self):
        a = 1
        b = 1
        res = add(a, b)
        self.assertEqual(res, 2)

if __name__ == "__main__":
    unittest.main()
