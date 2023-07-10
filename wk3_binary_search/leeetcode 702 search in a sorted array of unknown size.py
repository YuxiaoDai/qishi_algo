# 本题的难点在于如何确定搜索边界
# 我们可以先定义边界为【0,1】，然后不断逼近合适的边界
# 如果reader.get(right) < target, 说明左边界可以更新为left = right。
# 但如果更新right = right + 1， 右侧边界的寻找则非常慢，因此直接更新右边界为right = right * 2
# 确定了左右边界后，剩下的就是最简单的二分查找了

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 1
        while target > reader.get(right):
            left = right
            right = right * 2

        while left <= right:
            mid = (right - left)//2 + left
            if reader.get(mid) > target:
                right = mid - 1
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                return mid
        return -1