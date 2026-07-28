from datetime import date

import analysis
import data  # noqa: F401
import student


def StudentReportGenerator():
    print("------ Student Report Generation System ------")
    try:
        ID = input("Enter the student's Registration Number for Report Generation: ").strip().lower()
        required = student.searchStudent(ID)
        print("=" * 55)
        print(f"{'STUDENT REPORT': ^55}")
        print("=" * 55)
        print(f"{'Name':.<35}{required['name']:.>15}")
        print(f"{'Registration Number':.<35}{required['regno']:.>15}")
        print(f"{'Department':.<35}{required['Dep']:.>15}")
        print(f"{'Program':.<35}{required['Program']:.>15}")
        print("-" * 55)
        print(f"{'Registered Courses & Marks Details ': ^55}")
        print("-"*55)
        print(f"|{'Courses':<25} | {'Marks/Total':<13} | {'Grade':<8} |")
        print("-"*55)
        for course, details in required['Reg_Course'].items():
            marks = details.get('marks', 'N/A')
            grade = details.get('grade', 'N/A')
            score_string = f"{marks}/100" if marks != 'N/A' else 'N/A'
            print(f"|{course:<25} | {score_string:<13} | {grade:<8} |")
        print("-"*55)
        print(f"{'Total Marks: '} : {required['TMarks']}")
        print("-" *55)
        print(f"{' '*27}Printing Date: {date.today().strftime('%B %d,%Y')}") # noqa: DTZ011
        print("="*55)
    except student.StudentNotfounderror as e:
        print (e)
        
def DetailedAllStudentReport():
    students = analysis.SortStudents()
    print("=" * 55)
    print(f"{'All STUDENTS DETAILED REPORTS': ^55}")
    print("=" * 55)
    for s in students:
        REPORT(s)
    print(" "*27 + "Printing Date: " + date.today().strftime("%B %d,%Y")) # noqa: DTZ011
    print(f"{'END OF STUDENTS': ^55}")
        
    
def REPORT(given):
    required = given
    print(f"{'Name':.<35}{required['name']:.>15}")
    print(f"{'Registration Number':.<35}{required['regno']:.>15}")
    print(f"{'Department':.<35}{required['Dep']:.>15}")
    print(f"{'Program':.<35}{required['Program']:.>15}")
    print("-" * 55)
    print(f"{'Registered Courses & Marks Details ': ^55}")
    print("-"*55)
    print(f"|{'Courses':<25} | {'Marks/Total':<13} | {'Grade':<8} |")
    print("-"*55)
    for course, details in required['Reg_Course'].items():
        marks = details.get('marks', 'N/A')
        grade = details.get('grade', 'N/A')
        score_string = f"{marks}/100" if marks != 'N/A' else 'N/A'
        print(f"|{course:<25} | {score_string:<13} | {grade:<8} |")
    print("-"*55)
    print(f"{'Total Marks: '} : {required['TMarks']}")
    print("-" *55)
    

def AllStudentReport():  
    students = analysis.SortStudents()
    
    print("=" * 105)
    print(f"{'ALL STUDENTS MASTER DETAIL SPREADSHEET': ^105}")
    print("=" * 105)
    
    print(f"| {'Reg No':<12} | {'Student Name':<20} | {'Dept':<6} | {'Program':<8} | {'Registered Courses':<25} | {'Total':<6} |")
    print("-" * 105)
    
    if not students:
        print(f"|{'NO STUDENT RECORDS FOUND':^103}|")
        print("-" * 105)
        return

    course_map = {
        "programming fundamentals": "PF",
        "oop programming": "OOP",
        "data structures": "DS",
        "digital logic design": "DLD",
        "calculus": "Calc",
        "analysis to electronics": "AE"
    }

    for s in students:
        courses_dict = s.get('Reg_Course', {})
        total_marks = s.get('TMarks', 0)
        
        short_courses = []
        for course_name in courses_dict:
            clean_name = str(course_name).strip().lower()
            abbreviation = course_map.get(clean_name, course_name[:4].upper())
            short_courses.append(abbreviation)
            
        courses_str = ", ".join(short_courses) if short_courses else "None"
        
        print(f"| {s['regno']:<12} | {s['name']:<20} | {s['Dep']:<6} | {s['Program']:<8} | {courses_str:<25} | {total_marks:<6} |")     
    print("-" * 105)
    print(" " * 65 + "Printing Date: " + date.today().strftime("%B %d, %Y"))  # noqa: DTZ011
    print(f"{'END OF SPREADSHEET FILE': ^105}")
    print("=" * 105)
    
