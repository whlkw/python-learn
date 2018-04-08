
#a decorator in Python is a callable Python object
# that is used to modify a function, method or class definition.

def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)

print(succ.calls)


print("function name: ", succ.__name__)
print("module name: ", succ.__module__)

#A function is a callable object, but lots of Python programmers don't know
# that there are other callable object. A callable object is an object which
# can be used and behaves like a function but might not be a function.
# It is possible to define classes in a way that the instances will be callable objects.
# The __call__ method is called, if the instance is called "like a function".
class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
	         self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print('the fib number is:', fib(10))
