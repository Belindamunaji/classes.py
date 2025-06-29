class Student:
    def __init__(self):
        self.total = None
        self.x = int(input("please enter the cat marks"))
        self.y = int(input("please enter the final marks"))
        print(f'cat: {self.x}  final_exam: {self.y}')
        self.admission_number = input("enter the student's admission number:")
        self.name = input("Enter student's name: ")

        print("Student Name:", self.name)
        print("Student Admission Number:", self.admission_number)

    def grades(self):
        self.total = self.x + self.y
        print(f'the total is : {self.total}')

    def qualify(self):
        if self.total > 40:
            print(f'Your total score is {self.total} Congratulations you have passed!')
        else:
            print("You have failed! ")


maureen = Student()
maureen.grades()
maureen.qualify()
alvin = Student()
alvin.grades()
alvin.qualify()
Belinda = Student()
Belinda.grades()
Belinda.qualify()
Jackie = Student()
Jackie.grades()
Jackie.qualify()
Kenduiwa = Student()
Kenduiwa.grades()
Kenduiwa.qualify()
Anita = Student()
Anita.grades()
Anita.qualify()
Abdul = Student()
Abdul.grades()
Abdul.qualify()
Carlos = Student()
Carlos.grades()
Carlos.qualify()
