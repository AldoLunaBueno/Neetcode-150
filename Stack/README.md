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

