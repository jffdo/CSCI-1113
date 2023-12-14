# Problem D parts 1,2, and 6 were chosen

import math, random
from turtle import Screen, Turtle
screen = Screen()
class Ball(Turtle):
    '''
    Purpose: 
        Represents a ball
    Instance variables: 
        Turtle.__init__(self) = inherits Turtle, creates ball
        self.x = x position
        self.y = y position
        self.vx = x velocity
        self.vy = y velocity
        self.bouce = number of bounces
        self.anglep1 = current angle of p1 the ball will be hit by
        self.anglep2 = current angle of p2 the ball will be hit by
    Methods: 
        __init__ = constructor of the class
            Parameter(s):
               x = x postion
               y = y postion 
               vx = x velocity
               vy = y velocity
        move = moves the ball
        hit = hits the ball at an angle
        reset = resets the ball
    '''
    def __init__(self, x, y, vx, vy):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.shape('circle')
        self.turtlesize(0.3)
        self.penup()
        self.setpos(self.x, self.y)

        self.bounce = 0
        self.anglep1 = 150
        self.anglep2 = 30

    def move(self):
        self.vy -= 0.981
        self.x = self.xcor() + self.vx
        if (self.ycor() + self.vy) < 0:
            self.y = -1 * (self.ycor() + self.vy) * 0.75
            self.vy = -1 * self.vy * 0.75
            self.bounce += 1
        else:
            self.y = self.ycor() + self.vy
        self.goto(self.x, self.y)

    def hit(self):
        if self.x > 0:
            new_vy = (2 * (self.vx * math.cos(math.radians(self.anglep2)) + self.vy * math.sin(math.radians(self.anglep2))) * math.sin(math.radians(self.anglep2))) - self.vy
        else:
            new_vy = (2 * (self.vx * math.cos(math.radians(self.anglep1)) + self.vy * math.sin(math.radians(self.anglep1))) * math.sin(math.radians(self.anglep1))) - self.vy
        self.vx *= -1
        self.vy = new_vy + 5

    
    def reset(self):
        self.x = random.uniform(-100, 100)
        self.y = random.uniform(30, 100) 
        self.setpos(self.x, self.y)
        self.vx = random.choice([random.uniform(-12, -6),random.uniform(6, 12)]) 
        self.vy = random.uniform(4, 10)
        self.bounce = 0

class Button:
    '''
    Purpose: 
        A button
    Instance variables: 
        self.x = x position
        self.y = y postion
        self.w = width of button
        self.h = height of button
        self.name = name of the button
    Methods: 
        __init__ = constuctor of the class
            Parameter(s):
            x = x coordinate
            y = y coordinate
            width = width of button 
            height = height of the button
            name = button display name
        contains = returns True or False depending if the cursor 
            clicked the button
            Parameter(s):
            x = x coordinate
            y = y coordinate
        function = rotates a line on the display showing the angle
            Parameter(s):
                t = the turtle to be moved
                num = int representing the angle of the line  
    '''
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.name = name
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.setpos(self.x,self.y)
        t.pendown()
        for i in range(4):
            if i % 2 == 0:
                t.fd(self.w)
                t.lt(90)
            else:
                t.fd(self.h)
                t.lt(90)
        t.penup()
        t.setpos(self.x + self.w/2, self.y + self.h/4)
        t.write('{}'.format(self.name), align='center', 
            font=('Helvetica',8))
    def contains(self, x, y):
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            return True
        else:
            return False
    
    def function(self, t, num):
        x = t.xcor()
        y = t.ycor()
        t.clear()
        t.setpos((math.cos(math.radians(num))*50) + x,
                (math.sin(math.radians(num))*50) + y)
        t.pendown()
        t.setpos((math.cos(math.radians(180+num))*50) + x,
                (math.sin(math.radians(180+num))*50) + y)
        t.penup()
        t.setpos(x,y)

