## Valid Stack

```python
closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue
            if c not in closeToOpen:
                stack.append(c)
            else:
                if closeToOpen[c] != stack[-1]:
                    return False
                else:
                    stack.pop()                
        return stack == []
```

![](sources/2023-06-06-11-01-20.png)

Un pequeño ajuste hizo la diferencia:

```python
stack = [" "]
for c in s:
    if c not in closeToOpen:
        stack.append(c)
```

![](sources/2023-06-06-10-59-42.png)

## Min Stack

```python
class MinStack:
    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)
```

![](sources/2023-06-06-15-04-14.png)

```python
class MinStack:
    def __init__(self):
        self.arr = []
        self.eachMin = [2**31-1]

    def push(self, val: int) -> None:
        self.arr.append(val)
        if val < self.eachMin[-1]:
            self.eachMin.append(val)
        else:
            self.eachMin.append(self.eachMin[-1])

    def pop(self) -> None:
        self.arr.pop()
        self.eachMin.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.eachMin[-1]
```

![](sources/2023-06-06-16-28-31.png)


## Evaluating reverse Polish notation

![](sources/2023-06-08-10-40-08.png)

## Largest rectangle in histogram

```python
def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        min_indices = [-1, len(heights)]
        indices_by_height = [i[0] for i in sorted(enumerate(heights), key = lambda x:x[1])]
        curr_ind = 0
        while curr_ind < len(indices_by_height):
            curr_height = heights[indices_by_height[curr_ind]]
            min_indices_copy = min_indices[:]
            while (curr_ind < len(indices_by_height) 
                   and curr_height == heights[indices_by_height[curr_ind]]):
                ind_of_indices = bisect(min_indices, indices_by_height[curr_ind])
                lim_sup = min_indices[ind_of_indices]
                lim_inf = min_indices[ind_of_indices-1]
                curr_area = (lim_sup - lim_inf - 1) * curr_height
                if curr_area > max_area:
                    max_area = curr_area                
                min_indices_copy.insert(ind_of_indices, indices_by_height[curr_ind])
                curr_ind += 1
                min_indices = min_indices_copy           
        return max_area
```