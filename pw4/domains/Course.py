class Course():
    def __init__(self, id, name, credit):
        self.__classID = 1
        self.__id = id
        self.__name = name
        self.__credit = credit
        self.__students={} # {studentID:[studentName, class, mark]}
        self.__classes = []

    def getCredit(self):
        return self.__credit

    def getMarks(self):
        return self.__marks

    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def addClass(self, n=1):
        for i in range(n):
            self.__classes.append(f"G{self.__classID}")
            self.__classID = self.__classID + 1

    def getClasses(self):
        return self.__classes
    
    def getStudents(self):
        return self.__students

    def info(self, stdscr):
        stdscr.addstr(f"\nThis is course {self.getID()} - {self.getName()} which has {len(self.getClasses())} classes and {len(self.getStudents())} students")
        if len(self.getStudents()) <= 0:
            return
        for sid, info in self.getStudents():
            stdscr.addstr(f"\n{sid} - {info[1]} - {info[0]}")
            stdscr.refresh()

    def displayClasses(self, stdscr):
        if len(self.getClasses()) <= 0:
            stdscr.addstr("\n\tThis course has no class!")
            stdscr.refresh()
        else:
            for i in self.getClasses():
                try:
                    stdscr.addstr(f"\n\tClass {i}")
                    stdscr.refresh()
                except curses.error:
                    stdscr.addstr("\n\tCannot display classes!")
        
    def displayMarks(self, stdscr):
        if len(self.getStudents()) <= 0:
            stdscr.addstr("\n\tThere is no student in this course!")
            return
        stdscr.addstr(f"\n\tCourse: {self.getName()}")
        for sid, info in self.getStudents().items():
            stdscr.addstr(f"\n{sid} - {info[0]}: {info[2]}")
            stdscr.refresh()