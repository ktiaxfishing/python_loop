print()
print('start...')
print()
def hello3time():
    print('hello')
    print('hello')
    print('hello')

def hello(name):
    print('hello,', name)

# hello('john')
# hello('dan')
def hello2(name, name2):
    print('hello,', name, 'and', name2, '.')
# hello2('john', 'dan')

def cal(num1, num2, num3):
    print(num1 * num2 + num3)
    print('hello')

# cal(5,10,3)

# for i in range(2):
#     print('----start------')
#     hello3time()
#     print('-----end-----')


def a():
    print('a')
    print('hello')
    print('hello')
    print('hello')
    print('hello')

def ab():
    print('b')

# import math
# math.pi => 180
# pi/2 => 90
# pi/3 => 60
# pi/6 => 30
# print(math.sin(math.pi/6))


# required and optional argument
def mul(num1, num2=9, num3=10):
    print(num1, num2, num3)

# mul(5, 4)


num = 5 # global variable
a = 10

def a(num, a): # local variable
    num = 7
    print('num in function=', num)

def a(): # local variable
    global num, a
    num = 7
    print('num in function=', num)

a()
print('num out func=',num)
