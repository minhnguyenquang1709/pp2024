import curses

class Course():
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit
        self.__students={} # {studentID:[studentName, mark]}

    def getCredit(self):
        return self.__credit

    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getStudents(self):
        return self.__students

    def info(self, stdscr):
        stdscr.addstr(f"\nThis is course {self.getID()} - {self.getName()} which has {len(self.getStudents())} students")
        if len(self.getStudents()) <= 0:
            return
        for sid, info in self.getStudents():
            stdscr.addstr(f"\n{sid} - {info[1]} - {info[0]}")
            stdscr.refresh()
        
    def displayMarks(self, stdscr):
        if len(self.getStudents()) <= 0:
            stdscr.addstr("\n\tThere is no student in this course!")
            return
        stdscr.addstr(f"\n\tCourse: {self.getName()}")
        for sid, info in self.getStudents().items():
            stdscr.addstr(f"\n{sid} - {info[0]}: {info[1]}")
            stdscr.refresh()