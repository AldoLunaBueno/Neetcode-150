import pytest
from largest_rect import *

class Test:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.sol = Solution()
    
    @pytest.mark.parametrize("input, expected", [
        ([0], 0),
        ([1], 1),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 2),
    ])
    def test_trivial(self, input, expected):
        assert self.sol.largestRectangleArea(input) == expected

    @pytest.mark.parametrize("input, expected", [
        ([1, 2, 3, 4, 5, 6], 12),
        ([6, 2, 1, 4, 3, 5], 9),
        ([1, 4, 3, 2, 1, 5, 1], 7),
        ([1, 3, 5, 2, 2], 8)
    ])
    def test_drawn_cases(self, input, expected):
        assert self.sol.largestRectangleArea(input) == expected

if __name__=="__main__":
    pytest.main()