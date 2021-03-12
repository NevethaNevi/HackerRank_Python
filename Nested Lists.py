if __name__ == '__main__':
    student_grade = []
    score_List=[]
    second_largest = []
    # first_value = 0
    # second_value = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grade.append([name,score])
        score_List.append(score)
    score_set = set(score_List)
    score_List = list(score_set)
    score_List.sort()
    for i in range(len(student_grade)):
        if student_grade[i][1] == score_List[1]:
            second_largest.append(student_grade[i][0])
    second_largest.sort()
    for i in second_largest:
        print(i)
    
