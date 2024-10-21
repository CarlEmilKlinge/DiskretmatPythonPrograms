import math
def printTableInPython(VarNames, Variables):
    print()
    Lengths = _returnMaxLengths(VarNames, Variables)
    totalLength = sum(Lengths)
 
    print("_"*(totalLength+3*len(Variables)+1))

    UnderLineWrapper = ["\033[4m", "\033[0m"]

    firstLine = "".join(f"| {_addPadding(varName, length)} " for varName, length in zip(VarNames, Lengths))
    firstLine += "|"
    firstLine = _wrapText(firstLine, UnderLineWrapper)

    print(firstLine)


    
    # Finds the amount of colums to be printed, does this by seing the length of the first Variable, it assumes they all have the same length
    for index in range(len(Variables[0])):
        MainLine = "".join(f"| {_addPadding(variable[index], length)} " for variable, length in zip(Variables, Lengths))
        MainLine += "|"
        MainLine = _wrapText(MainLine, UnderLineWrapper)
        print(MainLine)

    print()

# The _ in this case just means that its a function that is only really meant to be used by the other real print functions in this file.
def _addPadding(word, length):
    word=str(word)
    padding = length-len(word)
    return " " * math.floor(padding/2) + word + " " * math.ceil(padding/2)

def _returnMaxLengths(VarNames, Variables):
    MaxLengths = []
    for varName, variable in zip(VarNames, Variables):
        currentMaxLength = max(len(varName), max(len(str(value)) for value in variable))
        MaxLengths.append(currentMaxLength)
    return MaxLengths

def _wrapText(text, wrapList):
    startWrap, endWrap = wrapList
    return f"{startWrap}{text}{endWrap}"


def printTableInLaTeX(Variables, VarNames):
    print()
    print("\\begin{tabular}{|" + "c|"*len(Variables) + "}")
    print("\\hline")

    firstline="    "
    for name in VarNames:
        firstline += f"${name}$"
        if name!=VarNames[-1]:
            firstline += " & "

    firstline += " \\\\"
    print(firstline)
    print("\\hline")

    for index in Variables[0]:
        MainLine = "    "
        for var in Variables:
            MainLine += f"{var[index]} "
            if var != Variables[-1]:
                MainLine += "& "
        MainLine += "\\\\"
        print(MainLine)
        print("\\hline")
    print("\\end{tabular}")
    print()