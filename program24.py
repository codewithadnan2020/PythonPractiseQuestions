import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", password="", database="pythonMysql")
cursor=db.cursor()
def update_records():
    user_choice = input("Enter 1 to Update Employee Details. Enter 2 to Exit: ")
    if user_choice == "1":
        emp_no = input("Enter your emp no: ")
        query = "SELECT * FROM `employee` WHERE `emp_no`='"+emp_no+"'"
        cursor.execute(query)
        cursor.fetchall()
        if cursor.rowcount > 0:
            cursor.execute(query)
            for records in cursor:
                print(records)
                print('''Enter 1 -> Update Emp Name
Enter 2 -> Update Emp Salary''')
                update_field = input("Enter your choice: ")
                new_value = input("Enter A New Value: ")
                if update_field == "1":
                    update_query  = "UPDATE `employee` SET `name`='"+new_value+"' WHERE `emp_no`='"+emp_no+"'"
                    cursor.execute(update_query)
                    print('Employee '+emp_no+' Updated Successfully!')
                elif update_field == "2":
                    update_query  = "UPDATE `employee` SET `salary`='"+new_value+"' WHERE `emp_no`='"+emp_no+"'"
                    cursor.execute(update_query)
                    print('Employee '+emp_no+' Updated Successfully!')
                else:
                    print('Invalid choice! Try Again...')
        else:
            print("No Records Found!")
        update_records()
    else:
        print("Thank You!!!")
update_records()