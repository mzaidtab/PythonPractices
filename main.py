import analysis
import report
import student


def RegMain():
    while True:
        print("="*50)
        print(f"{'Student Registration System': ^50}")
        print("="*50)
        print("1.Add New Student.")
        print("2.Register Courses for Student.")
        print("3.Remove Student.")
        print("4.Exit the System.")
        print("-"*50)
        try:
            raw_choice = (input("Enter your choice: ").strip())
            choice = int(raw_choice)
            match choice:
                case 1:
                    student.addStudent()
                case 2:
                    student.regCorMan()
                case 3:
                    student.RemoveStudent()
                case 4:
                    print("Exiting the System........")
                    break
                case _:
                    print("Invalid Choice")
        except ValueError :
            print("Invalid Input!!")


def PAO():
    while True:
        print("="*50)
        print(f"{'Student Performance & Analysis System': ^50} ")
        print("="*50)
        print("1.Assign Marks to Students")
        print("2.Calculate Total For each Student.")
        print("3.Search Specific Student.")
        print("4.Check Toppers.")
        print("5.Check Failed Students")
        print("6.Check Passed Students") 
        print("7.Exit the System..")
        try:
            raw_choice = (input("Enter your choice: ").strip())
            choice = int(raw_choice)
            match choice:
                case 1:
                    analysis.marksAssignment()
                case 2:
                    analysis.TotalMarks()
                case 3:
                    try:
                        Id = input("Enter the ID of the Required Student: ").strip().lower()
                        Stu = student.searchStudent(Id)
                        report.viewStudent(Stu)
                    except student.StudentNotfounderror as e:
                        print(e)
                case 4:
                    analysis.Topper()
                case 5:
                    student.viewFailed()
                case 6:
                    student.ViewPassed()
                case 7:
                    print("Exiting the Performance & Analysis System......")
                    break
                case _:
                    print("Invalid Choice...\n")
        except ValueError :
            print("Invalid Input!!")

def ROI():
    while True:
        print("="*50)
        print(f"{'Report and Information System': ^50}")
        print("="*50)
        print("1.All Students Report.")
        print("2.Specific Student's Report.")
        print("3.Listed Students Report.")
        print("4.Failed Student's Report.")
        print("5.Passted Student's Report.")
        print("6.Exiting the System.....")
        try:
            raw_choice = (input("Enter your choice: ").strip())
            choice = int(raw_choice)
            match choice:
                case 1:
                    report.DetailedAllStudentReport()
                case 2:
                    report.StudentReportGenerator()
                case 3:
                    report.AllStudentReport()
                case 4:
                    report.FailedStudentReport()
                case 5:
                    report.PassStudentReport()
                case 6:
                    print("Exiting the Report Management System.....")
                case _:
                    print("Invalid choice!!!!!")
        except ValueError :
            print("Invalid Input!!")
                        

while True:
    print("="*50)
    print(f"{'Student Performance Analysis System': ^50}")
    print("="*50)
    print("1.Registration Related Operations.")
    print("2.Performance Analysis Operations.")
    print("3.Report OR Information Related Operations.")
    print("4.Exit the System.")
    print("-"*50)
    try:
        raw_choice = (input("Enter your choice: ").strip())
        choice = int(raw_choice)
        match choice:
            case 1:
                RegMain()
            case 2:
                PAO()
            case 3:
                ROI()
            case 4:
                print("Exiting the System........")
                break
            case _:
                print("Invalid Choice")
    except ValueError :
        print("Invalid Input!!")        
                     
