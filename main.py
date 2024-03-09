import psycopg
import os
# database params to login
db_params = {
    "host": "localhost",
    "dbname": "Python",
    "user": "postgres",
    "password": "3005",
}

# main loop function for io and calling other functs
def main():
    while(True):
        
        print("\nSIMPLE DATABASE OPERATIONS\n")

        print("(1) Get all students.")
        print("(2) Add a student.")
        print("(3) Update student email.")
        print("(4) Delete student.")
        print("(5) QUIT\n")

 
        
        try:
            choice = int(input("Enter your choice: "))
            os.system('cls')
           
        except ValueError:
            print("Invalid input, try again.")
            continue
        
        if choice == 1:
            getAllStudents()
        elif choice == 2:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == 3:
            try:
                student_id = int(input("Enter student ID: "))
                new_email = input("Enter new email: ")
                updateStudentEmail(student_id, new_email)
            except ValueError:
                print("Invalid input. Student ID must be a number.")
        elif choice == 4:
            try:
                student_id = int(input("Enter student ID to delete: "))
                deleteStudent(student_id)
            except ValueError:
                print("Invalid input. Student ID must be a number.")
        elif choice == 5:
            print("Exiting the program.")
            break




# function that uses params to get all students through query
def getAllStudents():
    try:
        with psycopg.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Students")
                records = cursor.fetchall()
                for record in records:
                    print(record)
    except Exception as e:
        print(f"Error: {e}")

# function that takes input params and using them attempts to add a new student through db
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        with psycopg.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO Students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
                values = (first_name, last_name, email, enrollment_date)
                cursor.execute(sql, values)
                connection.commit()
                print("Student added successfully!")
    except Exception as e:
        print(f"Error: {e}")
# function that takes input params and using them attempts to update student email through db
def updateStudentEmail(student_id, new_email):
    try:
        with psycopg.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                sql = "UPDATE Students SET email = %s WHERE student_id = %s"
                values = (new_email, student_id)
                cursor.execute(sql, values)
                connection.commit()
                print("Email updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
# function that takes student id and trys to delete it if it exists in db
def deleteStudent(student_id):
    try:
        with psycopg.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM Students WHERE student_id = %s"
                values = (student_id,)
                cursor.execute(sql, values)
                connection.commit()
                print("Student deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

main()

# python main.py