university = {
    'students': [],
    'professors': []
}

class Person():
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age 

    def __str__(self):
        return f'Hi! my name is {self.name} and i am {self.age} years old!'

class Student(Person):
    def __init__(self, name:str, age:int, student_id:int, courses:set) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses

    def enroll_course(self, course_name:str) -> None:
        if course_name not in self.courses:
            print("Invalid course")
            return
        
        for student in university['students']:
            if student['student'].student_id == self.student_id:
                if(student['course'] is not None):
                    print("You are currently enrolled!")
                    break
                student['course'] = course_name
                print("Enrolled Successfully!")
                break
        return

    def drop_course(self, course_name:str) -> None:
        if course_name not in self.courses:
            print("Invalid course")
            return
        
        for student in university['students']:
            if student['student_id'] == self.student_id:
                if(student['course'] == None):
                    print("You are not currently enrolled")
                    break
                student['course'] == None                 
                print("Drop Successfully!")
                break
        return            

    def get_details(self):
        pass

class Professor(Person):
    def __init__(self, name:str, age:int, employee_id:int, department:str) -> None:
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

        university['professors'].append({
            'employee_id':self.employee_id,
            'department': self.department
        })


    def assign_grade(self, student_id:int, course_name:str, grade: str) -> None:
        pass

class Course:
    def __init__(self, course_name:str, professor: Professor) -> None:
        self.course_name = course_name
        self.professor = professor
        self.students_enrolled = [dict]
    
    def enroll_student(self, student_id:int) -> None:
        for students in self.students_enrolled:
            if student_id == students['student_id']:
                print(f'This student is already enrolled')
                return
            
        new_student:dict = {
                     'student_id': student_id, 
                     'grade': None
                    }
        self.students_enrolled.append(new_student)

    def remove_student(self, student_id:int) -> None:
        pass

def main() -> None:
    student_1 = Student('Jose Dalanon',21,1,['BSIT','BSCS','BSCE'])
    student_2 = Student('Maria Magalang',21,2,['BSIT','BSCS','BSCE'])

    for students in university['students']:
        print(students['student'])

if __name__ == "__main__":
    main()
