import gzip
import curses
import math
import pickle

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

def addStudent(studentList, stdscr): # Add student to the list
        student = studentList.makeStudent(stdscr)
        if student != None:
            studentList = studentList.getList()
            try:
                with open("./students.txt", "a+", buffering=1) as studentFile: # open file in appending mode, a+ is for appending and reading from the end of file
                    if student.getID() in studentList:
                        stdscr.addstr("\nStudent already exists. Updating info...")
                        studentList.update({f"{student.getID()}":student})

                        # Update student data in the file (take it out, change data and push back to file)
                        studentFile.seek(0, 0) # move the pointer to the beginning of the file
                        lines = studentFile.readlines() # 22BI13301-Nguyen Quang Minh-17/09/2004-15.4
                        for i in range(len(lines)):
                            if student.getID() in lines[i]:
                                # sid, name, dob, gpa = lines[i].split("-")
                                updatedLine = f"{student.getID()}-{student.getName()}-{student.getDOB()}-{student.getGPA()}\n"
                                lines[i] = updatedLine
                        # Write back to the file
                        studentFile.truncate(0) # clear contents
                        for line in lines:
                            studentFile.write(f"{line}")

                        stdscr.addstr("\n\tDone!")
                        stdscr.refresh()
                        stdscr.getch()
                    else:
                        stdscr.addstr("\nAdding the new student to the list...")
                        studentList.update({f"{student.getID()}":student})

                        # Add student data to file
                        dob = student.getDOB().replace("-","/")
                        line = f"{student.getID()}-{student.getName()}-{dob}-{student.getGPA()}\n"
                        studentFile.write(line)

                        stdscr.addstr("\n\tDone!")
                        stdscr.addstr("\nPress any key")
                        stdscr.refresh()
                        stdscr.getch()
                    
                    # Print the file content after changing
                    stdscr.clear()
                    studentFile.seek(0, 0)
                    stdscr.addstr(studentFile.read())
                    stdscr.refresh()
                    stdscr.getch()
            except IOError:
                stdscr.addstr("\n\tError handling file!")
                stdscr.refresh()
                stdscr.getch()

def updateCourse(courseList, stdscr): # Add or reinitialize a course
    c = courseList.makeCourse(stdscr)
    try:
        if c != None:
            with open("courses.txt", "a+", buffering=1) as courseFile:
                if c.getID() in courseList.getCourses():
                    courseList.getCourses().update({c.getID():c})
                    courseFile.seek(0,0)
                    lines = courseFile.readlines()
                    for i in range(len(lines)):
                        if c.getID() in lines[i]:
                            updatedLine = f"{c.getID()}-{c.getName()}-{c.getCredit()}\n"
                            lines[i] = updatedLine
                    # Update file contents
                    courseFile.truncate(0) # Clear contents
                    for line in lines:
                        courseFile.write(line)
                else:
                    courseList.getCourses().update({c.getID():c})
                    newLine = f"{c.getID()}-{c.getName()}-{c.getCredit()}\n"
                    courseFile.write(newLine)
                stdscr.addstr("\nUpdating.")
                stdscr.addstr("\n\tDone!")
                # Display the file contents after update
                courseFile.seek(0,0)
                lines = courseFile.readlines()
                for i in range(len(lines)):
                    stdscr.addstr(lines[i])
                    y, x = curses.getsyx()
                    if y == curses.LINES - 1: # if the cursor is at the last line, clear screen to avoid error
                        stdscr.getch()
                        stdscr.clear()

                stdscr.addstr("\n\tPress any key to continue")
                stdscr.refresh()
                stdscr.getch()
        else:
            stdscr.addstr("\n\tThere is no course to add!")
            stdscr.addstr("\nPress any key to continue")
            stdscr.refresh()
            stdscr.getch()
    except IOError:
        stdscr.addstr("\n\tError handling file!")
        stdscr.addstr("\nPress any key to continue")
        stdscr.refresh()
        stdscr.getch()

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
        # stdscr.refresh()

        studentList[sid].enroll(stdscr, course.getID(), course.getName(), course.getCredit())
        course.getStudents().update({sid:[studentList[sid].getName(), 0]})

def addMark(course, stdscr, studentList): # Add mark for a specific student in a course
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
            course.getStudents()[sid][1] = mark
            studentList[sid].setMark(stdscr, course.getID(), mark)
            with open("marks.txt", "a+") as markFile: # StudentID-CourseID-Mark
                markFile.seek(0,0)
                lines = markFile.readlines()
                done = False
                for i in range(len(lines)):
                    if sid in lines[i] and course.getID() in lines[i]:
                        updatedLine = f"{sid}-{course.getID()}-{mark}\n"
                        lines[i] = updatedLine
                        done = True
                markFile.truncate(0)
                markFile.seek(0,0)
                for line in lines:
                    markFile.write(line)
                # Display contents after update
                markFile.seek(0,0)
                lines = markFile.readlines()
                for line in lines:
                    stdscr.addstr(line)
                    stdscr.refresh()
                    y, x = curses.getsyx()
                    if y == curses.LINES - 1:
                        stdscr.getch()
                        stdscr.clear()

                if not done:
                    line = f"{sid}-{course.getID()}-{mark}\n"
                    markFile.write(line)


        except curses.error:
            stdscr.addstr("\n\tFailed to add mark!")
            stdscr.refresh()
            stdscr.getch()
        except IOError:
            stdscr.addstr("\n\tError handling file!")
            stdscr.refresh()
            stdscr.getch()

def decompress(compressedFile, stdscr):
    # with gzip.open(compressedFile, "rb") as file:
    #     data = file.readlines()
    with gzip.open(compressedFile, "rb") as dataFile:
        pickledData = dataFile.read()
    data = pickle.loads(pickledData)
        # stdscr.addstr(data)
    # for line in data:
    #     for i in line:

            # stdscr.addstr(i)
            # stdscr.refresh()
            # stdscr.getch()
        # stdscr.addstr("hehe")
    # stdscr.refresh()
    # stdscr.getch()
    return data

def loadData(data, stdscr):
    studentDataX, courseDataX, markDataX = data
    section = None
    studentData = []
    courseData = []
    markData = []
    for line in studentDataX:
        # line = line.strip()
        # stdscr.addstr(str(line))
        # stdscr.refresh()
        # stdscr.getch()
        # stdscr.clear()
        if "STUDENT" in line:
            section = line
        else:
            
            sid, sName, dob, gpa = line.split("-")
            dob=dob.replace("/", "-")
            studentData.append((sid, sName, dob, gpa))
            # stdscr.addstr(f"{sid}-{sName}-{gpa}")
            # stdscr.refresh()
            # stdscr.getch()
    # stdscr.getch()
    for line in courseDataX:
        if "COURSE" in line:
            section = line
        else:
            
            courseID, cName, credit = line.split("-")
            credit = int(credit)
            courseData.append((courseID, cName, credit))
                # stdscr.addstr(f"{courseID}-{cName}")
                # stdscr.refresh()

    for line in markDataX:
        if "MARK" in line:
            section = line
        else:
    
            sid, cid, mark = line.split("-")
            mark = float(mark)
            markData.append((sid,cid,mark))

    return (studentData, courseData, markData)