# class method as a constructor
class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    @staticmethod
    def hello():
        print('hello, static method is called')

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18



p1 = Person('Mohit','Chaudhary',10)
p2 = Person('mohit', 'Chaudhary', 24)

p3 = Person.from_string('Mohit,Chaudhary,24')
