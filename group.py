from datetime import date
BXXXX
class Register:
    def __init__(self, date):
        self.date = date
        self.students = []   

    def check_in(self, student_name):
        
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"{student_name} checked in.")
        else:
            print(f"{student_name} is already checked in!")

    def is_present(self, student_name):
        
        return student_name in self.students

    def list_students(self):
        
        print(f"Present students on {self.date}:")
        for student in self.students:
            print(f"- {student}")



register = Register(date.today())


register.check_in("XATO")
register.check_in("XACIA")
register.check_in("KATO")
register.check_in("CHURCHILL")
register.check_in("LILLIAN")


register.check_in("XATO")


print("\nChecking attendance:")
print("Is XATO present?", register.is_present("XATO"))
print("Is XACIA present?", register.is_present("XACIA"))


print("\nFull Attendance List:")
register.list_students()
