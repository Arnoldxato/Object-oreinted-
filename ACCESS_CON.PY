class student:
    def __init__ (self, name):
     self.name = name
     self.gpa = 3.5
     self._password = "1234" 

student  = student('xato')
print(student.name)
# print(student.gpa)