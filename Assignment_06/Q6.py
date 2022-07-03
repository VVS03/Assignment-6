class Student:
    def __init__(self, name, Class):
        self.name = name 
        self.Class = Class

    def get_student(self):
        print(f"Student ID:\nName : {self.name} \nClass : {self.Class}")

SID1 = Student("Rajat", "Civil")
SID2 = Student("Saachika", "CSE")
SID3 = Student("Aakash", "Mechanical")
SID4 = Student("Kavya Joshi", "Metallurgy")

SID1.get_student()
print()
SID2.get_student()
print()
SID3.get_student()
print()
SID4.get_student()
print()

