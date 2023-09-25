import turtle
from axiom_generator import Lsystem

def main():
    axiom = "A"
    rules = ["A=A-B--B+A++AA+B-","B=+A-BB--B-A++A+B"]
    lsys = Lsystem(0,0,0,10,60,axiom,rules)
    lsys.GenerateNSteps(6)
    lsys.Draw()

if __name__ == "__main__":
    main()