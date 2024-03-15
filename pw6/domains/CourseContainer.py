import curses
from .Course import *
from input import *

class CourseContainer:
    def __init__(self):
        ads = Course("ICT2.001", "Algorithm and Data Structure", 3)
        algeStruc = Course("MATH2.002", "Algebraic Structures", 3)
        cal1 = Course("MATH1.001", "Calculus I", 4)
        oop = Course("ICT2.002", "Object-oriented Programming", 4)
        self.__courses = {}

    def getCourses(self):
        return self.__courses
    
    def makeCourse(self, stdscr):
        stdscr.addstr("\nEnter the course's ID: ")
        courseID = stdscr.getstr().decode('utf-8')
        stdscr.addstr(courseID)
        # stdscr.refresh()
        stdscr.addstr("\nEnter the course's name: ")
        courseName = stdscr.getstr().decode('utf-8')
        stdscr.addstr(courseName)
        # stdscr.refresh()
        stdscr.addstr("\nEnter the number of credits for the course: ")
        credit = stdscr.getstr().decode('utf-8')
        stdscr.addstr(credit)
        # stdscr.refresh()
        if not credit.isnumeric():
            stdscr.addstr("\n\tInvalid number of credits!")
            return None
        if courseID in self.getCourses():
            stdscr.addstr("\nThis course already exists, do you want to update it?(old data will be removed)")
            choice = confirm(stdscr)
            if choice:
                return Course(courseID, courseName, credit)
            else:
                return None
        return Course(courseID, courseName, credit)

    def __str__(self):
        return str(self.getCourses())
    
    def chooseCourse(self, stdscr):
        stdscr.addstr("\nEnter course ID: ")
        cid = stdscr.getstr().decode('utf-8')
        if cid not in self.getCourses():
            stdscr.addstr("\n\tThe course does not exist!")
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()
            return None
        return self.getCourses()[cid]