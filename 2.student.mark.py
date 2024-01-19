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
        day, month, year = map(int, input_date.split('-'))
        
        # Check if day, month, and year values are within valid ranges
        if 1 <= day <= 31 and 1 <= month <= 12:
            return True

    # If any condition fails, return False
    return False

def addCourse(courses):
	id = input("Enter ID of course: ")
	name = input("Enter the name of course: ")
	newCourse = Course(id, name)
	courses.update({id:newCourse})


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

	def getID(self):
		return self.__id
	def setID(self, id):
		self.__id = id

	def info(self):
		print("----------------------------------------------------------")
		print(f"Student: {self.getID} - {self.getName}")
		print(f"Date of birth: {self.getDOB}")
		self.displayMarks()
		
	

class CourseClass:
	def __init__(self, name):
		self.__name = name
		self.__students = {}

	def getName(self):
		return self.__name
	
	def setName(self, name):
		self.__name = name
		
	def getStudents(self):
		return self.__students

	def info(self):
		print(f"\nThis is class {self.getName()} which has {len(self.getStudents())} students")
		self.display()
		
	def display(self):
		if len(self.getStudents()) == 0:
			print("There is no student in this class!")
		for student, attribute in self.getStudents().items():
			print("----------------------------------------------------------------")
			print(f"Student: {student} - {attribute.getName()}")
			print(f"\tDate of birth: {attribute.getDOB()}")
			
	def makeStudent(self):
		id = input("Enter student's id: ")
		if id in self.getStudents():
			print(f"The student {id} already exists, do you want to override? (yes/no): ")
			if confirm():
				name = input("Enter student's name: ")
				dob = input("Enter student's date of birth (dd-mm-yyyy): ")
				student = Student(id, name, dob)
				student.setID(id)
				student.setName(name)
				if student.setDOB(dob):
					return student
				else:
					return None
			else:
				return None
		else:
			name = input("Enter student's name: ")
			dob = input("Enter student's date of birth (dd-mm-yyyy): ")
			student = Student(id, name, dob)
			student.setID(id)
			student.setName(name)
			if student.setDOB(dob):
				return student
			else:
				return None

	def addStudent(self):
		student = self.makeStudent()
		if student != None:
			self.getStudents().update({f"{student.getID()}":student})
		else:
			print("There is no student to add")

#	def addStudent(self, student):
#		if student != None:
#			self.__students.update({f"{student.getID()}":student})
#		else:
#			print("There is no student to add")
			
	def addManyStudent(self):
		numb = input("Enter the number of students to add to class: ")
		if numb.isnumeric():
			numb = int(numb)
			while numb>0:
				self.addStudent()
				numb=numb-1
		else:
			print("\n\tInvalid input!")

	def removeStudent(self):
		id = input("Enter the ID of the student to be removed: ")
		if id in self.getStudents():
			self.getStudents().pop(id)
		else:
			print("\n\tThe student does not exist!")
	

class Course():
	def __init__(self, id, name):
		self.__id = id
		self.__name = name
		self.__classes=[]
		self.__marks = {}

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

	def getClasses(self):
		return self.__classes

	def info(self):
		print(f"\nThis is course {self.getID()} - {self.getName()} which has {len(self.getClasses())} classes")
		self.display()

	def display(self):
		if len(self.getClasses()) == 0:
			print("\n\tThis course has no class!")
		else:
			for i in self.getClasses():
				print("==========================================================")
				i.info()

	def makeClass(self):
		name = input("Enter name of class: ")
		if name in self.getClasses():
			return None
		else:
			return CourseClass(name)

	def addClass(self):
		print("Add a new class")
		choice = confirm()
		if choice:
			newClass = self.makeClass()
			if newClass != None:
				self.getClasses().append(newClass)
			else:
				print("\n\tThe class already exists!")

	def removeClass(self):
		name = input("Which class to be removed?: ")
		for clas in self.getClasses():
			if name == clas.getName():
				self.getClasses().remove(clas)
		
	def displayMarks(self):
		if len(self.getMarks()) == 0:
			print("This course has no mark")
		else:
			for stuName, mark in self.getMarks().items():
				print(f"\t{stuName}: {mark}")

	def checkStudentInCourse(self, sid):
		for clas in self.getClasses():
			if sid in clas.getStudents():
				return sid
		return None

	def addMark(self):
		print(f"Add mark for student")
		sid = self.checkStudentInCourse(input("Enter student's ID: "))
		if sid == None:
			print("\n\tThe student does not exist in this course!")
			return False
		else:
			mark = input("Enter the mark: ")
			temp = mark.replace(".", '')
			if temp.isnumeric() == False or float(mark) < 0 or float(mark) > 22:
				print("\n\tInvalid mark!")
			else:
				self.getMarks().update({sid: float(mark)})
				return True
			

def main():
	ads = Course("ICT2.001", "Algorithm and Data Structure")
	algeStruc = Course("MATH2.002", "Algebraic Structures")
	cal1 = Course("MATH1.001", "Calculus I")
	oop = Course("ICT2.002", "Object-oriented Programming")
	courses = {ads.getID():ads,
			algeStruc.getID():algeStruc,
			cal1.getID():cal1,
			oop.getID():oop}
	
	print("Current existing courses:")
	for course in courses.values():
		print(f"{course.getID()} - {course.getName()}")

	# student1 = Student("22BI13482", "Tran Anh Vu", "04-09-2004")
	# student2 = Student("22BI13392", "Dao Thai Son", "19-10-2004")
	# student3 = Student("22BI13789", "Vu Ham Thieu", "18-07-2004")

	# class1 = CourseClass("G5")
	# class1.info()
	# class1.addStudent()
	# class1.info()

	# class2 = CourseClass("G4")
	# class2.info()
	# class2.addStudent()
	# class2.info()
	# class1.addStudent()
	# class1.info()
		
	while True:
		print("H===========================================================H")
		print("Current existing courses:")
		for course in courses.values():
			print(f"{course.getID()} - {course.getName()}")
		print("""
			0. Exit
			1. Input student(s) to a class
			2. Input class
			3. Input course
			4. Select a course, input marks for student in this course
			5. List courses' info
			6. Show student marks for a course""")
		print("\nH===========================================================H")		
		option = input("Your choice: ")
		if option.isnumeric():
			option = int(option)
		else:
			option = -1

		if option == 0:
			print("Exiting program.")
			break
		elif option == 1:
			cid = input("Enter the ID of the course to add students to: ")
			if cid in courses:
				className = input("Enter the name of the class to add student to: ")
				for clas in courses[cid].getClasses():
					if className == clas.getName():
						clas.addManyStudent()
					else:
						print("\n\tInvalid class!")
			else:
				print("\n\tInvalid course ID!")
		elif option == 2:
			cid = input("Enter the ID of the course to add a class to: ")
			if cid in courses:
				course = courses[cid]
				course.addClass()
			else:
				print("\n\tInvalid course ID!")
		elif option == 3:
			addCourse(courses)
		elif option == 4:
			cid = input("Enter the ID of the course to input marks for: ")
			if cid in courses:
				course = courses[cid]
				course.addMark()
			else:
				print("\n\tInvalid course ID!")
		elif option == 5:
			for course in courses.values():
				print("-------------------------------------------------------------------")
				course.info()
		elif option == 6:
			cid = input("Enter the ID of the course to show student marks: ")
			if cid in courses:
				course = courses[cid]
				course.displayMarks()
			else:
				print("\n\tInvalid course ID!")
		else:
			print("\n\tInvalid option. Please choose a valid option.")

	
if __name__ == "__main__":
	main()