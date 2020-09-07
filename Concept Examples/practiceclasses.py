class Person:
  def __init__(self, name, age, occupation):
    self.name = name
    self.age = age
    self.occupation = occupation

  def myfunc(self):
    print("Hello my name is " + self.name + " " + self.occupation)
    print(self.age)

p1 = Person("John", 36, "Electrician")
p1.myfunc()
p2 = Person("Drew", 20, "Student")
p2.myfunc()
