# 1

students = {
    1: {"name": "Charan", "age": 19, "marks": 92},
    2: {"name": "Ritesh", "age": 25, "marks": 36},
    3: {"name": "sai", "age": 20, "marks": 45},
    4: {"name": "vishnu", "age": 18, "marks": 56},
    5: {"name": "shiva", "age": 19, "marks": 65}
}
for student_id, detailes in students.items():
    print(f"Student-ID: {student_id} & Name: {detailes["name"]} ; age: {detailes["age"]} - Marks is {detailes["marks"]}")

# 2

import pandas as pd
data = [20,30,40,50,2,3,6,8,10,19,20,24,2,4,5,6]
No_of_studied=data[4:8]
print("No.Of hours_studied",No_of_studied)
Age = data[9:13]
print("Student_age",Age)
screen_time=data[12:18]
print("screen_time",screen_time)
Data_Frame=pd.DataFrame(data)
print(Data_Frame)


#3
def validate_password(password):
    if len(password) >= 8:
        if any(char.isdigit() for char in password):
            if any(char.isalpha() for char in password):
                if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password):
                    print("Password is valid.")
                else:
                    print("Password is invalid. It must contain at least one special character.")
            else:
                print("Password is invalid. It must contain at least one letter.")
        else:
            print("Password is invalid. It must contain at least one digit.")
    else:
        print("Password is invalid. It must be at least 8 characters long.")

password = input("Enter your password: ")

validate_password(password)
