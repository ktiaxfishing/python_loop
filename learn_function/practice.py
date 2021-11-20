
# write a function named "gen_mul" to get an argument as int
# this function can generate multiply table
# ex.
'''
gen_mul(3)
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 12 = 36
'''

# code here
def gen_mul(num):
    for i in range(12):
        i += 1
        print(num ,"x", i, "=", num * i)
        
# gen_mul(17)

# DRY -> Don't Repeat Yourself
def my_print(num, i):
    print(num ,"x", i, "==", num * i)

def gen_mul2(num):
    for i in range(12):
        i += 1
        my_print(num, i)

# gen_mul2(6)


# write a function to calculate petagorus a^2 + b^2 = c^2
# this function get two arguments a and b
# return c

print('start...')
# code here
def petagorus(a=0, b=0, c=0):
    if c != 0:
        ans = c**2 - a**2
        ans = ans**0.5
    else:
        c = (a**2 + b**2)**(0.5)
        ans = c
    return ans

c = petagorus(a=3, b=9)
print('result=',c)

result = petagorus(a=3, c=21)
print('result=',result)
