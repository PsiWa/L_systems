from axiom_generator import Lsystem
from os import listdir
from os.path import isfile, join


def main():
    #axiom = "A"
    #rules = ["A=A-B--B+A++AA+B-","B=+A-BB--B-A++A+B","",""]
    rules = []
    setups = {}
    onlyfiles = [f for f in listdir("./Tasks") if isfile(join("./Tasks", f))]
    print(onlyfiles)
    n = input("select X.txt :")
    file = open(f"Tasks/{n}.txt", "r")
    pars=file.read()
    lines = pars.splitlines()
    for line in lines:
        (par,var) = line.split(":")
        if par == "rule":
            rules.append(var)
        else:
            setups[par]=var
    lsys = Lsystem(int(setups["startx"]),int(setups["starty"]),float(setups["startangle"]),int(setups["length"]),float(setups["angle"]),setups["axiom"],rules)
    lsys.GenerateNSteps(int(setups["steps"]))
    lsys.Draw(True,10)

if __name__ == "__main__":
    main()