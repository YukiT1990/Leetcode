# 1086. High Five

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items = sorted(items, key=lambda x: x[1], reverse=True)
        students_record = dict()
        for student, score in items:
            if student in students_record.keys():
                students_record[student].append(score)
            else:
                students_record[student] = [score]
        # print(students_record)
        result = []    
        for key in students_record.keys():
            ave = 0
            if len(students_record[key]) >= 5:
                ave = sum(students_record[key][:5]) // 5
            else:
                ave = sum(students_record[key]) // len(students_record[key])
            result.append([key, ave])
            
        result = sorted(result, key=lambda x: x[0])
        return result