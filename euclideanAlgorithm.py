# Setup
import math
import printLibrary as PL
    #euclideanAlgorithm(Extended, PrintInPython, PrintForLaTeX, FirstNumber, SecondNumber)


### ADVARSEL. Har ikke tjekket med edgecases, tror ikke det virker helt korrekt med negative tal.

# Kig i bunden for at ændre settings eller whatever


def main(Extended = True, PrintInPython = True, PrintForLaTeX = True, FirstNumber = 0, SecondNumber = 0):
    i = [0]
    currenti = 0

    r_i = [max(FirstNumber, SecondNumber)]
    r_iPlus1 = [min(FirstNumber, SecondNumber)]

    q_iPlus1 = []
    r_iPlus2 = []

    s_i = [1, 0]
    t_i = [0, 1]

    while True:
        q_iPlus1.append(math.floor(r_i[currenti]/r_iPlus1[currenti]))
        r_iPlus2.append(r_i[currenti]%r_iPlus1[currenti])

        if currenti >= 2:
            s_i.append(s_i[currenti-2]-q_iPlus1[currenti-2]*s_i[currenti-1])
            t_i.append(t_i[currenti-2]-q_iPlus1[currenti-2]*t_i[currenti-1])


        if r_iPlus2[currenti] == 0:
            break
        r_i.append(r_iPlus1[currenti])
        r_iPlus1.append(r_iPlus2[currenti])
        i.append(currenti+1)
        currenti += 1

    if Extended:
        i.append(currenti+1)
        currenti += 1
        s_i.append(s_i[currenti-2]-q_iPlus1[currenti-2]*s_i[currenti-1])
        
        t_i.append(t_i[currenti-2]-q_iPlus1[currenti-2]*t_i[currenti-1])

        r_i.append("")
        r_iPlus1.append("")
        r_iPlus2.append("")
        q_iPlus1.append("")



    # Printing nice table:

    #Lengths, VarNames, Variables
    Variables = [i, r_i, r_iPlus1, q_iPlus1, r_iPlus2]
    VarNamesForPython = ["i", "r_i", "r_i+1", "q_i+1", "r_i+2"]
    VarNamesForLaTeX = ["i", "r_{i}", "r_{i+1}", "q_{i+1}", "r_{i+2}"]

    if Extended:
        Variables += [s_i, t_i]
        VarNamesForPython += ["s_i", "t_i"]
        VarNamesForLaTeX += ["s_{i}", "t_{i}"]

    if PrintInPython:
        PL.printTableInPython(VarNamesForPython, Variables)

    if PrintForLaTeX:
        PL.printTableInLaTeX(Variables, VarNamesForLaTeX)

    
# Start på program

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

main(FirstNumber=num1, SecondNumber=num2)