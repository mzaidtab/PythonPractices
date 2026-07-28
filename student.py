import copy

from data import Students_Record, add_student, courses, save_data


class StudentNotfounderror(Exception):
    pass


def addStudent():
    print("========  Student Registration System =========")
    while True:
        name = input("Enter the Student's Name: ").strip()
        RegNo = input(f"Enter the {name}'s Registration Number: ").strip()
        dep = input(f"Enter the {name}'s Department: ").strip()
        pro = input("Enter the Program: ").strip()
        
        student_det = {
            'name': name,
            'regno': RegNo,
            'Dep': dep,
            'Program': pro,
            'Reg_Course': {},
            'TMarks': 0
        }
        
        selection = input("Do you want to Register courses for the student(yes or no): ").strip().lower()
        if selection == "yes":
            courseReg(student_det)
            
        bbol = add_student(student_det)
        if(bbol):
            print(f"{student_det['name']} is succesfully registered..")
        else:
            print("Unable to register the student.....")
        choice = input("Do you want to add another student(yes or no): ").strip().lower()
        if choice != "yes":
            break     
        
def courseReg(Details):
    print("------ Course Registration System ------")
    print('''Available Courses:
  1.Programming Fundamentals
  2.OOP Programming
  3.Data Structures
  4.Digital Logic Design
  5.Calculus
  6.Analysis to Electronics''') 
    
    while True:
        validity = None
        course = input("Enter the Course from given list: ").strip().lower()
        for items in courses:
           if items.strip().lower() == course:
               validity = items
               break
               
        if validity is None:
            print("Invalid course name! Please choose a course from the list.")
            continue
            
        if validity in Details['Reg_Course']:
            print(f"The course {validity} is already registered.")
            continue 
        else:
            Details['Reg_Course'][validity] = {'marks': 'N/A', 'grade': 'N/A'}
            print(f"The Course {validity} has been successfully registered.")
            
        choice = input("Do you want to register another Course(yes or no): ").strip().lower()
        if choice != "yes":
            break
        
def regCorMan():
    try:
        ID = input("Enter the Student's Registration Number for Course Registration: ").strip().lower()
        Student = searchStudent(ID)
        courseReg(Student)
    except StudentNotfounderror as e:
        print(e)

def searchStudent(ID):
    for Student in Students_Record:
        if Student['regno'].strip().lower() == ID.strip().lower():
            return Student
    raise StudentNotfounderror("Student Not Found!")
    
def RemoveStudent():
    try:
        ID = input("Enter the Student's Registration Number for Removal: ").strip().lower()
        Student = searchStudent(ID)
        Temp = copy.deepcopy(Student)
        Students_Record.remove(Student)
        save_data(Students_Record)
        print(f"Student {Temp['name']} has been removed from the records.")
    except StudentNotfounderror as e:
        print(e)
     
        
def ViewPassed():
    import analysis
    _, passed_students = analysis.ProcessResultStudents()
    
    print("=" * 45)
    print(f"{'PASSED STUDENTS REPORT':^45}")
    print("=" * 45)
    print(f"| {'Reg No':<12} | {'Student Name':<24} |")
    print("-" * 45)
    
    if not passed_students:
        print(f"|{'NO PASSED STUDENT RECORDS FOUND':^41}|")
    else:
        for s in passed_students:
            print(f"| {s['regno']:<12} | {s['name']:<24} |")         
    print("-" * 45)

def viewFailed():
    import analysis
    failed_students , _ = analysis.ProcessResultStudents()
    print("=" * 45)
    print(f"{'FAILED STUDENTS REPORT':^45}")
    print("=" * 45)
    print(f"| {'Reg No':<12} | {'Student Name':<24} |")
    print("-" * 45)
    
    if not failed_students:
        print(f"|{'NO FAILED STUDENT RECORDS FOUND':^41}|")
    else:
        for s in failed_students:
            print(f"| {s['regno']:<12} | {s['name']:<24} |")         
    print("-" * 45)
    
    