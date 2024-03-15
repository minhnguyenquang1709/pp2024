import curses
import numpy as np
from domains.Course import *
from domains.Student import *
from domains.StudentList import *
from domains.CourseContainer import *

def displayCourses(courseList, stdscr):
        if len(courseList.getCourses()) <= 0:
            stdscr.addstr("\n\tThere is no course!")
            return
        for course in courseList.getCourses().values():
            stdscr.addstr(f"\n{course.getID()} - {course.getName()}")

def displayStudents(studentList, stdscr):
        if len(studentList.getList()) == 0:
            stdscr.addstr("\n\tThere is no student in the list!")
            return
        for sid, student in studentList.getList().items():
            stdscr.addstr(f"\n{sid} - {student.getName()} - {student.getDOB()}")
            for cid, info in student.getMarks().items():
                stdscr.addstr(f"\n{cid} - {info[0]} - Class: {info[1]} - Mark: {info[2]}")

def calGPA(studentList, stdscr):
        studentListX = studentList.getList().items()
        if len(studentListX) <= 0:
            stdscr.addstr("\n\tThere is no student!")
            stdscr.refresh()
            stdscr.getch()
        for sid, student in studentListX:
            stdscr.addstr(f"\n{sid} - {student.getName()}: {student.GPA()}")
            stdscr.refresh()
            x, y = stdscr.getyx()
            if y == (curses.LINES - 1):
                stdscr.getch()
                stdscr.clear()
            else:
                stdscr.getch()

def sortByGPA(studentList, stdscr):
        if len(studentList.getList()) <= 0:
            stdscr.addstr("\n\tThere is no student!")
            stdscr.refresh()
            stdscr.getch()
            return
        list1 = np.array(list(studentList.getList().values()))
        # stdscr.addstr(list1)
        # Specify data types to sort more easily
        dtype = [('student', Student), ('gpa', float)]
        list2 = np.array([], dtype=dtype)
        for  student in list1:
            list2 = np.append(list2, np.array((student, student.getGPA()), dtype=dtype))
        
        # np.sort(list2, order='gpa')
        sortedList = sorted(list2, key=lambda student: student[1], reverse=True)

        for student in sortedList:
            stdscr.addstr(f"\n{student[0].getID()} - {student[0].getName()}: {student[1]}")
            stdscr.refresh()
            x, y = stdscr.getyx()
            if y == (curses.LINES - 1):
                stdscr.getch()
                stdscr.clear()
            else:
                stdscr.getch()