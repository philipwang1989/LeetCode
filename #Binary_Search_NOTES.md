# Leetcode Binary Search

Binary search has the following search application:

1. Exactly equal
2. Greater than or less than
3. Leftmost or rightmost in the case of repeated numbers

## Exactly equal

```python
def binarySearch(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1
```

This is fairly easy to understand.

## Greater than (smallest upper bound)

Given: [2, 3, 5, 7, 11, 13, 17]
Target: 7
Upper bound is then 11.

```python
def binarySearchUpper(nums, target):
    l = 0
    r = len(nums) - 1
    mid = (l + r)//2
    while l < r:
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
        mid = (l + r)//2
    return mid
```

## Less than (largest lower bound)

Given: [2, 3, 5, 7, 11, 13, 17]
Target: 7
Lower bound is then 5.

```python
def binarySearchLower(nums, target):
    l = 0
    r = len(nums) - 1
    mid = (l + r + 1)//2 # "ceil"
    while l < r:
        if nums[mid] < target:
            l = mid
        else:
            r = mid - 1
        mid = (l + r + 1)//2
    return mid
```

## Leftmost

Given: [2, 3, 5, 7, 7, 7, 11, 13, 17]
Target: 7
Leftmost is 3.

```python
def binarySearchLeft(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r)//2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l
```

## Rightmost

Given: [2, 3, 5, 7, 7, 7, 11, 13, 17]
Target: 7
Rightmost is 5.

```python
def binarySearchRight(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r)//2
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l - 1
```
