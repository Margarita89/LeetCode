from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        General idea: topological sort solve with bfs.
        1. Create 2 dictionaries: 'courses' to store a list of next courses for each courses in prerequisites, 'prer_count' to store a count of prerequisite courses.
        2. Put all courses that are not in prer_count (so they do not have prerequisites) into deque 'q' and answer
        3. BFS with deque 'q': popleft course from deque and decrease prer_count by 1 for all courses that had this course as prerequisite. If prer_count[any course] == 0 then append it to deque and answer
        5. Finally check if the length of answer is the same as number of courses, if not -> return []
        """
        courses = defaultdict(list)
        prer_count = defaultdict(int)
        q = deque()
        ans = []
        for pair in prerequisites:
            courses[pair[1]].append(pair[0])
            prer_count[pair[0]] += 1
        for n in range(numCourses):
            if n not in prer_count:
                q.append(n)
                ans.append(n)
        
        while q:
            course = q.popleft()
            for next_course in courses[course]:
                prer_count[next_course] -= 1
                if prer_count[next_course] == 0:
                    q.append(next_course)
                    ans.append(next_course)
        if len(ans) == numCourses:
            return ans
        return []210. Course Schedule II