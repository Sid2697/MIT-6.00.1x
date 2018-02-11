import datetime


class Person(object):
    def __init__(self, name):
        '''
        This creates a person when name is provided
        '''
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        self.firstName = name.split(' ')[0]

    def __str__(self):
        '''
        Defining manner in which class would print out name
        '''
        return self.name

    def __lt__(self, other):
        '''
        Return True if self's name is Lexicographically less than other's name, and Flase otherwse
        '''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.getLastName

    def getLastName(self):
        '''
        Returns self's last name
        '''
        return self.lastName

    def getFirstName(self):
        '''
        Returns self's first name
        '''
        return self.firstName

    def setBirthday(self, day, month, year):
        '''
        Set's self's birhday to birthday
        '''
        self.birthday = datetime.date(year, month, day)
        return self.birthday

    def getAge(self):
        '''
        Returns self current age in years
        '''
        if self.birthday == None:
            raise ValueError('Date of Birth not provided!')
        return '{} {}'.format(int((datetime.date.today() - self.birthday).days / 365), 'years')


class VgecPerson(Person):
    nextIdNum = 0  # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)  # Initilize Person attribute
        self.idNum = VgecPerson.nextIdNum  # VgecPerson attribute: Unique ID
        VgecPerson.nextIdNum += 1

    def getIdNum(self):
        '''
        Returns ID number of student at VGEC
        '''
        return self.idNum
    # sorting VGEC people uses ther ID number, not name!

    def __lt__(self):
        return self.idNum < other.idNum

    def speak(self, utterance):
        '''
        Defines the manner in which VGEC Students speak
        '''
        return (self.getFirstName() + ' says ' + utterance)


class Student(VgecPerson):
    '''
    Defining a class student as subclass of VgecStudent
    '''
    pass


class UG(Student):
    '''
    A class inhereted from VgecPerson
    '''

    def __init__(self, name, classYear):
        '''
        Initialization method of UG
        '''
        VgecPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        '''
        Tells the year of UG student
        '''
        return self.year

    def speak(self, utterance):
        '''
        Defines the manner in which UG student speaks
        '''
        return VgecPerson.speak(self, "Dude, " + utterance)


class Grad(Student):
    '''
    Defining another class Grad inhereted from VgecPerson
    '''
    pass


class TransferStudent(Student):
    '''
    Defining third type of student Transfer Student
    '''
    pass


def isStudent(obj):
    '''
    Checking weaher a person is student or not
    '''
    return isinstance(obj, Student)


class Professor(VgecPerson):
    '''
    A new class of officers in VGEC
    '''

    def __init__(self, name, department):
        '''
        Initialization method for Professor
        '''
        VgecPerson.__init__(self.name)
        self.department = department

    def speak(self, utterance):
        '''
        Speak method for Professor
        '''
        new = 'In course ' + self.department + ' we say '
        return VgecPerson.speak(self, new + utterance)

    def lecture(self, topic):
        '''
        Method defining which lecture professor is going to take
        '''
        return self.speak('it is obvious that ' + topic)


class Grades(object):
    '''
    Defining a class for handling grades
    '''

    def __init__(self):
        '''
        Create empty grade book
        '''
        self.students = []  # List of student object
        self.grades = {}  # maps idNUm -> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        '''
        Assumes: Student is of type Student
        Add student to the grade book
        '''
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def getStudent(self):
        '''
        Returns list of students
        '''
        return self.students

    def addGrade(self, student, grade):
        '''
        Assumes: Grade is a float
        Add grade to the list of grades for student
        '''
        try:
            self.grades[student.getIdnum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        '''
        Return a list of grades for student
        '''
        try:
            return self.grade[student.getIdnum()][:]  # Return a copy of grades
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        '''
        Return a list of students in the grade book
        '''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.Students[:]  # Returns a copy of students

    def gradeReport(self, course):
        '''
        Assumes: course is of type grades
        '''
        for s in course.allStudents():
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot / numGrades
                report.append(str(s) + '\'s mean grade is' + str(average))
            except ZeroDivisionError:
                report.append(str(s) + 'has no grades')
        return '\n'.join(report)


# a = VgecPerson('Siddhant Bansal')
# b = Person('Seema Bansal')
# c = Person('Astha Bansal')
# d = Person('Sanjay Bansal')
# a.setBirthday(26, 3, 1997)
# b.setBirthday(11, 7, 1972)
# c.setBirthday(5, 10, 2003)
# d.setBirthday(1, 3, 1972)
# BansalFamily = [a, b, c, d]
# BansalFamily.sort()
# for member in BansalFamily:
#     print ('{} {} {} {}'.format(member, 'is', member.getAge(), 'old.'))

# print(a.getLastName())
# print(a.getFirstName())
# print(a.getAge())
# print(b.getLastName())
# print(b.getFirstName())
# print(b.getAge())
# print(c.getLastName())
# print(c.getFirstName())
# print(c.getAge())
# print(d.getLastName())
# print(d.getFirstName())
# print(d.getAge())
# print(a.speak('Hello!'))


# s1 = UG('Siddhant Bansal', 2016)
# s2 = UG('Ram Chaudhari', 2015)
# s3 = UG('Ramesh Patel', 2016)
# s4 = Grad('Leonardo di Caprio')
# s5 = TransferStudent('Robert deNiro')
# # faculty = Professor('Siddhant','Electronics and Communication')
# print(s1)
# print(s1.getClass())
# print(s1.speak('Where is the Quiz?'))
# print(s2.speak('I have no idea!'))


# ug1 = UG('Siddhant Bansal', 2018)
# ug2 = UG('Amitabh Bacchan', 1997)
# ug3 = UG('Tarry Singh', 2010)
# ug4 = UG('Neil Armstrong', 1990)
# g1 = Grad('Bill Gates')
# g2 = Grad('Steve Jobs')

# six00 = Grades()
# six00.addStudent(g1)
# six00.addStudent(ug2)
# six00.addStudent(ug1)
# six00.addStudent(g2)
# six00.addStudent(ug4)
# six00.addStudent(ug3)

# print(Grades.gradeReport(six00))
# print(six00.gradeReport())
# a = six00.sort()
# for s in six00.students:
#     print(s)
