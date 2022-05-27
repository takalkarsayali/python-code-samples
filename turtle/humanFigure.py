import turtle

def draw_dream():
	window = turtle.Screen()
	window.bgcolor("white")
	draw_Scarlett()
	window.exitonclick()


def draw_Scarlett():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	draw_head(brad)
	draw_body(brad)
	draw_arm(brad)
	draw_leg1(brad)
	draw_leg2(brad)


def draw_head(brad):
	brad.circle(60)
	brad.speed(3)
	brad.right(60)


def draw_body(brad):
	num = 0
	while num < 3:
		brad.forward(150)
		brad.right(120)
		brad.speed(1)
		num += 1


def draw_arm(brad):
	brad.forward(60)
	brad.left(60)
	brad.forward(60)

	brad.backward(60)
	brad.right(60)
	brad.backward(60)

	brad.right(60)

	brad.forward(60)
	brad.right(60)
	brad.forward(60)

	brad.backward(60)
	brad.left(60)
	brad.forward(90)


def draw_leg1(brad):
	brad.left(120)
	brad.forward(40)
	brad.right(120)
	brad.forward(120)
	draw_foot1(brad)


def draw_leg2(brad):
	brad.color("red")
	brad.right(180)
	brad.forward(120)
	brad.right(60)
	brad.forward(70)
	brad.right(60)
	brad.forward(120)
	draw_foot2(brad)


def draw_foot1(brad):
	brad.color("blue")
	num = 0
	while num < 4:
		brad.forward(20)
		brad.right(90)
		num += 1


def draw_foot2(brad):
	brad.color("blue")
	num = 0
	while num < 4:
		brad.forward(20)
		brad.left(90)
		num += 1


draw_dream()
