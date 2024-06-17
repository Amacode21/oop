class Person():
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age 

    def __str__(self):
        return f'Hi! my name is {self.name} and i am {self.age} years old!'
class Student(Person):
    def __init__(self, name:str, age:int, student_id:int) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = set()

    def enroll_course(self, course_name:str) -> None:
        self.courses.add(course_name)  

    def drop_course(self, course_name:str) -> None:
        if course_name in self.courses:
            self.courses.remove(course_name)
        else:
            print('Course cant find')      

    def get_details(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'ID: {self.student_id}')
        print(f'Courses Currently Enrolled')
        print(f'--------------------------')
        if len(self.courses) < 1:
            print('No courses enrolled')
            return
        for _, course in enumerate(self.courses, 1):
            print(f'{_}. {course}')
class Professor(Person):
    def __init__(self, name:str, age:int, employee_id:int, department:str) -> None:
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def assign_grade(self, student_id:int, course_name:'Course', grade: str) -> None:
        is_exist = False
        for student in course_name.students_enrolled:
            is_found = False
            if is_found:
                break     
            if(student['student_id'] == student_id):
                student['grade'] = grade
                is_found = is_exist = True
        print(f'Student not found' if is_exist is not True else 'Grade assigned')

class Course:
    def __init__(self, course_name:str, professor: Professor) -> None:
        self.course_name = course_name
        self.professor = professor
        self.students_enrolled = []
    
    def show_students_enrolled(self) -> None:
        print(f'---{self.course_name}---')
        print('List of Students Enrolled')
        print('------------------------')
        for student in self.students_enrolled:
            for k, v in student.items():
                print(f'{k}: {v}', end=' ')
            print('')

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
        print('Student Enrolled')

    def remove_student(self, student_id:int) -> None:
        for index, students  in enumerate(self.students_enrolled):
            if student_id == students['student_id']:
                self.students_enrolled.pop(index)
                print('Student removed')
                return
        print('Student did not exist')

    def __str__(self) -> str:
        self.x = f'Course: {self.course_name}\nProfessor: {self.professor.name}'
        return self.x

        
def main() -> None:
    import csv

    container = {
        'students': [],
        'professors': [],
        'courses': []
    }

    with open('students.csv',newline='') as f:
        student = csv.DictReader(f)
        for s in student:
            name = s['name']
            record = Student(s['name'], int(s['age']), int(s['id']))
            container['students'].append({'name':name,'record': record})

    for student in container['students']:
        print(f'{student['record'].student_id}. {student['name']}')
    

if __name__ == "__main__":
    main()