class Game:
    '''
    Purpose: 
        Simulates Tennis for Two
    Instance variables: 
        self.buttons = list of Button objects
        self.t2 = turtle that draws buttons
        self.p1score = score of player 1
        self.p2score = score of player 2
        self.s = turtle object that draws the score
        self.ball = Ball object
    Methods: 
        __init__ = constructor of the class
        gameloop = simulates the game
        button_press = checks if button is pressed
            Parameter(s):
            x = x coordinate
            y = y coordinate
    '''
    def __init__(self):
        screen.delay(0)
        screen.tracer(0,0)
        screen.setworldcoordinates(-500, -500, 500, 500)
        # Create Net
        t = Turtle()
        t.hideturtle()
        t.goto(0,30)
        t.penup()
        t.goto(-400,0)
        t.pendown()
        t.goto(400,0)
        t.penup()
        # Create Button
        self.buttons = [Button(-400,-300, 50, 50,'left'), Button(-350,-300, 50, 50,'right'), Button(350,-300, 50, 50,'left'), Button(400,-300, 50, 50,'right')]
        self.t2 = Turtle() # Player 1 current angledisplay
        self.t2.penup()
        self.t2.setpos(-400, 300)
        self.t2.hideturtle()
        self.t3 = Turtle() # Player 2 current angle display
        self.t3.penup()
        self.t3.setpos(400, 300)
        self.t3.hideturtle()
        #Create score 
        self.p1score = 0
        self.p2score = 0
        self.s = Turtle()
        self.s.penup()
        self.s.hideturtle()
        self.s.goto(-400,400)
        self.s.write('Score: {}'.format(self.p1score), align='center', 
            font=('Helvetica',16))
        self.s.goto(400,400)
        self.s.write('Score: {}'.format(self.p2score), align='center', 
            font=('Helvetica',16))

        self.ball = Ball(random.uniform(-100, 100), random.uniform(30, 100), 
            random.choice([random.uniform(-12, -6),random.uniform(6, 12)]), 
            random.uniform(4, 10))
        screen.update()
        self.gameloop()
        # Button Press
        screen.onscreenclick(self.button_press)
        screen.onkeypress(self.ball.hit, 'space')
        screen.listen()
        screen.mainloop()

    def gameloop(self):
        reach_zero = (self.ball.x <= 0 <=  self.ball.xcor() + self.ball.vx) or (
            self.ball.x >= 0 >=  self.ball.xcor() + self.ball.vx)
        below_thirty = self.ball.ycor() + self.ball.vy < 30
        if (reach_zero and below_thirty) or (self.ball.bounce == 2):
            if self.ball.x < 0:
                self.p2score += 1
                self.s.clear()
                self.s.goto(-400,400)
                self.s.write('Score: {}'.format(self.p1score), align='center', 
                    font=('Helvetica',16))
                self.s.goto(400,400)
                self.s.write('Score: {}'.format(self.p2score), align='center', 
                    font=('Helvetica',16))
            else:
                self.p1score += 1
                self.s.clear()
                self.s.goto(-400,400)
                self.s.write('Score: {}'.format(self.p1score), align='center', 
                    font=('Helvetica',16))
                self.s.goto(400,400)
                self.s.write('Score: {}'.format(self.p2score), align='center', 
                    font=('Helvetica',16))
            self.ball.reset()
        if reach_zero:
            self.ball.bounce = 0
        self.ball.move()
        screen.update()
        screen.ontimer(self.gameloop, 30)

    def button_press(self, x, y):
        for i in self.buttons[:]:
            if i.contains(x,y):
                if self.buttons[:].index(i) <= 1:
                    if i.name == 'left':
                        self.ball.anglep1 += 30
                    elif i.name == 'right':
                        self.ball.anglep1 -= 30
                    i.function(self.t2, self.ball.anglep1)
                else:
                    if i.name == 'left':
                        self.ball.anglep2 += 30
                    elif i.name == 'right':
                        self.ball.anglep2 -= 30
                    i.function(self.t3, self.ball.anglep2)

if __name__ == '__main__':
    Game()