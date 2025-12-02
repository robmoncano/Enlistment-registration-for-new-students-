import random

List_of_Courses = {
    "BSA"       : [],
    "BSHM"      : [],
    "BSTM"      : [],
    "BSBA"      : ["Marketing","Financial Management"],
    "BSMA"      : [],
    "BEED"      : [],
    "BSED"      : ["Mathematics","Filipino","English"],
    "BCHED"     : [],
    "BSCRIM"    : [],
    "BSARCH"    : [],
    "BSCPE"     : [],
    "BSCE"      : [],
    "BSEE"      : [],
    "BSME"      : [],
    "BSN"       : [],
    "BSPHARMA"  : [],
    "BSMEDTECH" : [],
    "BSPSYCH"   : [],
    "BSIT"      : []
}

List_of_Instructors = {
    "BSA"       : ["blue","red"],
    "BSHM"      : ["white","yellow"],
    "BSTM"      : ["green","grey"],
    "BSBA"      : ["cyan","green"],
    "BSMA"      : ["brown","burgundy"],
    "BEED"      : ["orange","beige"],
    "BSED"      : ["maroon","indigo","magenta","beige","gold"],
    "BCHED"     : ["cyan","red","violet"],
    "BSCRIM"    : ["yellow","green"],
    "BSARCH"    : ["blue","magenta"],
    "BSCPE"     : ["maroon","indigo"],
    "BSCE"      : ["cyan","white"],
    "BSEE"      : ["black","burgundy"],
    "BSME"      : ["pink","gold"],
    "BSN"       : ["beige","grey"],
    "BSPHARMA"  : ["orange","brown"],
    "BSMEDTECH" : ["green","red"],
    "BSPSYCH"   : ["magenta","blue"],
    "BSIT"      : ["blue","green"]
}

Admin_Data = {
    "Acera"     : ["Gil"],
    "Casona"    : ["Mike"],
    "Moncano"   : ["Rob"],
    "Rosal"     : ["Jeremy"],
    "Masinger"  : ["Jhomadyane"]                      
}

Student_Accounts = {}

def process_courses(List_of_Courses, student_name):

    Input_Name = student_name

    while True:
        Input_Course = input("Course: ").upper()

        if Input_Course in List_of_Courses:
            Course_hasValue = List_of_Courses[Input_Course]

            if Course_hasValue:
                return process_major(Input_Name, Input_Course, Course_hasValue)
            else:
                return Input_Name, Input_Course
        else:
            print("\n>>>>> Course not found\n")

def process_major(Input_Name, Input_Course, Course_hasValue):
    while True:
        Input_Major = input("Select Major: ")

        for major in Course_hasValue:

            if Input_Major.lower() == major.lower():
                Chosen_Course = Input_Course + " Major in " + Input_Major
                return Input_Name, Chosen_Course

        print("\n>>>>> Major not Found\n")

def show_information(Input_Name, Chosen_Course, List_of_Instructors, Registered_Students, Course_Counts):
    Base_Course = Chosen_Course.split()[0]
    Chosen_Instructor = random.choice(List_of_Instructors.get(Base_Course))

    print("==========================================")
    print("\n        **Student Information**           \n")
    print("Name         :", Input_Name)
    print("Year Level   : First Year")
    print("Course       :", Chosen_Course)
    print("Instructor   :", Chosen_Instructor)
    print("\n==========================================\n")

    Submit_Entry = input("[Y] Submit | [Any Char] Delete or Cancel:\nEnter ===> : ").upper()

    if Submit_Entry == 'Y':
        if Chosen_Course not in Registered_Students:
            Registered_Students[Chosen_Course] = []

        Registered_Students[Chosen_Course].append({
            "Name": Input_Name,
            "Course": Chosen_Course,
            "Instructor": Chosen_Instructor,
            "Status": "Pending"
        })

        Course_Counts[Base_Course] = Course_Counts.get(Base_Course, 0) + 1

        print("\n---------------- Submitted Successfully ----------------\n")
    else:
        print("\n---------------- Entry Canceled ----------------\n")

    return Registered_Students, Course_Counts

