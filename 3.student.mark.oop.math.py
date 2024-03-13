import math
import numpy as np

def confirm():
    choice = input("Your choice?(yes/no): ")
    if choice.lower() == 'y' or choice.lower() == 'yes':
        return True
    if choice.lower() == 'n' or choice.lower() == 'no':
        return False
    print("Invalid input")
    confirm()

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
        if 1 <= day <= 31 and 1 <= month <= 12:
            return True

    # If any condition fails, return False
    return False

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

    def setDOB(self, dob):
        if checkDOB(dob):
            self.__dob = dob
            return True
        else:
            print("\n\tInvalid date format!")
            return False

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.__id = id
        self.__gpa = 0
        self.__marks = {} # {courseID:[courseName, className, mark, credit]}

    def getGPA(self):
        return self.__gpa

    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id

    def getMarks(self):
        return self.__marks
    
    def setMark(self, courseID, mark = 0):
        if courseID not in self.getMarks():
            print("\n\tThe student has not enrolled the given course")
            return
        self.__marks[courseID][2] = mark

    def enroll(self, courseID, courseName, className, credit):
        if courseID in self.getMarks():
            print("\n\tThis student already enrolled in the given course!")
            return
        self.__marks.update({courseID:[courseName, className, 0, credit]})

    def displayMarks(self):
        if len(self.getMarks()) > 0:
            for courseID, mark in self.getMarks():
                print(f"{courseID} - {mark[0]}: {mark[2]}")
        else:
            print("\n\tThis student has no mark!")

    def info(self):
        print("----------------------------------------------------------")
        print(f"\tStudent: {self.getID()} - {self.getName()}")
        print(f"\tDate of birth: {self.getDOB()}")
        self.displayMarks()

    def GPA(self):
        if len(self.getMarks()) <= 0:
            return 0.0
        marks = np.array([])
        credits = np.array([])
        for info in self.getMarks().values():
            marks = np.append(marks, info[2])
            credits = np.append(credits, info[3])
        gpa = np.multiply(marks, credits)
        gpa = np.sum(gpa)
        divisor = np.sum(credits)
        gpa = 1.0*gpa/divisor
        self.__gpa = gpa
        return gpa


class StudentList:
    def __init__(self):
        self.__students = {} # {studentID: studentObj}
        
    def getList(self):
        return self.__students
    
    def makeStudent(self):
        id = input("Enter student ID: ")
        name = input("Enter student's name: ")
        dob = input("Enter student's date of birth (dd-mm-yyyy): ")
        if checkDOB(dob):
            student = Student(id, name, dob)
            return student
        else:
            print("\n\tFailed to make Student object!")
            return None

    def addStudent(self):
        student = self.makeStudent()
        if student != None:
            studentList = self.__students
            if student.getID() in studentList:
                print("Student already exists. Updating info...")
                studentList.update({f"{student.getID()}":student})
                print("\n\tDone!")
            else:
                print("Adding the new student to the list...")
                studentList.update({f"{student.getID()}":student})
                print("\n\tDone!")

    def info(self):
        if len(self.getList()) == 0:
            print("\n\tThere is no student in the list!")
            return
        for sid, student in self.getList().items():
            print(f"\n{sid} - {student.getName()} - {student.getDOB()}")
            for cid, info in student.getMarks().items():
                print(f"{cid} - {info[0]} - Class: {info[1]} - Mark: {info[2]}")

    def calGPA(self):
        studentList = self.getList().items()
        for sid, student in studentList:
            print(f"\n{sid} - {student.getName()}: {student.GPA()}")

    def sort(self):
        if len(self.getList()) <= 0:
            print("\n\tThere is no student!")
            return
        list1 = np.array(list(self.getList().values()))
        # print(list1)
        # Specify data types to sort more easily
        dtype = [('student', Student), ('gpa', float)]
        list2 = np.array([], dtype=dtype)
        for  student in list1:
            list2 = np.append(list2, np.array((student, student.getGPA()), dtype=dtype))
        # print(list2)
        np.sort(list2, order='gpa')
        list2 = list2[::-1]

        for student in list2:
            print(f"{student[0].getID()} - {student[0].getName()}: {student[0].getGPA()}")


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

    def info(self):
        print(f"\nThis is course {self.getID()} - {self.getName()} which has {len(self.getClasses())} classes and {len(self.getStudents())} students")
        if len(self.getStudents()) <= 0:
            return
        for sid, info in self.getStudents():
            print(f"\n{sid} - {info[1]} - {info[0]}")

    def displayClasses(self):
        if len(self.getClasses()) <= 0:
            print("\n\tThis course has no class!")
        else:
            for i in self.getClasses():
                print(f"\n\tClass {i}")
        
    def displayMarks(self):
        if len(self.getStudents()) <= 0:
            print("\n\tThere is no student in this course!")
            return
        print(f"\n\tCourse: {self.getName()}")
        for sid, info in self.getStudents().items():
            print(f"\n{sid} - {info[0]}: {info[2]}")
                
    def addMark(self, studentList):
        sid = input("Which student to add mark to? ")
        if sid not in self.getStudents().keys():
            print("\n\tThe student does not exist in this course")
            return
        mark = input("Enter the mark: ")
        temp = mark.replace(".", '')
        if temp.isnumeric() == False or float(mark) < 0 or float(mark) > 22:
            print("\n\tInvalid mark!")
            return
        mark = float(mark) * 10
        mark = np.floor(mark)
        mark = mark/10.0
        self.__students[sid][2] = mark
        studentList[sid].setMark(self.getID(), mark)

    def addStudent(self, studentList):
        sid = input("Enter student ID: ")
        if sid not in studentList:
            print("\n\tThe student does not exist in the list!")
            return
        if sid in self.getStudents():
            print("\n\tThe student is already in this course!")
            return
        self.displayClasses()
        if len(self.__classes) <=0:
            return
        className = input("Enter the name of the class to add the student: ")
        if className not in self.getClasses():
            print("\n\tThe class does not exist!")
            return
        student = studentList[sid].enroll(self.getID(), self.getName(), className, self.getCredit())
        self.__students.update({sid:[studentList[sid].getName(), className, 0]})

            
