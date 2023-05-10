# Arrays and Hashing

## 217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. ([->](https://leetcode.com/problems/contains-duplicate/))

- Example 1:
  - Input: nums = [1,2,3,1]
  - Output: true
- Example 2:
  - Input: nums = [1,2,3,4]
  - Output: false
- Example 3:

  - Input: nums = [1,1,1,3,3,4,3,2,4,2]
  - Output: true

- Constraints:
  - 1 <= nums.length <= 10<sup>5</sup>
    -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

**Preguntas clave**

**Desarrollo**

Nuestra primera aproximación para el método `containsDuplicate()` fue muy ingenua:

```py
def containsDuplicate(self, nums: list[int]) -> bool:
    for i, x in enumerate(nums[:-1]):
        for y in nums[i+1:]:
            if x == y:
                return True
        return False
```

Eseta es una mejore aproximación:

```py
def containsDuplicate(self, nums: list[int]) -> bool:
    hashset = set()
    for x in nums:            
        if x in hashset:
            return True
        hashset.add(x)
    return False
```

## 242. Valid Anagram

**Desarrollo**

```py
def isAnagram(self, s: str, t: str) -> bool:
    sSort = list(s)
    sSort.sort()
    tSort = list(t)
    tSort.sort()
    
    if sSort == tSort:
        return True
    return False
```

![](sources/2023-05-09-19-29-07.png)




```py
def strToDict(s: str) -> dict:
    sDict = {}
    for e in list(s):
        if e in sDict:                
            sDict[e] += 1
        else:
            sDict[e] = 1
    return sDict

```
![](sources/2023-05-09-20-23-47.png)


```py
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    ...
```

![](sources/2023-05-09-20-51-53.png)

```py
def strToDict(s: str) -> dict:
    sDict = {}
    for e in s:
        sDict[e] = 1 + sDict.get(e, 0)
    return sDict
```

![](sources/2023-05-10-13-44-54.png)