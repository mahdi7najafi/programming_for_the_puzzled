if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
    print(len(students))
    for i in range(len(students) - 1):
        iSm = i
        for j in range(i+1, len(students)):
            if students[j][1] < students[iSm][1]:
                iSm = j
        students[iSm][1], students[i][1] = students[i][1], students[iSm][1]
    print(students)