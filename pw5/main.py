from domains import *
from domains.Course import *
from domains.CourseContainer import *
from domains.Student import *
from domains.StudentList import *
from input import *
from output import *
import curses
from curses import wrapper

def main(stdscr):# curses put a screen on top of the terminal
    stdscr = curses.initscr()
    studentData, courseData, markData = loadData(decompress("students.dat", stdscr), stdscr)
    # for line in courseData:
    #     stdscr.addstr(f"{line[0]}-{line[1]}-{line[2]}")
    #     stdscr.refresh()
    # stdscr.getch()
    
    stdscr.clear() # clear the screen
    curses.cbreak() # turn off input buffering
    stdscr.keypad(True) # enable keyboard

    # Initialize the list of students and the list of courses
    studentList = StudentList()
    courseList = CourseContainer()

    # Load data
    for info in studentData:
        studentList.getList().update({info[0]:Student(info[0], info[1], info[2])})
        studentList.getList()[info[0]].setGPA(info[3])

    for info in courseData:
        courseList.getCourses().update({info[0]:Course(info[0], info[1], int(info[2]))})
        for markInfo in markData:
            if info[0] in markInfo:
                # Update the student list in Course
                courseList.getCourses()[info[0]].getStudents().update({markInfo[0]: [studentList.getList()[markInfo[0]].getName(), markInfo[2]]})

                # Update mark in Student
                studentList.getList()[markInfo[0]].enroll(stdscr, markInfo[1], info[1], info[2])
                studentList.getList()[markInfo[0]].getMarks()[markInfo[1]][1] = markInfo[2]

    try:
        # Menu
        while(True):
            # stdscr.clear()
            stdscr.addstr("\nH==================Student Management Program=================H", curses.A_STANDOUT)
            stdscr.addstr("\n0. Exit")
            stdscr.addstr("\n1. Input student(s) to the list")
            stdscr.addstr("\n2. Input course(s) to the list")
            stdscr.addstr("\n3. Select a course and do something")
            stdscr.addstr("\n4. List students")
            stdscr.addstr("\n5. List courses")
            stdscr.addstr("\n6. Calculate GPA")
            stdscr.addstr("\n7. Sort student list by GPA")
            stdscr.addstr("\nH=============================================================H")		
            stdscr.addstr("\nYour choice: ")
            option = stdscr.getstr().decode('utf-8')
            stdscr.addstr(option)
            # stdscr.refresh()

            if option.isnumeric():
                option = int(option)
            else:
                stdscr.addstr("\n\tInvalid input!")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                continue

            if option == 0:
                compress(studentList, courseList)
                stdscr.addstr("\n\tExiting...")
                stdscr.refresh()
                break
            elif option == 1:
                stdscr.clear()
                stdscr.addstr("\nHow many student? ")
                n = stdscr.getstr().decode('utf-8')
                stdscr.addstr(n)
                # stdscr.refresh()
                if n.isnumeric():
                    n = int(n)
                    while(n > 0):
                        addStudent(studentList, stdscr)
                        n=n-1
                        stdscr.clear()
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()

            elif option == 2:
                stdscr.clear()
                stdscr.addstr("\nHow many courses? ")
                n = stdscr.getstr().decode('utf-8')
                stdscr.addstr(n)
                # stdscr.refresh()
                if n.isnumeric():
                    n = int(n)
                    while(n > 0):
                        updateCourse(courseList, stdscr)
                        n=n-1
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()

            elif option == 3:
                stdscr.clear()
                course = courseList.chooseCourse(stdscr)
                if course != None:
                    while(True):
                        stdscr.addstr("\n-------------------------")
                        stdscr.addstr("\n1. Add a student")
                        stdscr.addstr("\n2. Input mark for a student")
                        stdscr.addstr("\n3. Show student marks")
                        stdscr.addstr("\n-------------------------")
                        stdscr.addstr("\nYour choice(0 to exit): ")
                        option2 = stdscr.getstr().decode('utf-8')
                        stdscr.addstr(option2)
                        stdscr.refresh()
                        
                        if not option2.isnumeric():
                            stdscr.addstr("\n\tInvalid number!")
                            stdscr.refresh()
                            stdscr.getch()
                            stdscr.clear()
                            continue
                        option2 = int(option2)
                        if option2 == 0:
                            stdscr.getch()
                            stdscr.clear()
                            break
                        elif option2 == 1:
                            stdscr.clear()
                            addStudentToCourse(course, stdscr, studentList.getList())
                            stdscr.refresh()
                        elif option2 == 2:
                            stdscr.clear()
                            addMark(course, stdscr, studentList.getList())
                            stdscr.refresh()
                        elif option2 == 3:
                            stdscr.clear()
                            course.displayMarks(stdscr)
                            stdscr.refresh()
                        else:
                            stdscr.clear()
                            stdscr.addstr("\n\tInvalid number!")
                            stdscr.refresh()
                            continue

            elif option == 4:
                stdscr.clear()
                displayStudents(studentList, stdscr)
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
            elif option == 5:
                stdscr.clear()
                displayCourses(courseList, stdscr)
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
            elif option == 6:
                stdscr.clear()
                calGPA(studentList, stdscr)
                stdscr.refresh()
                stdscr.getch()

            elif option == 7:
                stdscr.clear()
                sortByGPA(studentList, stdscr)
            else:
                stdscr.addstr("\n\tInvalid number!")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                continue
            

    except curses.error:
        stdscr.addstr("\n\tCurses error!")
        

    stdscr.refresh()
    curses.nocbreak()
    stdscr.keypad(False)

    curses.endwin()


if __name__ == "__main__":
    wrapper(main)