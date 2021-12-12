
'''class Student:
    def language(self, name ='python'):
        print(f"This is the language that i love most {name}");
d1 =Student();
d1.language()
d1.language("java");
d1.language("Ravi Kiran Konda");'''

class Student:
    def Name(self, name ="Ravi"):
        print(f"Hello Hi This is {name}")
    def Age(self, age ="78"):
        print(f" and my age is {age}");
s = Student();
s.Age();


class Employee():
    def __init__(self, name, age, exp):
        self.name =name;
        self.age =age;
        self.exp =exp;
    def Name (self,name):
        print(f"Hello Good morning This is {name} ");
    def Age (self ,age):
        print(f"And my age is {age}");
    def Experience(self,exp):
        print(f"And I had {exp} years of Experience;");
emp = Employee("Ravi Kiran",45,8);
emp.Name("Ravi Kiran");
emp.Age(45);
emp.Experience(8);
