
class Student():
    name = '' # 类变量
    age = 0
    sum = 0

    def __init__(self, name, age):
        self.name = name # 实例变量
        self.age = age
        print('class Name age', self.name,self.age)
        print('summm', self.__class__.sum) # 类变量的调用使用 self.__class__

    def print_file(self):
        self.name = 'changeSimone'
        print('age', self.age)
    
    @classmethod  # 使用classmethod装饰器表示定义了类方法
    def plus_sum(cls):
        cls.sum += 1
        print('clsmethod', cls.sum)
    
    @staticmethod   # staticmethod定义静态方法，静态方法同样可以访问类变量
    def add(x, y):
        print(Student.sum)
        # print(self.name)
        print('This is a static method', x + y)



student = Student('simone', 18)
# print(student.name)
# student.print_file()
# print(student.name)

# print('Student',Student.name) # 类变量直接通过类来调用，区别于js里面的需要通过指定static为静态变量才能调用

# print(id(student1), id(student2), id(student3))

# Student.plus_sum()
# Student.plus_sum()
# Student.plus_sum() # 通过类调用类方法
student1 = Student('simone', 18)
student2 = Student('ximeng', 20)
student2.plus_sum()
student3 = Student('mengli', 20)
student3.plus_sum()

Student.add(1,5)
student.add(1,5)


