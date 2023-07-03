class Solution:
    def helper(self, nums, left, right):
        if left == right:
            return nums[left]
        
        
        mid = (right + left) // 2 
        # mid = (right - left) // 2 + left # both options are fine
        
        left_majority = self.helper(nums, left, mid)
        right_majority = self.helper(nums, mid + 1, right)
        #left_majority = self.helper(nums, left, mid - 1) # dont' use [left, mid-1] and [mid, right], it will cause infinite recursion
        #right_majority = self.helper(nums, mid, right)

        if left_majority == right_majority:
            return left_majority
        else:
            left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)
            return left_majority if left_count > right_count else right_majority
        
    def majorityElement(self, nums):
        result = self.helper(nums, 0, len(nums) - 1)
        return result
nums = [3,2,3]
S = Solution()
result = S.majorityElement(nums)
        
print(result)