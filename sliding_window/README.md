# Sliding Window

Template 1:
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

Template 2:
```Python
l = 0
for r < len(nums):
    process(nums[l:r])  // sum, product etc.
    while condition1(argv):
        # get output, process sth. etc.
        l += 1 # update l as needed (shrink window, for example)
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

**Constraints**
- `1 <= nums.length <= 3 * 10**4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10**6`


### [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray `[numsl, numsl+1, ..., numsr-1, numsr]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

**Example 1:**

Input: target = 7, nums = [2,3,1,2,4,3]

Output: 2

Explanation: The subarray [4,3] has the minimal length under the problem constraint.

**Constraints**
- `1 <= target <= 10**9`
- `1 <= nums.length <= 10**5`
- `1 <= nums[i] <= 10**5`
