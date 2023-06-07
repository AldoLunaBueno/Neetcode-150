import pytest
from min_stack import *




class TestMinStack:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.ms = MinStack()
    
    def test_get_min_trivial(self):
        self.ms.push(0)
        assert self.ms.getMin() == 0

    def test_get_min_update_min(self):
        self.ms.push(0)
        self.ms.push(-1)
        self.ms.pop()
        assert self.ms.getMin() == 0

    def test_get_min_secuence(self):
        self.ms.push(5)
        self.ms.push(4)
        assert self.ms.getMin() == 4
        self.ms.pop()
        self.ms.push(3)
        self.ms.push(0)
        self.ms.push(4)        
        assert self.ms.getMin() == 0

if __name__=="__main__":
    pytest.main()