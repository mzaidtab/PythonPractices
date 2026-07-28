import student
from data import Students_Record, save_data


def marksAssignment():
    print("------ Marks Assignment System ------")
    while True:
        try:
            ID = input("Enter the student's Registration Number for Marks Assignment: ").strip().lower()
            Student = student.searchStudent(ID)
            print(f"Registered Courses of {Student['name']}:")
            # Convert keys to a list to allow safe, predictable indexing
            course_list = list(Student['Reg_Course'].keys())
            for i, course in enumerate(course_list, start=1):
                print(f"{i}. {course}")
                
            while True:
                courseChoice = input("Enter the course name to assign marks from above: ").strip().lower()
                check = None
                for original_course_name in Student['Reg_Course'].keys():  # noqa: SIM118
                    if original_course_name.strip().lower() == courseChoice:
                        check = original_course_name
                        break
                        
                if check:
                    while True:
                        try:
                            num = float(input(f"Enter the marks obtained by {Student['name']} in {check}: ").strip())
                            if 0 <= num <= 100:
                                grade = GradeCalc(num)
                                Student['Reg_Course'][check] = {
                                    "marks": num, "grade": grade
                                }
                                print(f"Marks for {check} have been successfully assigned to {Student['name']}.")
                                
                                TotalMarks(Student)
                                save_data(Students_Record)
                                break
                            else:
                                print("Invalid marks! Please enter a value between 0 and 100.")
                        except ValueError:
                            print("Please enter a valid numeric value.")
                else:
                    print("Invalid course choice. Please select a valid course from the registered courses.")
                
                choice = input("Do you want to assign marks for another course(yes or no): ").strip().lower()
                if choice != "yes":
                    break
        except student.StudentNotfounderror as e:
            print(e)
        another = input("Do you want to assign marks for another student(yes or no): ").strip().lower()
        
        if another != "yes":
            break
        

def GradeCalc(marks):
    if marks >= 90: return 'A'
    elif marks >= 80: return 'B'
    elif marks >= 70: return 'C'
    elif marks >= 60: return 'D'
    else: return 'F' 

def TotalMarks(Student):
    total = 0
    for details in Student['Reg_Course'].values():
        if isinstance(details, dict):
            total += details.get('marks', 0)
    Student['TMarks'] = total
    return total

def AverageMarks(Student):

    Registered_Courses = len(Student['Reg_Course'])   
    Total_Marks = Student.get('TMarks', 0)
    if Total_Marks == 0 or Registered_Courses == 0:
        return 0
    return Total_Marks / Registered_Courses

def SortStudents():
    if not Students_Record:
        print("No students available to sort.")
        return []
    return sorted(Students_Record, key=lambda s: s['name'].capitalize())

def Topper():
    if not Students_Record:
        print("No students available to determine the topper.")
        return []
    Students_Records = sorted(Students_Record, key=lambda s: s.get('TMarks', 0), reverse=True)
    return Students_Records[:4]
    
def ProcessResultStudents():
    if not Students_Record:
        print("No students available to check for failures.")
        return [], []
    
    # FIX: Check passing logic using average scores instead of aggregate sums
    failed_students = list(filter(lambda fs: AverageMarks(fs) < 40, Students_Record))
    passed_students = list(filter(lambda ps: AverageMarks(ps) >= 40, Students_Record))
    passed_students.sort(key=lambda s: s.get('TMarks', 0), reverse=True)
    return failed_students, passed_students