class CourseContainer:
    def __init__(self):
        ads = Course("ICT2.001", "Algorithm and Data Structure", 3)
        algeStruc = Course("MATH2.002", "Algebraic Structures", 3)
        cal1 = Course("MATH1.001", "Calculus I", 4)
        oop = Course("ICT2.002", "Object-oriented Programming", 4)
        self.__courses = {ads.getID():ads,
             algeStruc.getID():algeStruc,
             cal1.getID():cal1,
             oop.getID():oop}

    def getCourses(self):
        return self.__courses
    
    def makeCourse(self):
        courseID = input("Enter the course's ID: ")
        courseName = input("Enter the course's name: ")
        credit = input("Enter the number of credits for the course: ")
        if not credit.isnumeric():
            print("\n\tInvalid number of credits!")
            return None
        if courseID in self.getCourses():
            print("This course already exists, do you want to update it?(old data will be removed)")
            choice = confirm()
            if choice:
                return Course(courseID, courseName, credit)
            else:
                return None
        return Course(courseID, courseName, credit)

    def updateCourse(self):
        c = self.makeCourse()
        if c != None:
            self.__courses.update({c.getID():c})
        else:
            print("\n\tThere is no course to add!")

    def info(self):
        if len(self.getCourses()) <= 0:
            print("\n\tThere is no course!")
            return
        for course in self.getCourses().values():
            print(f"\n{course.getID()} - {course.getName()}")

    def __str__(self):
        return str(self.getCourses())
    
    def chooseCourse(self):
        cid = input("Enter course ID: ")
        if cid not in self.getCourses():
            print("\n\tThe course does not exist!")
            return None
        return self.getCourses()[cid]


def main():
    studentList = StudentList()
    courseList = CourseContainer()
    for course in courseList.getCourses().values():
        print(f"{course.getID()} - {course.getName()}")

    # Menu
    while(True):
        print("\nH===========================================================H")
        print("Current existing courses:")
        print("""
            0. Exit
            1. Input student(s) to the list
            2. Input course(s) to the list
            3. Select a course, add a student to the course or input mark or show student mark
            4. List students
            5. List courses
            6. Calculate GPA
            7. Sort student list by GPA""")
        print("\nH===========================================================H")		
        option = input("Your choice: ")

        if option.isnumeric():
            option = int(option)
        else:
            print("\n\tInvalid input!")
            continue

        if option == 0:
            print("\n\tExiting...")
            break
        elif option == 1:
            n = input("How many students? ")
            if n.isnumeric():
                n = int(n)
                while(n > 0):
                    studentList.addStudent()
                    n=n-1

        elif option == 2:
            n = input("How many courses? ")
            if n.isnumeric():
                n = int(n)
                while(n > 0):
                    courseList.updateCourse()
                    n=n-1

        elif option == 3:
            course = courseList.chooseCourse()
            if course != None:
                while(True):
                    print("""
        1. Add a student
        2. Input mark for a student
        3. Add class(es) to the course
        4. Show student marks""")
                    option2 = input("Your option(0 to exit): ")
                    if not option2.isnumeric():
                        print("\n\tInvalid number!")
                        continue
                    option2 = int(option2)
                    if option2 == 0:
                        break
                    elif option2 == 1:
                        course.addStudent(studentList.getList())
                    elif option2 == 2:
                        course.addMark(studentList.getList())
                    elif option2 == 3:
                        n = input("How many classes to be added?(From G1 to Gn): n = ")
                        if (not n.isnumeric()):
                            print("\n\tInvalid number")
                            continue
                        if int(n) <= 0:
                            print("\n\tInvalid number")
                            continue
                        course.addClass(int(n))
                    elif option2 == 4:
                        course.displayMarks()
                    else:
                        print("\n\tInvalid number!")
                        continue

        elif option == 4:
            studentList.info()
        elif option == 5:
            courseList.info()
        elif option == 6:
            studentList.calGPA()

        elif option == 7:
            studentList.sort()
        else:
            print("\n\tInvalid number!")
            continue

if __name__ == "__main__":
    main()