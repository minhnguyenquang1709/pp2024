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
    stdscr.clear() # clear the screen
    curses.cbreak() # turn off input buffering
    stdscr.keypad(True) # enable keyboard

    # Initialize the list of students and the list of courses
    studentList = StudentList()
    courseList = CourseContainer()
    try:
        # Menu
        while(True):
            # stdscr.clear()
            stdscr.addstr("\nH==============================Student Management Program=============================H", curses.A_STANDOUT)
            stdscr.addstr("\nCurrent existing courses:")
            stdscr.addstr("\n0. Exit")
            stdscr.addstr("\n1. Input student(s) to the list")
            stdscr.addstr("\n2. Input course(s) to the list")
            stdscr.addstr("\n3. Select a course, add a student to the course or input mark or show student mark")
            stdscr.addstr("\n4. List students")
            stdscr.addstr("\n5. List courses")
            stdscr.addstr("\n6. Calculate GPA")
            stdscr.addstr("\n7. Sort student list by GPA")
            stdscr.addstr("\nH===========================================================H")		
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

            elif option == 3:
                stdscr.clear()
                course = courseList.chooseCourse(stdscr)
                if course != None:
                    while(True):
                        stdscr.addstr("\n1. Add a student")
                        stdscr.addstr("\n2. Input mark for a student")
                        stdscr.addstr("\n3. Add class(es) to the course")
                        stdscr.addstr("\n4. Show student marks")

                        stdscr.addstr("\nYour choice(0 to exit): ")
                        option2 = stdscr.getstr().decode('utf-8')
                        stdscr.addstr(option2)
                        # stdscr.refresh()
                        stdscr.addstr(option2)
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
                            stdscr.addstr("\nHow many classes to be added?(From G1 to Gn): n = ")
                            n = stdscr.getstr().decode('utf-8')
                            stdscr.addstr(n)
                            # stdscr.refresh()
                            if (not n.isnumeric()):
                                stdscr.addstr("\n\tInvalid number")
                                continue
                            if int(n) <= 0:
                                stdscr.addstr("\n\tInvalid number")
                                continue
                            course.addClass(int(n))
                            stdscr.refresh()
                        elif option2 == 4:
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