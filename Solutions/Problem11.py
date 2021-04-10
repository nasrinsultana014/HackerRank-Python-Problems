if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    queryScores = student_marks[query_name]
    sum = 0.00
    for i in range(len(queryScores)):
      sum = sum + queryScores[i]
    
    average = sum/len(queryScores)
    
    print("{:.2f}".format(average))