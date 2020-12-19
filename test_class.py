class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myMethod(self):
        print(self.name)
        print(self.age)


p1 = Myclass("Jyotiranjan", 25)
print("before change")
p1.myMethod()
p1.age = 26
print("after change")
p1.myMethod()
