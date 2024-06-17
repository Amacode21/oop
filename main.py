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
            return
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
        for student in course_name.students_enrolled:
            if(student['student_id'] == student_id):
                student['grade'] = grade
                return
class Course:
    def __init__(self, course_name:str, professor: Professor) -> None:
        self.course_name = course_name
        self.professor = professor
        self.students_enrolled = []
    
    def display_students(self) -> None:
        print(f'---{self.course_name}---')
        print('List of Students Enrolled')
        print('------------------------')
        for student in self.students_enrolled:
            for k, v in student.items():
                print(f'{k}: {v}', end=' ')
            print('\n------------------------')

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

    def __str__(self) -> str:
        self.x = f'Course: {self.course_name}\nProfessor: {self.professor.name}'
        return self.x

        
def main() -> None:
    student_1 = Student('Jose Dalanon',21,1)
    student_2 = Student('Maria Magalang',21,2)
    professor_1 = Professor('James William', 31, 1, 'CIT')
    professor_2 = Professor('Mike James', 45, 2, 'CIT')
    course_1 = Course('Intro to Web Development', professor_1)
    course_2 = Course('Introduction to Python', professor_2)

    course_1.enroll_student(student_1.student_id)
    student_1.enroll_course(course_1.course_name)

    course_1.enroll_student(student_2.student_id)
    student_2.enroll_course(course_1.course_name)
    
    professor_1.assign_grade(1,course_1,'A')
    professor_1.assign_grade(5,course_1,'B')
    course_1.display_students()

if __name__ == "__main__":
    main()
