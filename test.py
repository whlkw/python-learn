from enum import Enum, unique
import os
import json
import time
import threading

def buildConnectionString(age):
   if age > 50:
       print('You are old')
   elif age < 50 and age > 10:
       print('You are young')
   else:
       print('child')

def getPower(x):
    return x * x

def computeMultiple(x, *y):
    res = x
    for num in y:
      res *= num
    return res

def trimString(s):
    while(s[:1] == ' '):
      s = s[1:]
    while(s[-1:] == ' '):
      s = s[:-1]
    return s;

def generateList():
    list = ['Hello', 'World', 18, 'Apple', None]
    resList = [item for item in list if isinstance(item, str)]
    print(resList)

def highOrderFunction(x, y, f):
    return f(x) + f(y)

def _odd_iter():
    n = 1
    while True:
      n = n + 2
      yield n
def _not_visible(n):
    return lambda x: x % n > 0
def Primes():
    yield 2
    it = _odd_iter()
    while True:
      n = next(it)
      yield n
      it = filter(_not_visible(n), it)

def lazy_sum(*args):
    def sum():
        res = 0
        for n in args:
            res += n
        return res
    return sum

@unique
class Gender(Enum):
    male = 0
    female = 1

def loop():
   print('Threading %s is running ...' % threading.current_thread().name)
   n = 0
   while (n < 5):
       n = n + 1
       print('threading %s >>> %s' % (threading.current_thread().name, n))
       time.sleep(1)

def TestThread():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

class Student(object):
    def __init__(self, name, gender):
       self.name = name
       self.gender = gender

    def get_name(self):
       return self.name

def product(*numbers):
    sum = 0;
    for n in numbers:
        sum += n;
    return sum;


if __name__ == "__main__":

    print("The product is: %d" % product(10, 20, 30))
    print("The product is: %d" % product(-10, 10, 20, 30))

    buildConnectionString(100)
    base = 100;
    power = getPower(base)
    print('the %d power result is %d' % (base, power))

    print(computeMultiple(10, 30, 3))

    print(trimString('  This is a space at the head'))
    print(trimString('this is a space at tail  '))

    generateList()

    print(highOrderFunction(-10, -20, abs))

    print('Compute the primes before number 300:')
    for prime in Primes():
        if (prime < 300):
            print(prime)
        else:
            break

    #print map(lambda x:x**2, range(10))

    print('The sum is: ')
    print(lazy_sum(20, 10, 3, 3)())

    st = Student('Haha', Gender.male)
    print('My name is %s' % st.get_name())

    p = os.path.abspath('.');
    print(p)

    file = open('/Users/hualinwu/Desktop/test/License.txt', mode='r')
    content = file.read();
    #print(content)

    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=True)

    print('Process (%s) start...' % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
       print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
       print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

    TestThread()
