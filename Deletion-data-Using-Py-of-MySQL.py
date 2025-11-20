import mysql.connector  
class Employee:     
    def __init__(self, data):         
        # data must be a tuple with 6 items
        (self.EmployeeID,self.Firstname,self.Email,self.PhoneNumber,self.Position,
         self.Department) = data  
        
def fetchEmployee(cursor):     
    cursor.execute("SELECT * FROM employees")      
    return list(cursor)
  
def insertdata(cursor, emp):     
    q = """
        INSERT INTO employees
        (EmployeeID, Firstname, Email, PhoneNumber, Position, Department)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        emp.EmployeeID,emp.Firstname,emp.Email,emp.PhoneNumber,
        emp.Position,emp.Department
    )
    cursor.execute(q, values)  

def Updatedata(cursor, emp):
    q = """
        UPDATE employees 
        SET Firstname = %s,
            Email = %s,
            PhoneNumber = %s,
            Position = %s,
            Department = %s
        WHERE EmployeeID = %s
    """
    
    values = (
        emp.Firstname,
        emp.Email,
        emp.PhoneNumber,
        emp.Position,
        emp.Department,
        emp.EmployeeID   # WHERE condition
    )
    cursor.execute(q, values)

def deleteData(cursor, empid):
    q = "DELETE FROM employees WHERE EmployeeID = %s"
    cursor.execute(q, (empid,))

def main():     
    try:         
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='anant',
            database='db1'
        )         
        if mydb.is_connected():
            print("Connected to MySQL..")
            cursor = mydb.cursor()
            # employeeList = fetchEmployee(cursor)
            # for x in employeeList:
            #     print(x)

            # # TO INSERT THE DATA...
            # emp = Employee((17, 'Anant', 'anant@gmail.com', 88997711, 'Manager', 'I.T'))
            # insertdata(cursor, emp)
            # mydb.commit()

            # # print("Employee inserted successfully!")

            #to Update the Data...
            # emp=Employee((3, 'Aditya ', 'aditya@gmail.com', 88995869, 'Manager', 'I.T'))
            # Updatedata(cursor, emp)
            # mydb.commit()
            # employeeList = fetchEmployee(cursor)
            # for x in employeeList:
            #     print(x)

            deleteData(cursor,6)
            mydb.commit()
            employeeList = fetchEmployee(cursor)
            for x in employeeList:
                print(x)

        else:             
            print("Connection Failed..")     

    except mysql.connector.Error as e:         
        print("Error:", e)     

    finally:         
        if mydb.is_connected():             
            cursor.close()             
            mydb.close()  


if __name__ == '__main__':     
    main()
