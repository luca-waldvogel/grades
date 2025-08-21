import csv
import sys


def start():
    print("""
*********************************
** Welcome to the Grade Center **
*********************************
""")
    avg_grade()
    avg_grade_semester()

def menu():
    print("""
1 = Show all exams
2 = Show grades by module and semester
3 = Add new grade
4 = Exit
""")

    user_in = input('Enter number to navigate: ')
    print()
    match user_in:
        case '1':
            show_exams()
            menu()
        case '2':
            show_grades_module()
            menu()
        case '3':
            add_new()
            menu()
        case '4':
            sys.exit()
        case _:
            print('Choose from 1 to 4')
            menu()

def avg_grade():
    with open("files/grades.csv", "r") as f:
        data = csv.reader(f, delimiter=';')
        grade = 0
        count = 0
        for line in data:
            if not line or line[0] == "Module":
                continue
            grade += float(line[5]) * float(line[4])
            count += float(line[4])
        print(f'Average grade: {round(grade / count, 1)}')

def avg_grade_semester():
    with open("files/grades.csv", "r") as f:
        data = csv.reader(f, delimiter=';')
        grade = 0
        count = 0
        semester = 0
        for line in data:
            if not line or line[0] == "Module":
                continue
            semester = int(line[6])

    with open("files/grades.csv", "r") as f:
        data = csv.reader(f, delimiter=';')
        for line in data:
            if not line or line[0] == "Module":
                continue
            if int(line[6]) == semester:
                grade += float(line[5]) * float(line[4])
                count += float(line[4])
        print(f'Average grade in semester {semester}: {round(grade / count, 1)}')

def show_exams():
    # find block size
    with open("files/grades.csv", "r") as f:
        data = csv.reader(f, delimiter=';')
        size1 = 0
        size2 = 0
        size3 = 0
        size4 = 0
        size5 = 0
        size6 = 0
        size7 = 0
        
        for line in data:
            counter = 1
            for i in line:
                match counter:
                    case 1:
                        if len(i) > size1:
                            size1 = len(i)
                    case 2:
                        if len(i) > size2:
                            size2 = len(i)
                    case 3:
                        if len(i) > size3:
                            size3 = len(i)
                    case 4:
                        if len(i) > size4:
                            size4 = len(i)
                    case 5:
                        if len(i) > size5:
                            size5 = len(i)
                    case 6:
                        if len(i) > size6:
                            size6 = len(i)
                    case 7:
                        if len(i) > size7:
                            size7 = len(i)
                counter += 1
            
    # write block
    with open("files/grades.csv", "r") as f:
        data = csv.reader(f, delimiter=';')
        string = ''
        for line in data:
            counter = 1
            for value in line:
                match counter:
                    case 1:
                        string += value
                        for j in range(size1 + 2 - len(value)):
                            string += ' '
                    case 2:
                        string += value
                        for j in range(size2 + 2 - len(value)):
                            string += ' '
                    case 3:
                        string += value
                        for j in range(size3 + 2 - len(value)):
                            string += ' '
                    case 4:
                        string += value
                        for j in range(12 - len(value)):
                            string += ' '
                    case 5:
                        string += value
                        for j in range(8 - len(value)):
                            string += ' '
                    case 6:
                        string += value
                        for j in range(7 - len(value)):
                            string += ' '
                    case 7:
                        string += value
                        for j in range(8 - len(value)):
                            string += ' '
                counter += 1
            string += '\n'
        print(string)

def show_grades_module():
    with open("files/grades.csv", "r") as f:
        data = csv.reader(f, delimiter=';')
        string = f''
        counter = 1
        for line in data:
            if line[0] == 'Module':
                module = line[0]
                continue
            if int(line[6]) == counter:
                string += f'\nSemester {counter}:\n'
                counter += 1
            if line[0] == module:
                string = string[:-4]
                string += f'{round(((float(line[5]) * float(line[4])) + grade) *2)/2}\n'
            else:
                grade = float(line[5]) * float(line[4])
                string += f'{line[0]}: {round((float(line[5]) * float(line[4]))*2)/2}\n'
                module = line[0]
    print(string)

def add_new():
    with open("files/grades.csv", "a", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        module = input("Module: ")
        name = input("Name: ")
        exam_type = input("Exam type: ")
        date = input("Date: ")
        weight = input("Weight: ")
        grade = input("Grade: ")
        semester = input("Semester: ")
        writer.writerow([module, name, exam_type, date, weight, grade, semester])
        
    