class Person():
    def __init__(self, name:str = '', age:int = 0, gender:str = '' ):
        self.name = name
        self.age = age
        self.gender = gender
    
    def walk(self):
        return 'Im walking!'
    
    def __str__(self):
        return f'Hello my name is {self.name} im {self.age} years old : {self.gender}'


class Student(Person):
    def __init__(self, name, age,gender, grade) -> None:
        super().__init__(name, age, gender)
        self.grade = grade

    def __iter__(self):
        self.n = 1
        return self
    
    def __next__(self):
        if(self.n <= 20):
            x = self.n
            self.n += 1
            return x
        else:
            raise StopIteration

    def __str__(self):
        return f'Hello my name is {self.name} im {self.age} years old i am grade {self.grade}'




def main():
    new_person = Student('Jose',21,'Male',6)
    print(new_person)
    print(new_person.walk())
    new_person.circle(4)

if __name__ == "__main__":
    main()