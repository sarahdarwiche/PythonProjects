import sys; sys.path.append("/Users/Shared/cs8");
import cTurtle
t = cTurtle.Turtle()
def f(x):
    if x%2 == 0:
       y = x//2
    else:
       y = 3*x+1
    return y
def draw(xs):
    x=xs
    while x>1:
        for i in range(3):
            t.forward(x)
            t.right(120)
        for i in range(3):
            t.right(180)
            t.pencolor('red')
            t.right(40)
            t.forward(x)
            t.right(20)
        t.pencolor('black')
        t.right(20)
        y=f(x)
        x=y
    
    
    
