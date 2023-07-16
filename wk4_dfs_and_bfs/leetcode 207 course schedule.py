# BFS:
# 让入度为 0 的课入列，它们是能直接选的课。
# 然后逐个出列，出列代表着课被选，需要减小相关课的入度。
# 如果相关课的入度新变为 0，安排它入列、再出列……直到没有入度为 0 的课可入列。

# BFS 前的准备工作
# 每门课的入度需要被记录，我们关心入度值的变化。
# 课程之间的依赖关系也要被记录，我们关心选当前课会减小哪些课的入度。
# 因此我们需要选择合适的数据结构，去存这些数据：哈希表

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use a dictionary to save the course's in-degree and its following courses
        in_degree = {course: [0,[]] for course in range(numCourses)}
        for course, prereq in prerequisites:
            in_degree[course][0]  += 1
            in_degree[prereq][1].append(course)

        # start_courses are courses that do not have any prerequisite (in degree = 0)
        start_courses = [course for course in in_degree if in_degree[course][0] == 0]

        # created a double ended queue
        queue = deque(start_courses)

        # BFS
        # Loop while queue is not empty
        while queue:
            # Since BFS uses FIFO, pop the current node from the left 
            node = queue.popleft()
            numCourses -= 1
            for next_course in in_degree[node][1]:
                in_degree[next_course][0] -= 1
                if in_degree[next_course][0] == 0:
                    queue.append(next_course)

        return numCourses == 0

