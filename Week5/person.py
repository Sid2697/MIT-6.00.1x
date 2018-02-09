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

# print(isStudent(s5))
# print(isStudent(b))
