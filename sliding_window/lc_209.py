class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ans = float('inf')
        r = l = 0
        curr = 0
        while r < len(nums):

            while r < len(nums) and curr < target:
                curr += nums[r]
                r += 1
            
            while l<r and curr >= target:
                ans = min(ans, r-l)
                curr -= nums[l]
                l += 1
            
        return ans if ans != float('inf') else 0
