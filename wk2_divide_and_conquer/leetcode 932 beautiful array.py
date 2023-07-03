# 例子：[1 2 3 4] 

# 将所有的奇数放在 left 部分，所有的偶数放在 right 部分
# 保证等式恒不成立:
#   A[k] * 2 = A[i] + A[j], i < k < j；
#   A[i] 来自 left 部分，A[j] 来自 right 部分
# 例子：[1 3 2 4]

# 对于 [1..N] 的排列，left 部分包括 (N + 1) / 2 个奇数，right 部分包括 N / 2 个偶数。
# 对于 left 部分，进行 k = 1/2, b = 1/2 的仿射变换，把这些奇数一一映射到不超过 (N + 1) / 2 的整数
# 仿射变换性质：如果某个数组（x）是漂亮的，那么对这个数组进行仿射变换 （kx+b），得到的新数组也是漂亮的
# 例子：x = 1 --> kx + b = 1
# 例子：x = 3 --> kx + b = 2

# 对于 right 部分，进行 k = 1/2, b = 0 的仿射变换，把这些偶数一一映射到不超过 (N + 1) / 2 的整数
# 例子：x = 2 --> kx + b = 1
# 例子：x = 4 --> kx + b = 2

# left 和 right 部分变成了和原问题一样，但规模减少一半的子问题，这样就可以使用分治算法解决了。
# 例子：[1 2]

# 解决方法：
# 在 [1..N] 中有 (N + 1) / 2 个奇数和 N / 2 个偶数。
# 我们将其分治成两个子问题，其中一个为不超过 (N + 1) / 2 的整数，并映射到所有的奇数；另一个为不超过 N / 2 的整数，并映射到所有的偶数。

class Solution:
    def beautifulArray(self, n: int):

        def helper(array): 
            if len(array) == 1:
                return array
            
            # 将所有的奇数放在 left 部分，所有的偶数放在 right 部分
            left = [x for x in array if x % 2  == 1]
            right = [x for x in array if x % 2  == 0]

            # 仿射变换
            # 对于 left 部分，进行 k = 1/2, b = 1/2 的仿射变换，把这些奇数一一映射到不超过 (N + 1) / 2 的整数
            left_map = [x/2 + 1/2 for x in left]
            # 对于 right 部分，进行 k = 1/2, b = 0 的仿射变换，把这些偶数一一映射到不超过 (N + 1) / 2 的整数
            right_map = [x/2 for x in right]

            # left 和 right 部分变成了和原问题一样，但规模减少一半的子问题，这样就可以使用分治算法解决了
            left_map_beautify = helper(left_map)
            right_map_beautify = helper(right_map)

            # 仿射变换回来
            left_map_beautify_back = [(x-1/2)*2 for x in left_map_beautify]
            right_map_beautify_back = [x*2 for x in right_map_beautify]

            result = left_map_beautify_back + right_map_beautify_back
            return result
        
        array = [i for i in range(1, n+1)]
        array_beautify = helper(array)
        return array_beautify
    
n = 4
S = Solution()
result = S.beautifulArray(n)
print(result)