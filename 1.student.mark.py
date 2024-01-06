# Ask the user to input a number of unit (course / student)
def input_something(args):
    return int(input(f"Enter the number of {args} in this class: "))

# Ask the user to enter a list of info for an type
def input_infos(args):
    item = {
        f"{args[0]}":{
            "name":args[1],
            "dob":args[2]
        }
    }

    # TODO: input info for the type (student/course info)

    return item

# Input the student mark in a course base on the course id
def input_mark(id, students):
    if id in students:
        students[id]["marks"] = {}
    # TODO: check mark in student or not
    # If not, enter the mark for the course


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
    
        if "marks" in students[s].keys():
            for m in students[s]['marks'].keys():
                print(f"{m}: {students[s]['marks'][m]}")#, end="")
                #for subject in students[s][m]:
                 #   print(f"Marks (m} - {students[s]['marks'][m].values()}): ", end="")
        else:
            print(f"{students[s]['name']} has no mark")
        print("-------------------------------------------------")

# Display a list of courses
def list_courses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
        
    print("Here is the course list: ")
    # TODO: add loop function to check the info of course
    for c in courses:
        print(f"{c+1}. {c['id']} - {c['name']}")

# Main function for the "game"
def main():
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
                "calculus":19.9,
                "ads":20
            }
        },
        "22BI13301":{
            "name":"Nguyen Quang Minh",
            "dob":"17-09-2004",
            "marks":{
                "calculus":10,
                "ads":13,
                "fdb":11.2
            }
        },
        "22BI13444":{
            "name":"No Mark Student",
            "dob":"17-09-2004"
        }
    }
    num_students = 0
    num_courses = 0

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
            input_something(students)
        elif option == 2:    
            id = input("Enter the id: ") 
            name = input("Enter the name: ")      
            dob = input("Enter the date of birth(dd-mm-yyyy): ")                                                                   # Option 2                                                     
            students.update(input_infos(id, name, dob))
        elif option == 3:
            input_infos(courses)
        elif option == 4:
            input_infos(courses)
        elif option == 5:
            input_infos(courses)
        elif option == 6:
            input_infos(courses)
        elif option == 7:
            listStudents(students)
        elif option == 8:
            input_infos(courses)
            
        else:
            print("Your input is invalid. Please try again!")

# Call the main function
if __name__ == "__main__":
    main()
