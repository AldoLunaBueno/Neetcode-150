
import unittest
from top_k_frequent_elements import Solution as sol
from deepdiff import DeepDiff

class Test(unittest.TestCase):
    def test_trivial(self):
        result = sol.topKFrequent(self, [0], 1)
        expected = [0]
        Test.assertListEqualIgnoringOrder(self, result, expected)
    
    def test_k_one(self):
        result = sol.topKFrequent(self, [1, 0, 0], 1)
        expected = [0]
        Test.assertListEqualIgnoringOrder(self, result, expected)
    
    def test_k_two(self):
        result = sol.topKFrequent(self, [1, 3, 2, 1, 1, 2], 2)
        expected = [1,2]
        Test.assertListEqualIgnoringOrder(self, result, expected)
        
    def assertListEqualIgnoringOrder(self, result: list[int], expected: list[int]):
        if DeepDiff(result, expected, ignore_order=True) != {}:
            info = f'''Lists are not equal ignoring order.
            result =   {result}
            expected = {expected}
            '''
            assert False, info

if __name__=='__main__':
    unittest.main()