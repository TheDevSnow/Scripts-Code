import turtle

print("Fullscreen is required.")

wn = turtle.Screen()
wn.title("Cookie Clicker mini-game by @TheDevSnow")
wn.bgcolor("black")

wn.register_shape(r"C:\Users\iCan Student\Desktop\Python\cookie.gif")
wn.register_shape(r"C:\Users\iCan Student\Desktop\Python\cursor.gif")
wn.register_shape(r"C:\Users\iCan Student\Desktop\Python\grandma.gif")

cookie = turtle.Turtle()
cookie.shape(r"C:\Users\iCan Student\Desktop\Python\cookie.gif")
cookie.speed(0)

cursor = turtle.Turtle()
cursor.shape(r"C:\Users\iCan Student\Desktop\Python\cursor.gif")
cursor.speed(0)
cursor.penup()
cursor.goto(300, 150)

grandma = turtle.Turtle()
grandma.shape(r"C:\Users\iCan Student\Desktop\Python\grandma.gif")
grandma.speed(0)
grandma.penup()
grandma.goto(500, -200)

clicks = 0
increment = 1
grandmawork = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
pen.goto(-250, 50)
pen.write(f"Cursors: {increment}", align="center", font=("Courier New", 20, "normal"))
pen.goto(-250, 0)
pen.write(f"Grandmas: {clicks}", align="center", font=("Courier New", 20, "normal"))

def clicked(x, y):
    global clicks, increment, grandmawork
    clicks += increment
    pen.clear()
    pen.penup()
    pen.goto(0, 200)
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))


def upgrade(x, y):
    global clicks, increment
    if clicks >= 50:
        clicks -= 50
        increment += 1
        pen.clear()
        pen.penup()
        pen.goto(-250, 50)
        pen.write(f"Cursors: {increment}", align="center", font=("Courier New", 20, "normal"))
        
    elif clicks < 50:
        pen.penup()
        pen.goto(0,0)
        pen.pendown()
        pen.write(f"You do not have enough cookies to buy this upgrade", align="center", font=("Courier New", 20, "normal"))
        pen.penup()


def grandmaupgrade():



cookie.onclick(clicked)
cursor.onclick(upgrade)

wn.mainloop()


