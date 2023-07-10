
# 在数组中找到两个数，使得它们的和等于目标值，可以首先固定第一个数，然后寻找第二个数，第二个数等于目标值减去第一个数的差。
# 利用数组的有序性质，可以通过二分查找的方法寻找第二个数。
# 为了避免重复寻找，在寻找第二个数时，只在第一个数的右侧寻找。

class Solution:
    def twoSum(self, numbers, target):
        def binary_search(num, target):
            l, r = 0, len(num)-1
            while l <= r:
                mid = (r-l)//2 + l
                if num[mid] == target: 
                    return mid
                elif num[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        n = len(numbers)
        for i in range(n):
            target_num = target - numbers[i]
            j = binary_search(numbers[(i+1):], target_num)
            if j != -1:
                return [i+1,i+j+2]
            
numbers = [2,7,11,15]
target = 9
S = Solution()
result = S.twoSum(numbers, target)
print(result)