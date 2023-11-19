import csv


def create_csv():
    choice = input("Enter 1 to add new student details. Enter 2 to Exit:")
    if choice == "1":
        file = open('students.csv', 'a', newline='')
        writer = csv.writer(file)
        rollNo = input("Enter Roll No:")
        Name = input("Enter Name:")
        SubjectName = input("Enter Subject Name:")

        writer.writerow([rollNo, Name, SubjectName])
        file.close()
        create_csv()
    else:
        filesys = open("students.csv", 'r')
        csvreader = csv.reader(filesys)
        for row in csvreader:
            print(row)
        filesys.close()
create_csv()
