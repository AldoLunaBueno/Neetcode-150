import pytest
from two_sum_ii import *
sol = Solution()


class Test:
    @pytest.mark.parametrize(
        "inputArr, inputTarget, expected", [
            ([1, 2],    3, [1, 2]),
            ([0, 1, 2], 3, [2, 3])
        ])
    def test_trivial(self, inputArr, inputTarget, expected):
        assert sol.twoSum(inputArr, inputTarget) == expected

    @pytest.mark.parametrize(
        "inputArr, inputTarget, expected", [
            ([1, 1],       2, [1, 2]),
            ([1, 2, 3, 4], 4, [1, 3])
        ])
    def test_use_distincts(self, inputArr, inputTarget, expected):
        assert sol.twoSum(inputArr, inputTarget) == expected

    @pytest.mark.parametrize(
        "inputArr, inputTarget, expected", [
            ([-2, 1, 6, 7],    4, [1, 3]),
            ([-2, -2, -1, 5], -4, [1, 2])
        ])
    def test_negatives(self, inputArr, inputTarget, expected):
        assert sol.twoSum(inputArr, inputTarget) == expected


if __name__ == "__main__":
    pytest.main()
