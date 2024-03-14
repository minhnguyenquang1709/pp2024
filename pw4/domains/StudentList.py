from input import *
from .Student import *

class StudentList:
    def __init__(self):
        self.__students = {} # {studentID: studentObj}
        
    def getList(self):
        return self.__students
    
    def makeStudent(self, stdscr):
        stdscr.addstr("\nEnter student ID: ")
        id = stdscr.getstr().decode('utf-8')
        stdscr.addstr(f"{id}")
        # stdscr.refresh()
        stdscr.addstr("\nEnter student's name: ")
        name = stdscr.getstr().decode('utf-8')
        stdscr.addstr(name)
        # stdscr.refresh()
        stdscr.addstr("\nEnter student's date of birth (dd-mm-yyyy): ")
        dob = stdscr.getstr().decode('utf-8')
        stdscr.addstr(dob)
        # stdscr.refresh()
        if checkDOB(dob):
            student = Student(id, name, dob)
            return student
        else:
            stdscr.addstr("\n\tFailed to make Student object!")
            stdscr.refresh()
            stdscr.getch()
            return None