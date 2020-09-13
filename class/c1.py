
class Student():
    name = '' # 类变量
    age = 0

    def __init__(self, name, age):
        self.name = name # 实例变量
        self.age = age
        print('class Name age', self.name,self.age)

    def print_file(self):
        self.name = 'changeSimone'
        print('age', self.age)


student = Student('simone', 18)
print(student.name)
student.print_file()
print(student.name)

print('Student',Student.name) # 类变量直接通过类来调用，区别于js里面的需要通过指定static为静态变量才能调用




# print(id(student1), id(student2), id(student3))