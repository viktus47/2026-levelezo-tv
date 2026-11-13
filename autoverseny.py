# import osztaly
# t1 = osztaly.Teglalap()
# print('Terület:', t1.kerulet())


# autóverseny

import turtle

class Auto(turtle.Turtle):
    def __init__(self,szin, x, y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.goto(x,y)
        self.sebesseg = sebesseg

    def indit(self):
        self.forward(self.sebesseg)


ablak = turtle.Screen()
ablak.bgcolor("black")
ablak.title("Autóverseny")

a1 = Auto("red", -400, 200, 15)
a2 = Auto("blue", -400, -200, 20)
ablak.listen()

ablak.onkey(turtle.bye, "Escape")
ablak.onkey(a1.indit, "d")
ablak.onkey(a2.indit, "s")


turtle.mainloop()