def process_student_data(Registered_students, Approved_students):
    for Course, Students in Registered_students.items():
        for student in Students:
            name = student["Name"]
            course_info = student["Course"]
            instructor = student["Instructor"]
            status = student["Status"]

            print("==========================================")
            print("\n        **Approval Page** \n")
            print("Name         :", name)
            print("Course       :", course_info)
            print("Instructor   :", instructor)
            print("Status       :", status)
            print("\n==========================================\n")

            if status == "Pending":
                action = input("Approve student? [Y] Yes | [N] No | [Any Char] Skip:\nEnter ===> : ").upper()

                if action == 'Y':
                    student["Status"] = "Approved"
                    if Course not in Approved_students:
                        Approved_students[Course] = []

                    Approved_students[Course].append(student)
                    print("\n---------------- Approved ----------------\n")

                elif action == 'N':
                    student["Status"] = "Rejected"
                    print("\n---------------- Rejected ----------------\n")

                else:
                    print("Skipped\n")

    return Registered_students, Approved_students

def main_admin(Course_counts, Registered_students, Approved_students):
    print("==========================================")
    print("\n        **Students Registered ** \n")
    for Course, Count in Course_counts.items():
        print(Course, ":", Count, "Student(s)\n")
    print("==========================================\n")

    while True:
        Choice = input("View/Approve [1] | Logout [2]:\nEnter ===> : ").upper()

        if Choice == "1":
            if not Registered_students:
                print("\nNo registered students to approve.\n")
            else:
                Registered_students, Approved_students = process_student_data(Registered_students, Approved_students)

        elif Choice == "2":
            break

        else:
            print(">>>>> Invalid selection.")

    return Registered_students, Approved_students

def create_student_account(Student_Accounts):
    print("==========================================")
    print("\n        **Create Student Account** \n")
    Create_Student_user = input("Create Username: ")

    if Create_Student_user in Student_Accounts:
        print("\n>>>>> Username already Taken\n")
        return

    Create_Student_pass = input("Create Password: ")
    Full_name = input("Enter Name: ")

    Student_Accounts[Create_Student_user] = [Create_Student_pass, Full_name]
    print("\n---------------- Account Created Successfully ----------------\n")

def student_login(Student_Accounts, List_of_Courses, List_of_Instructors, Registered_Students, Course_Counts):
    print("==========================================")
    print("\n        **Student Login** \n")
    Student_username = input("Username: ")
    Student_password = input("Password: ")

    if Student_username not in Student_Accounts:
        print("\n>>>>> Account not found\n")
        return

    if Student_Accounts[Student_username][0] != Student_password:
        print("\n>>>>> Incorrect password\n")
        return

    Student_name = Student_Accounts[Student_username][1]
    print("\nWelcome,", Student_name, "\n")

    student_homepage(Student_name, List_of_Courses, List_of_Instructors, Registered_Students, Course_Counts)

def student_homepage(student_name, List_of_Courses, List_of_Instructors, Registered_Students, Course_Counts):
    while True:
        print("\n==========================================")
        print("\n        **Student Page** \n")
        Choice = input("Register    [1]\nView Status [2]\nLogout      [3]\nEnter ===> : ")

        if Choice == "1":
            Input_Name, Chosen_Course = process_courses(List_of_Courses, student_name)
            Registered_Students, Course_Counts = show_information(Input_Name, Chosen_Course, List_of_Instructors, Registered_Students, Course_Counts)

        elif Choice == "2":
            print("==========================================")
            print("\n        **Registration Status ** \n")
            found = False
            for course, students in Registered_Students.items():
                for s in students:
                    if s["Name"] == student_name:
                        print("Course:", s["Course"],"\nStatus:", s["Status"])
                        found = True
            if not found:
                print("\n>>>>> No registration found.\n")

        elif Choice == "3":
            print("\n---------------- Logged Out Successfully ----------------\n")
            break
        else:
            print("\n>>>>> Invalid Input.\n")

def main():
    Registered_Students = {}
    Approved_Students = {}
    Course_Counts = {}

    while True:
        print("\nStudent Enlistment System\n")
        main_Choice = input("Student Login  [1]\nCreate Account [2]\nAdmin Page     [3]\nExit           [4]\nEnter ===> : ")

        if main_Choice == '1':
            student_login(Student_Accounts, List_of_Courses, List_of_Instructors, Registered_Students, Course_Counts)

        elif main_Choice == '2':
            create_student_account(Student_Accounts)

        elif main_Choice == '3':
            Admin_username = input("Username: ")
            Admin_password = input("Password: ")

            if Admin_username in Admin_Data and Admin_Data[Admin_username][0] == Admin_password:
                Registered_Students, Approved_Students = main_admin(Course_Counts, Registered_Students, Approved_Students)
            else:
                print("\nUsername or Password not found.\n")

        elif main_Choice == '4':
            print ("\n---------------- Exit Successfully ----------------\n")
            break

        else:
            print(">>>>> Invalid Input\n")

if __name__ == "__main__":