def viewStudent(student):
    print("=" * 55)
    print(f"{'STUDENT DETAILS': ^55}")
    print("=" * 55)
    print(f"{'Name':.<35}{student['name']:.>15}")
    print(f"{'Registration Number':.<35}{student['regno']:.>15}")
    print(f"{'Department':.<35}{student['Dep']:.>15}")
    print(f"{'Program':.<35}{student['Program']:.>15}")
    print("-" * 55)
    print(f"{'Registered Courses & Marks Details ': ^55}")
    print("-"*55)
    print(f"|{'Courses':<25} | {'Marks/Total':<13} | {'Grade':<8} |")
    print("-"*55)
    for course, details in student['Reg_Course'].items():
        marks = details.get('marks', 'N/A')
        grade = details.get('grade', 'N/A')
        score_string = f"{marks}/100" if marks != 'N/A' else 'N/A'
        print(f"|{course:<25} | {score_string:<13} | {grade:<8} |")
    print("-"*55)
    print(f"{'Total Marks: '} : {student['TMarks']}")
    print("-" *55)
    
    
def PassStudentReport():  
    _, students = analysis.ProcessResultStudents()
     
    
    print("=" * 105)
    print(f"{'ALL STUDENTS MASTER DETAIL SPREADSHEET': ^105}")
    print("=" * 105)
    
    print(f"| {'Reg No':<12} | {'Student Name':<20} | {'Dept':<6} | {'Program':<8} | {'Registered Courses':<25} | {'Total':<6} |")
    print("-" * 105)
    
    if not students:
        print(f"|{'NO STUDENT RECORDS FOUND':^103}|")
        print("-" * 105)
        return

    course_map = {
        "programming fundamentals": "PF",
        "oop programming": "OOP",
        "data structures": "DS",
        "digital logic design": "DLD",
        "calculus": "Calc",
        "analysis to electronics": "AE"
    }

    for s in students:
        courses_dict = s.get('Reg_Course', {})
        total_marks = s.get('TMarks', 0)
        
        short_courses = []
        for course_name in courses_dict:
            clean_name = str(course_name).strip().lower()
            abbreviation = course_map.get(clean_name, course_name[:4].upper())
            short_courses.append(abbreviation)
            
        courses_str = ", ".join(short_courses) if short_courses else "None"
        
        print(f"| {s['regno']:<12} | {s['name']:<20} | {s['Dep']:<6} | {s['Program']:<8} | {courses_str:<25} | {total_marks:<6} |")      
    print("-" * 105)
    print(" " * 65 + "Printing Date: " + date.today().strftime("%B %d, %Y"))  # noqa: DTZ011
    print(f"{'END OF SPREADSHEET FILE': ^105}")
    print("=" * 105)
    

def FailedStudentReport():  
    students, _ = analysis.ProcessResultStudents()
    print("=" * 105)
    print(f"{'ALL STUDENTS MASTER DETAIL SPREADSHEET': ^105}")
    print("=" * 105)
    
    print(f"| {'Reg No':<12} | {'Student Name':<20} | {'Dept':<6} | {'Program':<8} | {'Registered Courses':<25} | {'Total':<6} |")
    print("-" * 105)
    
    if not students:
        print(f"|{'NO STUDENT RECORDS FOUND':^103}|")
        print("-" * 105)
        return

    course_map = {
        "programming fundamentals": "PF",
        "oop programming": "OOP",
        "data structures": "DS",
        "digital logic design": "DLD",
        "calculus": "Calc",
        "analysis to electronics": "AE"
    }

    for s in students:
        courses_dict = s.get('Reg_Course', {})
        total_marks = s.get('TMarks', 0)
        
        short_courses = []
        for course_name in courses_dict:
            clean_name = str(course_name).strip().lower()
            abbreviation = course_map.get(clean_name, course_name[:4].upper())
            short_courses.append(abbreviation)
            
        courses_str = ", ".join(short_courses) if short_courses else "None"
        
        print(f"| {s['regno']:<12} | {s['name']:<20} | {s['Dep']:<6} | {s['Program']:<8} | {courses_str:<25} | {total_marks:<6} |")
        
    print("-" * 105)
    print(" " * 65 + "Printing Date: " + date.today().strftime("%B %d, %Y"))  # noqa: DTZ011
    print(f"{'END OF SPREADSHEET FILE': ^105}")
    print("=" * 105)