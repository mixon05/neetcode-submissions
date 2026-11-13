class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_grades = defaultdict(list)
        for student_id, score in items:
            if len(student_grades[student_id]) == 5:
                if student_grades[student_id][0] < score:
                    heapq.heappushpop(student_grades[student_id], score)
            else:
                heapq.heappush(student_grades[student_id], score)
        res = []
        students = list(student_grades.keys())
        heapq.heapify(students)
        while students:
            student_id = heapq.heappop(students)
            res.append([student_id, sum(student_grades[student_id]) // len(student_grades[student_id])])
        return res