import pytest
from eval_rpn import *

class Test:
    @pytest.fixture(autouse = True)
    def setup(self):
        self.sol = Solution()
    
    @pytest.mark.parametrize("input, expected", [
        (["1", "1", "+"], 2),
        (["-1", "1", "+"], 0),
        (["1", "1", "-"], 0),
        (["1", "-1", "-"], 2),
        (["2", "2", "*"], 4),
        (["2", "-1", "*"], -2),
        (["2", "2", "/"], 1),
        (["4", "-2", "/"], -2),
        ])
    def test_trivial(self, input, expected):
        assert self.sol.evalRPN(input) == expected
    
    @pytest.mark.parametrize("input, expected", [
        (["2", "3", "/"], 0),
        (["-2", "3", "/"], 0),
        (["5", "2", "/"], 2),
        (["5", "-2", "/"], -2)
        ])
    def test_division_trucates_toward_zero(self, input, expected):
        assert self.sol.evalRPN(input) == expected

    @pytest.mark.parametrize("input, expected", [
        # 3 - (1 + 2) = 0
        (["3", "1", "2", "+", "-"], 0), 
        
        # (1 - 3) / (4 / 2) = -1
        (["1", "3", "-", "4", "2", "/", "/"], -1), 
        
        # ((2 + 1) * 3) = 9
        (["2","1","+","3","*"], 9), 
        
        # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),        
        ])
    def test_combined_ops(self, input, expected):
        assert self.sol.evalRPN(input) == expected     

if __name__=="__main__":
    pytest.main()