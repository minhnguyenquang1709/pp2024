from input import *
import numpy as np
import curses
import math

class Person:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getDOB(self):
        return self.__dob

    def setDOB(self, stdscr, dob):
        if checkDOB(dob):
            self.__dob = dob
            return True
        else:
            stdscr.addstr("\n\tInvalid date format!")
            stdscr.refresh()
            return False

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.__id = id
        self.__gpa = 0.0
        self.__marks = {} # {courseID:[courseName, mark, credit]}

    def getGPA(self):
        return self.__gpa
    def setGPA(self, gpa):
        self.__gpa = gpa

    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id

    def getMarks(self):
        return self.__marks
    
    def setMark(self, stdscr, courseID, mark = 0):
        if courseID not in self.getMarks():
            stdscr.addstr("\n\tThe student has not enrolled the given course")
            stdscr.refresh()
            return
        self.__marks[courseID][1] = mark

    def enroll(self, stdscr, courseID, courseName, credit):
        if courseID in self.getMarks():
            stdscr.addstr("\n\tThis student already enrolled in the given course!")
            stdscr.refresh()
            stdscr.getch()
            return
        self.__marks.update({courseID:[courseName, 0, credit]})

    def displayMarks(self, stdscr):
        if len(self.getMarks()) > 0:
            for courseID, mark in self.getMarks():
                stdscr.addstr(f"\n{courseID} - {mark[0]}: {mark[1]}")
        else:
            stdscr.addstr("\n\tThis student has no mark!")
            stdscr.refresh()

    def info(self, stdscr):
        stdscr.addstr("----------------------------------------------------------")
        stdscr.addstr(f"\tStudent: {self.getID()} - {self.getName()}")
        stdscr.addstr(f"\tDate of birth: {self.getDOB()}")
        self.displayMarks(stdscr)

    def GPA(self):
        if len(self.getMarks()) <= 0:
            return 0.0
        marks = np.array([])
        credits = np.array([])
        for info in self.getMarks().values():
            marks = np.append(marks, info[1])
            credits = np.append(credits, info[2])
        gpa = np.multiply(marks, credits)
        gpa = np.sum(gpa)
        divisor = np.sum(credits)
        gpa = 1.0*gpa/divisor
        gpa = math.floor(gpa*10)
        gpa = float(gpa/10)
        self.__gpa = gpa
        return gpa