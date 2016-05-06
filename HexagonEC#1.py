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
    t.up()
    t.goto(400,90)
    t.down()
    x=xs
    while x>1:
        for i in range(20):
            t.pencolor('blue')
            t.forward(x)
            t.backward(x)
            t.right(5)
            t.right(90)
        for i in range(4):
            t.pencolor('green')
            t.forward(x)
            t.right(90)
            t.forward(x)
        for i in range(20):
            t.pencolor('red')
            t.right(30)
            t.forward(x)
        y=f(x)
        x=y

    
