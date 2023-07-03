class Solution:
    def searchMatrix(self, matrix, target):
        
        # Z 字形查找
        # 从矩阵 matrix 的右上角进行搜索, 如果位于位置 (x,y)，那么以matrix的左下角为左下角、以 (x,y) 为右上角的矩阵中进行搜索

        ncol = len(matrix[0])
        nrow = len(matrix)
        x, y = 0, ncol - 1
        while x >= 0 and x <= (nrow-1) and y >= 0 and y <= (ncol-1):
            # 如果 matrix[x,y]=target，说明搜索完成
            if target == matrix[x][y]:
                return True
            
            # 如果 matrix[x,y]>target，由于每一列的元素都是升序排列的，那么在当前的搜索矩阵中，所有位于第 y 列的元素都是严格大于 target 的，
            # 因此我们可以将它们全部忽略，即将y = y - 1
            elif matrix[x][y]>target:
                y = y-1
            
            # 如果 matrix[x,y]<target，由于每一行的元素都是升序排列的，那么在当前的搜索矩阵中，所有位于第 x 行的元素都是严格小于 target 的，
            # 因此我们可以将它们全部忽略，即将x = x + 1
            else:
                x = x + 1
        return False



# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 15
matrix = [[1,1]]
target = 1
S = Solution()
result = S.searchMatrix(matrix, target)
print(result)

