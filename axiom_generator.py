import sys
import  turtle

class Lsystem:
    def __init__(self,startx,starty,startangle,length,angle,axiom,rules):
        self.SetParams(startx,starty,startangle,length,angle,axiom,rules)
    def SetParams(self,startx,starty,startangle,length,angle,axiom,rules):
        self.startx = startx
        self.starty = starty
        self.startangle = startangle
        self.length = length
        self.angle: float = angle
        self.axiom = axiom
        self.rules = {}
        self.syms = {}
        count = 0;
        for str in rules:
            if str != "":
                str.replace("–", "-")
                str.replace(" ", "")
                (sym, rule) = str.split('=')
                self.syms[count] = sym
                self.rules[sym] = rule
                count += 1

    def GenerateNSteps(self,n):
        print(self.axiom)
        for i in range(1,n):
            for n,sym in self.syms.items():
                self.axiom = self.axiom.replace(sym,str(n))
            print(self.axiom)
            for n, sym in self.syms.items():
                self.axiom = self.axiom.replace(str(n), self.rules[sym])
            print(self.axiom)


    def Draw(self,isInstant,s):
        if (isInstant):
            turtle.Screen().tracer(0)
            s=int(10)
        turtle.speed(int(s))
        turtle.penup()
        turtle.goto(self.startx,self.starty)
        turtle.setheading(self.startangle)
        turtle.pendown()
        returnpoints = list()
        returnangle = list()
        for ch in self.axiom:
            if (ch == "+"):
                turtle.left(self.angle)
            if (ch == "-"):
                turtle.right(self.angle)
            #if (ch.isalpha()):
            if (ch == "F"):
                turtle.forward(self.length)
            if (ch == "["):
                returnpoints.append(turtle.pos())
                returnangle.append(turtle.heading())
            if (ch == "]"):
                turtle.penup()
                turtle.goto(returnpoints.pop())
                turtle.setheading(returnangle.pop())
                turtle.pendown()
        turtle.Screen().update()
        turtle.screensize(5000,5000)
        turtle.exitonclick()

