
# Show the class
# constructor and destructor
class Employee:
   empCount = 0

#The self variable represents the instance of the object itself. Most object-oriented languages
#pass this as a hidden parameter to the methods defined on an object; Python does not.
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
      print ("constructor")

   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destructor")


   def displayCount(self):
      print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print("创建 Employee 类的第一个对象")
emp1 = Employee("Zara", 2000)
print("创建 Employee 类的第二个对象")
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

# Show the class' hidden attributes
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

# The following is the class inheritance example
class Parent:
   __parentAttr = 100

   def __init__(self, att):
      self.__parentAttr = att

   def myMethod(self):
      print ('call parent method')

   def setAttr(self, val):
      Parent.__parentAttr = val;

   def getAttr(self):
      print ('parent attribute is %d' % Parent.__parentAttr)
      return Parent.__parentAttr

class Child(Parent): # 定义子类
   def __init__(self, att):
         super(Child, self).__init__(att)

   def myMethod(self):
      print ('This is child method, and the attribute is', self.getAttr())

   def __str__(self):
      return 'this is child class'

def testClassInheritance():
    c = Child(10)          # 子类实例
    c.myMethod()         # 子类调用重写方法
    c.setAttr(200)
    c.getAttr()
    print(isinstance(c, Parent))
    print(c)

testClassInheritance()
