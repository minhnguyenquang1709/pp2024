# Ask the user to input a number of unit (course / student)
def inputSomething(args):
    return input(f"Enter the number of {args} in this class: ")

# Ask the user to enter a list of info for an type
def inputInfo(args):
    item = {
        f"{args[0]}":{
            "name":args[1],
            "dob":args[2]
        }
    }

    # TODO: input info for the type (student/course info)

    return item

# Enter info for a course
def inputCourse(args):
    item = {
        f"{args[0]}":args[1]
    }
    return item

# Input the student mark in a course base on the course id
def inputMark(students, courses):
    sid = input("Enter the student id to add mark: ")
    cid = input("Enter the course id to add mark: ")
    if cid not in courses or sid not in students:
        print("The course or student does not exist!")
        return
    else:
        mark = input("Enter the mark: ")
        temp = mark
        if temp.replace(".", "").isnumeric():
            item = {
                f"{courses[cid]}":mark
            }
            students[sid]['marks'].update(item)
        else:
            print("""
            Invalid mark""")
            
def displayMarks(students, courses):
    cid = input("Enter the course id to add mark: ")
    
    for s in students.keys():
        if "marks" in students[s].keys() and len(students[s]['marks']) > 0:
            if courses[cid] in students[s]['marks']:
                print(f"{students[s]['name']}: {students[s]['marks'][courses[cid]]}")
                #for subject in students[s][m]:
                 #   print(f"Marks (m} - {students[s]['marks'][m].values()}): ", end="")
            else:
                print(f"{students[s]['name']} has no mark")
            print("-------------------------------------------------")


# Display a list of students
def listStudents(students):

    # TODO: check what happens if there's no student (hint: len(students))
    if len(students) == 0:
        print("There aren't any students yet")
        return

    # TODO: display the student list
    print("Here is the student list: ")
    print("-------------------------------------------------")

    # TODO: add loop function to check the info of student
    for s in students.keys():
        print(f"{s} - {students[s]['name']} - {students[s]['dob']}")

    # TODO: check if mark student and print out the information
    
        if "marks" in students[s].keys() and len(students[s]['marks']) > 0:
            for m in students[s]['marks'].keys():
                print(f"{m}: {students[s]['marks'][m]}")#, end="")
                #for subject in students[s][m]:
                 #   print(f"Marks (m} - {students[s]['marks'][m].values()}): ", end="")
        else:
            print(f"{students[s]['name']} has no mark")
        print("-------------------------------------------------")

# Display a list of courses
def listCourses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
        
    print("Here is the course list: ")
    # TODO: add loop function to check the info of course
    for key, value in courses.items():
        print(f"{key} - {value}")

# Main function for the "game"
def main():
    cNum = 0
    stuNum = 0
    # Initialize the list for DATA option
    courses = {
        "ICT2.001":"ADS",
        "MAT1.001":"Calculus I"
    }
    students = {
        "22BI13482":{
            "name":"Tran Anh Vu dep trai",
            "dob":"04-09-2004",
            "marks":{
                "Calculus I":19.9,
                "ads":20
            }
        },
        "22BI13301":{
            "name":"Nguyen Quang Minh",
            "dob":"17-09-2004",
            "marks":{
                "Calculus I":10,
                "ads":13,
                "fdb":11.2
            }
        },
        "22BI13444":{
            "name":"No Mark Student",
            "dob":"17-09-2004"
        },
        "22BI13449":{
            "name":" Second No Mark Student",
            "dob":"17-09-2004",
            "marks":{}
        }
    }

    while(True):
        print("""
=========================================================================
    0. Exit
    1. Input number of students in a class
    2. Input student information: id, name, DoB
    3. Input number of courses
    4. Input course information: id, name
    5. Select a course, input marks for student in this course
    6. List courses
    7. List students and their marks
    8. Show student marks for a course
    """)
        option = input("Your choice: ")
        #print("option is ",type(option)," option.isnumber = ", option.isnumeric())
        if option.isnumeric()==False:
            option = 9
        else:
            option = int(option)
            
        # Choose option from 0 -> n
        if option == 0:
            break

        elif option == 1:                                                                            # Option 1
            stuNum = inputSomething('students')
            if stuNum.isnumeric()==False:
                print("""
                Invalid number of students""")
                continue
            else: 
                stuNum = int(stuNum)
                if stuNum < 1:     
                    print("""
                    Invalid number of students""")
                    continue    

        elif option == 2:   
            if stuNum is 0:
                print("You have not enter a valid number of students to be added!")
            while stuNum > 0:
                print("""
------------------------------------------------------------
                          """)
                id = input("Enter the id: ") 
                name = input("Enter the name: ")      
                dob = input("Enter the date of birth(dd-mm-yyyy): ")                                                                   # Option 2                                                     
                students.update(inputInfo([id, name, dob]))
                stuNum=stuNum-1 

        elif option == 3:
            cNum = inputSomething('courses')
            if cNum.isnumeric() == False:
                print("""
                Invalid number of courses!""")
                continue
            else:
                cNum = int(cNum)
                if cNum < 1:
                    print("""
                    Invalid number of courses!""")
                    continue

        elif option == 4:
            if cNum is 0:
                print("You have not enter a valid number of courses to be added!")
                continue
            while cNum > 0:
                id = input("Enter course id: ") 
                name = input("Enter course name: ")
                courses.update(inputCourse([id, name]))
                cNum=cNum-1

        elif option == 5:
            inputMark(students, courses)
            continue

        elif option == 6:
            listCourses(courses)

        elif option == 7:
            listStudents(students)

        elif option == 8:
            displayMarks(students,courses)
            
        else:
            print("""
            Your input is invalid""")

# Call the main function
if __name__ == "__main__":
    main()