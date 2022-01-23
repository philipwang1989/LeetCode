# Sliding Window

Template 1: find interval
```Python
l = 0
while l < len(nums):
    if condition1(nums[l]):
        r = l + 1
        while not condition2(nums[l:r]):
            r += 1
        # if l:r is still in bound, then condition2 is satisfied
        # we can then process l:r as part of our answer
        process(nums[l:r])
        l = r
    else:
        l += 1
```

## Examples
### [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

Input: s = "cbaebabacd", p = "abc"

Output: [0,6]

Explanation:

The substring with start index = 0 is "cba", which is an anagram of "abc".

The substring with start index = 6 is "bac", which is an anagram of "abc".

**Constraints:**
- `1 <= s.length, p.length <= 3 * 10**4`
- `s` and `p` consist of lowercase English letters.


### [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

**Example 1:**

Input: nums = [10,5,2,6], k = 100

Output: 8

Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


### [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

