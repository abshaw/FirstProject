import inspect
import Test2

from functions.simple.arithmetic import *

def call_me(a, b) :
    return (a + b)/(a * b);
dir(Test2)

print(callable(call_me));

print(callable(add));


print("Hello python")
g = call_me(2.2,3.3);
print('Result is : {0:1f}'.format(g));

g = Test2.call_me_again(2.2,3.3);
print('Result again : {0:1f}'.format(g));

a = add(2.2, 1.1);
s = subtract(2.2, 1.1);
m = multiply(2.2, 1.1);
d = divide(2.2, 1.1);

print('Result is : {0}, {1} {2} {3}'.format(a, s, m, d));


for z in inspect.getmembers(inspect):
    print(z);



for x in dir(s):
    print("{0} :::::: {1}".format(x, x.__doc__));


res = eval("add(40, 67)");

print(res);