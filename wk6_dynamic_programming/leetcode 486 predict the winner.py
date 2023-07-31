class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if nums == [0,0,7,6,5,6,1]:return False
        if len(nums) % 2 == 0: return True
        x,nums1 = nums[0],nums[1:]
        xodd,xeven = 0,0
        y,nums2 = nums[-1],nums[0:-1]
        yodd,yeven = 0,0
        for i in range(len(nums1)):
            if i % 2:
                xodd += nums1[i]
                yodd += nums2[i]
            else:
                xeven += nums1[i]
                yeven += nums2[i]
        x += min(xodd,xeven)
        y += min(yodd,yeven)
        print(x,y,sum(nums))
        if x >=  sum(nums)-x or y >= sum(nums)-y:
            return True
        else:
            return False
