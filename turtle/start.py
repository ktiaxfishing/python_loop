import turtle as t
import time
t.speed(0)

def sq():
    for i in range(4):
        t.fd(20)
        t.lt(90)
        

for _ in range(8):
    for i in range(8):
        sq()
        t.forward(20)
     
    t.penup() 
    t.right(180)
    t.forward(160)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    
t.done()