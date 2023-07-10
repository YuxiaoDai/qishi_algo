# 将左右边界分别初始化为 1 和 n是给定的版本数量。
# 设定左右边界之后，每次我们都依据左右边界找到其中间的版本，检查其是否为正确版本。
# 如果该版本为正确版本，那么第一个错误的版本必然位于该版本的右侧，我们缩紧左边界；
# 否则第一个错误的版本必然位于该版本及该版本的左侧，我们缩紧右边界。
# 这样我们每判断一次都可以缩紧一次边界，而每次缩紧时两边界距离将变为原来的一半，因此我们至多只需要缩紧 O(logn) 次。


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (r - l)//2 + l
            if (isBadVersion(mid) and not isBadVersion(mid - 1)) or (isBadVersion(mid)  and mid == 1):
                return mid
            elif (isBadVersion(mid) and isBadVersion(mid - 1)):
                r = mid - 1
            else:
                l = mid + 1