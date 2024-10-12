import math

def addPadding(word, length):
    word=str(word)
    padding = length-len(word)
    return " " * math.floor(padding/2) + word + " " * math.ceil(padding/2)

Extended = True
PrintInPython = True
PrintForLaTeX = True



num1 = int(input("First number: "))
num2 = int(input("Second number: "))

i = [0]

r_i = [max(num1, num2)]
r_iPlus1 = [min(num1, num2)]

q_iPlus1 = []
r_iPlus2 = []

s_i = [1, 0]
t_i = [0, 1]

currenti = 0
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

maxiLength=max(len("i"),len(str(i[-1])))

maxr_iLength=max(len("r_i"), len(str(r_i[0]))) 

maxr_iPlus1Length=max(len("r_i+1"),len(str(r_iPlus1[0])))  

maxq_iPlus1Length = len("q_i+1")
for number in q_iPlus1:
    maxq_iPlus1Length = max(maxq_iPlus1Length, len(str(number)))

maxr_iPlus2Length=max(len("r_i+2"),len(str(r_iPlus2[0])))  


maxs_iLength = len("s_i")
for number in s_i:
    maxs_iLength = max(maxs_iLength, len(str(number)))

maxt_iLength = len("t_i")
for number in t_i:
    maxt_iLength = max(maxt_iLength, len(str(number)))




if PrintInPython:
    if Extended:
        print("_"*(maxiLength+maxr_iLength+maxr_iPlus1Length+maxr_iPlus2Length+maxq_iPlus1Length+maxs_iLength+maxt_iLength+3*7+1))
        print(f"\033[4m| {addPadding("i", maxiLength)} | {addPadding("r_i",maxr_iLength)} | {addPadding("r_i+1",maxr_iPlus1Length)} | {addPadding("q_i+1",maxq_iPlus1Length)} | {addPadding("r_i+2", maxr_iPlus2Length)} | {addPadding("s_i",maxs_iLength)} | {addPadding("t_i",maxt_iLength)} |\033[0m")
    else:
        print("_"*(maxiLength+maxr_iLength+maxr_iPlus1Length+maxr_iPlus2Length+maxq_iPlus1Length+3*5+1))
        print(f"\033[4m| {addPadding("i", maxiLength)} | {addPadding("r_i",maxr_iLength)} | {addPadding("r_i+1",maxr_iPlus1Length)} | {addPadding("q_i+1",maxq_iPlus1Length)} | {addPadding("r_i+2", maxr_iPlus2Length)} |\033[0m")
    for index in i:
        indexWithPadding = addPadding(index, maxiLength)
        r_iWithPadding = addPadding(r_i[index], maxr_iLength)
        r_iPlus1WithPadding = addPadding(r_iPlus1[index], maxr_iPlus1Length)
        q_iPlus1WithPadding = addPadding(q_iPlus1[index], maxq_iPlus1Length)
        r_iPlus2WithPadding = addPadding(r_iPlus2[index], maxr_iPlus2Length)
        s_iWithPadding = addPadding(s_i[index], maxs_iLength)
        t_iWithPadding = addPadding(t_i[index], maxt_iLength)

        if Extended:
            print(f"\033[4m| {indexWithPadding} | {r_iWithPadding} | {r_iPlus1WithPadding} | {q_iPlus1WithPadding} | {r_iPlus2WithPadding} | {s_iWithPadding} | {t_iWithPadding} |\033[0m")
        else:
            print(f"\033[4m| {indexWithPadding} | {r_iWithPadding} | {r_iPlus1WithPadding} | {q_iPlus1WithPadding} | {r_iPlus2WithPadding} |\033[0m")
    
    print()


if PrintForLaTeX:
    if Extended:
        print("\\begin{tabular}{|c|c|c|c|c|c|c|}")
        print("\\hline")
        print("    i & $r_i$ & $r_{i+1}$ & $q_{i+1}$ & $r_{i+2}$ & $s_{i}$ & $t_{i}$ \\\\")
        print("\\hline")
        for index in i:
            print(f"    {index} & {r_i[index]} & {r_iPlus1[index]} & {q_iPlus1[index]} & {r_iPlus2[index]} & {s_i[index]} & {t_i[index]} \\\\")
            print("\\hline")
        print("\\end{tabular}")
        print()
    else:
        print("\\begin{tabular}{|c|c|c|c|c|}")
        print("\\hline")
        print("    i & $r_i$ & $r_{i+1}$ & $q_{i+1}$ & $r_{i+2}$ \\\\")
        print("\\hline")
        for index in i:
            print(f"    {index} & {r_i[index]} & {r_iPlus1[index]} & {q_iPlus1[index]} & {r_iPlus2[index]}\\\\")
            print("\\hline")
        print("\\end{tabular}")
        print()


