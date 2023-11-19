import mysql.connector
db=mysql.connector.connect(host="localhost", user="root", password="", database="pythonMysql")
cursor=db.cursor()
def check_records():
    user_choice = input("Enter 1 to Check Employee Details. Enter 2 to Exit: ")
    if user_choice == "1":
        emp_no = input("Enter your emp no: ")
        query = "SELECT * FROM `employee` WHERE `emp_no`='"+emp_no+"'"
        cursor.execute(query)
        cursor.fetchall()
        if cursor.rowcount > 0:
            cursor.execute(query)
            for records in cursor:
                print(records)
        else:
            print("No Records Found!")
        check_records()
    else:
        print("Thank You!!!")
check_records()