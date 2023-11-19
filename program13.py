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
    for keys in data:
        print(keys[0],keys[1],keys[2])
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