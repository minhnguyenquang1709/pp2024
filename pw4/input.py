import curses
import math

def confirm(stdscr):
    stdscr.addstr("Your choice?(yes/no): ")
    choice = stdscr.getstr().decode('utf-8')
    stdscr.addstr(choice)
    # stdscr.refresh()
    if choice.lower() == 'y' or choice.lower() == 'yes':
        return True
    if choice.lower() == 'n' or choice.lower() == 'no':
        return False
    stdscr.addstr("\n\tInvalid input")
    stdscr.refresh()
    confirm(stdscr)

def checkDOB(input_date):
    # Check if the input has the correct format (dd-mm-yyyy)
    if len(input_date) == 10 and input_date[2] == input_date[5] == '-':
        for i in range(len(input_date)):
            if i == 2 or i==5:
                continue
            if input_date[i].isnumeric():
                continue
            else:
                return False
        day, month, year = map(int, input_date.split('-'))

        # Check if day, month, and year values are within valid ranges
        if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024:
            return True

    # If any condition fails, return False
    return False

def addStudent(studentList, stdscr):
        student = studentList.makeStudent(stdscr)
        if student != None:
            studentList = studentList.getList()
            if student.getID() in studentList:
                stdscr.addstr("\nStudent already exists. Updating info...")
                studentList.update({f"{student.getID()}":student})
                stdscr.addstr("\n\tDone!")
                stdscr.refresh()
                stdscr.getch()
            else:
                stdscr.addstr("\nAdding the new student to the list...")
                studentList.update({f"{student.getID()}":student})
                stdscr.addstr("\n\tDone!")
                stdscr.refresh()
                stdscr.getch()

def updateCourse(courseList, stdscr):
    c = courseList.makeCourse(stdscr)
    if c != None:
        courseList.getCourses().update({c.getID():c})
    else:
        stdscr.addstr("\n\tThere is no course to add!")

def addStudentToCourse(course, stdscr, studentList):
        stdscr.addstr("\nEnter student ID: ")
        sid = stdscr.getstr().decode('utf-8')
        stdscr.addstr(sid)
        # stdscr.refresh()
        if sid not in studentList:
            stdscr.addstr("\n\tThe student does not exist in the list!")
            # stdscr.refresh()
            return
        if sid in course.getStudents():
            stdscr.addstr("\n\tThe student is already in this course!")
            # stdscr.refresh()
            return
        course.displayClasses(stdscr)
        if len(course.getClasses()) <=0:
            return
        stdscr.addstr("\nEnter the name of the class to add the student: ")
        className = stdscr.getstr().decode('utf-8')
        stdscr.addstr(className)
        # stdscr.refresh()
        if className not in course.getClasses():
            stdscr.addstr("\n\tThe class does not exist!")
            # stdscr.refresh()
            return
        student = studentList[sid].enroll(stdscr, course.getID(), course.getName(), className, course.getCredit())
        course.getStudents().update({sid:[studentList[sid].getName(), className, 0]})

def addMark(course, stdscr, studentList):
        try:
            stdscr.addstr("\nWhich student to add mark to? ")
            sid = stdscr.getstr().decode('utf-8')
            stdscr.addstr(sid)
            # stdscr.refresh()
            if sid not in course.getStudents().keys():
                stdscr.addstr("\n\tThe student does not exist in this course")
                return
            stdscr.addstr("\nEnter the mark: ")
            mark = stdscr.getstr().decode('utf-8')
            stdscr.addstr(mark)
            # stdscr.refresh()
            temp = mark.replace(".", '')
            if temp.isnumeric() == False or float(mark) < 0 or float(mark) > 22:
                stdscr.addstr("\n\tInvalid mark!")
                # stdscr.refresh()
                return
            mark = float(mark) * 10
            mark = math.floor(mark)
            mark = mark/10.0
            course.getStudents()[sid][2] = mark
            studentList[sid].setMark(stdscr, course.getID(), mark)
        except curses.error:
            stdscr.addstr("\n\tFailed to add mark!")
            stdscr.refresh()
            stdscr.getch()