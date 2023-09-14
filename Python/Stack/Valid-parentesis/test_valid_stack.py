import pytest
from valid_stack import *

sol = Solution()

class Test:
    @pytest.mark.parametrize("input, expected", [
        ("", True),
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("(", False),
        ("]", False),
        ("{", False)
    ])
    def test_trivial(self, input, expected):
        assert sol.isValid(input) == expected
    
    @pytest.mark.parametrize("input, expected", [
        ("()()", True),
        ("()[]{}", True),
        (")(", False),
        ("()(", False),
        (")()", False)
    ])
    def test_no_nested(self, input, expected):
        assert sol.isValid(input) == expected

    @pytest.mark.parametrize("input, expected", [
        ("(())", True),
        ("([{()}])", True),
        ("{([])()}", True),
        ("([)]", False),
        ("(()", False)
    ])
    def test_nested(self, input, expected):
        assert sol.isValid(input) == expected
if __name__=="__main__":
    pytest.main()