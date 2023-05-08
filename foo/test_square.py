import unittest
from square import *

class Test(unittest.TestCase):
    def test_square(self):
        self.assertEqual(Solution.square(2), 4)

if __name__=='__main__':
    unittest.main()