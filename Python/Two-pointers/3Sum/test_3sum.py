import pytest
from sum3 import *
from deepdiff import DeepDiff as dd

sol = Solution()

class Test:
    @pytest.mark.parametrize("input, expected", [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]])
    ])
    def test_cases(self, input, expected):
        result = sol.threeSum(input)
        if dd(result, expected, ignore_order=True) != {}:
            info = f'''Lists are not equal ignoring order.
            result =   {result}
            expected = {expected}
                                    '''
            assert False, info


if __name__=="__main__":
    pytest.main()