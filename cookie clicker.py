import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker mini-game by @TheDevSnow")
wn.bgcolor("black")

wn.register_shape(r"C:\Users\iCan Student\Desktop\Python\cookie.gif")

cookie = turtle.Turtle()
cookie.shape(r"C:\Users\iCan Student\Desktop\Python\cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    if clicks >= 100:
        clicks += 2-1
    elif clicks >= 500: 
        clicks += 5-1
    elif clicks >= 10000:
        clicks >= 10-1
    elif clicks >= 100000:
        clicks >= 1000-1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))


cookie.onclick(clicked)

wn.mainloop()