import json

Students_Record = []

courses = (
    "Programming Fundamentals",
    "OOP Programming",
    "Data Structures",
    "Digital Logic Design",
    "Calculus",
    "Analysis to Electronics"
)
Path = "Student.json"

def load_data():
    try:
        with open (Path,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(students):
    try:
        with open (Path,"w") as file:
            json.dump(students,file,indent=4)
            print(f"Data Sucessfully stored in the file {Path}")
    except IOError as e:  # noqa: UP024
        print(f"Error Storing to File: {e}")
             
            
    

def add_student(students):
    if students:
        Students_Record.append(students)
        save_data(Students_Record)
        return True
    return False
    
    
