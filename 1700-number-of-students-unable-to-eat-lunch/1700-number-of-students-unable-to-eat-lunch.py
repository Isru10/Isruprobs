class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt=0
        l=len(students)
        while students and cnt<l:
            if students[0]==sandwiches[0]:
                del students[0]
                del sandwiches[0]
                cnt=0
                l-=1
            else:
                students.append(students.pop(0))
                cnt +=1
        return l