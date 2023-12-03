import pickle

def storeData():
    emp = []
    EmpNo = int(input('Enter Employee No:'))
    Name = input('Enter Employee Name:')
    Salary = float(input('Enter Employee Salary:'))
    data=[EmpNo, Name, Salary]
    emp.append(data)
    emps_data = open('binaryFile.bin', 'wb')
    
    pickle.dump(emp, emps_data)                     
    emps_data.close()

def readData():
    file = open('binaryFile.bin', 'rb')
    data = pickle.load(file)
    inp = input('Enter Employee No to update marks: ')

    found = False
    for employee in data:
        if str(employee[0]) == inp:
            print('Employee found. Details:', employee)
            new_salary = float(input('Enter new Salary: '))
            employee[2] = new_salary  # Update the Salary
            found = True

    file.close()

    if not found:
        print('Employee not found')

    # Writing the updated data back to the file
    file = open('binaryFile.bin', 'wb')
    pickle.dump(data, file)
    file.close()


def program():
    user_choice = input("Enter 1 to run Program. Enter 2 to Exit: ")
    if user_choice == "1":
        storeData()
        readData()
        program()
    else:
        print('Thank You!!!')
program()