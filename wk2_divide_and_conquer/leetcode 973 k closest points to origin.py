# 经典topk问题
# 借鉴快速排序的思想。快速排序中的划分操作每次执行完后，都能将数组分成两个部分，
# 其中小于等于分界值 pivot 的元素都会被放到左侧部分，而大于 pivot 的元素都都会被放到右侧部分。
# 与快速排序不同的是，在本题中我们可以根据 k 与 pivot 下标的位置关系，只处理划分结果的某一部分

import random
class Solution:
    def kClosest(self, points, k):

        def helper(left, right, k):
            
            pivot_id = random.randint(left, right)
            pivot_value = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2

            # 把pivot换到最右端 
            points[right], points[pivot_id] = points[pivot_id], points[right]

            # 设置指标mark，mark左侧是小于pivot，mark右侧是大于pivot
            # 最开始把mark设置在最左端再往左，之后会不断移动
            mark = left - 1    
            for i in range(left, right):
                if points[i][0] ** 2 + points[i][1] ** 2 <= pivot_value:
                    # 当point[i]小于pivot_value时候
                    # 向右侧移动mark光标，并替换mark和当前point[i]位置
                    # mark位置永远小于当前point[i]位置, 在mark上被替换的点，已经经过检验，可以安全替换当前point[i]，不会出现遗漏现象
                    mark += 1
                    points[i], points[mark] = points[mark], points[i]

            # 最后替换mark和当前point[right]位置（也就是pivot位置）
            mark += 1
            points[right], points[mark] = points[mark], points[right]

            # 现在，pivot左侧是小于pivot，pivot右侧是大于pivot
            # [left, mark-1] 都小于等于 pivot, [mark+1, right] 都大于 pivot

            if k == mark - left + 1:
                return 
            elif k < mark - left + 1:
                helper(left, mark - 1, k)
            else:
                helper(mark + 1, right, k - (mark - left + 1))
        
        n = len(points)
        helper(0, n - 1, k)
        return points[:k]

