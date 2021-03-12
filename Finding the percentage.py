if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum = 0
    length = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for name in student_marks:
        if name == query_name:
            length = len(student_marks[name])
            for mark in student_marks[name]:
                sum += mark
            break
    avg = float(sum/length)
print("{0:.2f}".format(avg))
