import math
import itertools
import printLibrary as PL
import BasicFunctions as BF




# x \equiv 2 mod 3
# x \equiv 3 mod 6

def chinese_remainder(a_values, mod_values):
    mod_values_choose2 = list(itertools.combinations(mod_values,2))
    if not all(math.gcd(mod, othermod) == 1 for mod, othermod in mod_values_choose2):
        print("Not all pairs of mod values are relatively prime, which is required")
        return
    m = math.prod(mod_values)

    
    M_values = list(int(m/mod) for mod in mod_values)

    yvalues = []
    for mod, M in zip(mod_values, M_values):
        for i in range(mod):
            if M * i % mod == 1:
                yvalues.append(i)

    

    index = list(i for i in range(1, len(a_values)+1))
    
    var_names = ["i", "a_i", "mod_i", "M_i", "y_i"]
    variables = [index, a_values, mod_values, M_values, yvalues]



    PL.printTableInPython(var_names, variables)

    print(f"m = {m}")
    solution = sum((a*M*y for a,M,y in zip(a_values,M_values,yvalues)))
    print()
    print(f"x = {solution} congruent {solution%m} mod {m}")
    print(f"x = {m}*k+{solution%m} for any integer k")
    print(f"x = {solution%m} is the smallest positive integer that is a simultaneous solution")


    print()
    print("LaTeX below")
    print()


    var_names = ["i", "a_i", "\\text{mod}_i", "M_i", "y_i"]

    # Solution table
    whatever = [["i"], ["a_{i}"], ["\\text{mod}_{i}"], ["m/mod_{i}"], ["y_{i}\\cdot M_{i} \\equiv 1 \\text{ mod } a_{i}"]]
    


    print("\\[x = \\sum_{i=1}^{n}  a_1 M_1 y_1 + a_2 M_2 y_2 +...+ a_n M_n y_n\\]")
    print()
    print("\\[x = a_1 M_1 y_1 " + "".join(f"+ a_{i}M_{i}y_{i}" for i in range(2, len(a_values)+1)) + "\\]")
    print("This is the solution table: ")


    PL.printTableInLaTeX(var_names, whatever)
    print()
    print(f"Where $m$ is the product of all $\\text{{mod}}_{{i}}$. In this case m = {m}")
    print()
    print("Putting our numbers into the tabel we get: ")
    
    PL.printTableInLaTeX(var_names, variables)

    print("\\begin{align}")
    print(f"    x &= {a_values[0]}\\cdot{M_values[0]}\\cdot{yvalues[0]} " + "".join(f"+ {a_values[i]}\\cdot{M_values[i]}\\cdot{yvalues[i]}" for i in range(1, len(a_values))) + " \\\\")
    print(f"    x &= {solution}")
    print("\\end{align}")

    print("From this x can be written as: ")
    print(f"\\[x\\equiv{solution%m}\\text{{ mod }}{m}\\]")
    print("From this we see the smallest possible integer solution is:")
    print(f"\\[x={solution%m}\\]")

    print()

        



def back_substitution(a_values, mod_values):
    mod_values_choose2 = list(itertools.combinations(mod_values,2))
    if not all(math.gcd(mod, othermod) == 1 for mod, othermod in mod_values_choose2):
        print("Not all pairs of mod values are relatively prime, which is required")
        return

    print()    
    print("Convert to function using t (0)")
    print("Plug previous into new line function (1)")
    print("Reduce, if relevant, by finding the remainder of the coefficients divided by the current mod value (2)")
    print("Reduce left side by removing the non t term(3)")
    print("Make the right side of congruence positive, if negative, by adding the mod value(4)")
    print("Remove coefficient on the t by finding the inverse and multiplying it on the other side, also do step 2 (5)")
    print("Convert to function using t_+1 (6)")
    print("Plug this into the t from the previous function (7)")
    print("Reduce (8)")
    print()    

    overarching_steps = []

    for i in range(len(a_values)):
        if i == 0: # Step (0)
            t = mod_values[i]
            nott = a_values[i]
            previoust = t
            previousnott = nott 
            substitution = f"{t}t_{i} + {nott}"
            overarching_steps.append([f"x = {substitution} (0)"])
            print(f"x = {substitution} (0)")
            continue

        steps = []

        # Step 1
        steps.append(f"{substitution} congruent {a_values[i]} mod {mod_values[i]} (1)")

        # Step 2
        substitution = f"{t}t_{i-1} + {nott}"
        t = t % mod_values[i]
        nott = nott % mod_values[i]
        
        potential_substitution = f"{t}t_{i-1} + {nott}"
        if potential_substitution != substitution:
            steps.append(f"{potential_substitution} congruent {a_values[i]} mod {mod_values[i]} (2)")
        
        # Step 3
        nextnott = a_values[i]-nott

        steps.append(f"{t}t_{i-1} congruent {nextnott} mod {mod_values[i]} (3)")

        # Step 4
        if nextnott < 0:
            nextnott += mod_values[i]
            steps.append(f"{t}t_{i-1} congruent {nextnott} mod {mod_values[i]} (4)")

        # Step 5
        inverset = BF.findInversion(t, mod_values[i])
        nextnott *= inverset
        nextnott = nextnott % mod_values[i]
        steps.append(f"t_{i-1} congruent {nextnott} mod {mod_values[i]} (5)")

        # Step 6
        nextt = mod_values[i]
        tsubstitution = f"{nextt}t_{i} + {nextnott}"
        steps.append(f"t_{i-1} = {tsubstitution} (6)")
        
        # Step 7
        substitution = f"{previoust}({tsubstitution}) + {previousnott}"

        steps.append(f"x = {substitution} (7)")

        # Step 8
        nextt = previoust*nextt
        nextnott = previoust*nextnott + previousnott
        substitution = f"{nextt}t_{i} + {nextnott}"
        steps.append(f"x = {substitution} (8)")

        # Preparation for next function
        t = nextt
        nott = nextnott
        substitution = f"{t}t_{i} + {nott}"

        previoust = t
        previousnott = nott

        overarching_steps.append(steps)


    print()
    print("Python: ")

    for steps, i in zip(overarching_steps, range(len(overarching_steps))):
        print(f"Beginning with funktion {i}:")
        for step in steps:
            print(step)

        print()
    
    # Conclusion should be printed unless that just is the conclusion idk


    # LaTeX
    print()    
    print()    
    print("LaTeX: ")
    print()    
    print("Convert to equation using $t_{0}$ (0)")
    print()    
    print("Plug previous into new line function (1)")
    print()    
    print("Reduce, if relevant, by finding the remainder of the coefficients divided by the current mod value (2)")
    print()    
    print("Reduce left side by removing the non $t$ term(3)")
    print()    
    print("Make the right side of congruence positive, if negative, by adding the mod value(4)")
    print()    
    print("Remove coefficient on the $t$ by finding the inverse and multiplying it on the other side, also do step 2 (5)")
    print()    
    print("Convert to equation using $t_{+1}$ (6)")
    print()    
    print("Plug this into the $t$ from the previous equation (7)")
    print()    
    print("Reduce (8)")
    print() 

    for steps, i in zip(overarching_steps, range(1, len(overarching_steps)+1)):
        print(f"Equation {i}:")
        print("\\begin{align*}")
        for step in steps:
            step = step.replace("congruent", "\\equiv")
            step = step.replace("mod", "\\text{ mod }")
            step = BF.insert_into_string(step, "\quad ", -3)
            step += " \\\\"
            print(step)
        print("\\end{align*}")
        print()