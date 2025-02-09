
class Student:
    classroom = '106'
    address = 'beijing'

    def __init__(self,username,age):
        self.name = username
        self.age = age

    def print_info(self):
        print('%s: %s' %(self.name,self.age))

s1 = Student('tom', 29)
s2 = Student('ucs','19')

s1.print_info()