import turtle
turtle.shape('turtle')
turtle.color('red')
def sqr(x):
	turtle.forward(x)
	turtle.left(90)
	turtle.forward(x)
	turtle.left(90)
	turtle.forward(x)
	turtle.left(90)
	turtle.forward(x)
	turtle.right(45)
	turtle.penup()
	turtle.forward(13)
	turtle.pendown()
	turtle.left(135)

sqr(20)
sqr(40)
sqr(60)
sqr(80)
sqr(100)
sqr(120)
sqr(140)
sqr(160)
sqr(180)
sqr(200)