import BasicFunctions as BF
import math

# ADVARSEL. Pls vær sød mod programmet, den fejler hvis man ikke skriver det op på specifik måde, det virker også kun med heltal.
# Generelt er det ikke specielt robust. Så tag svaret den giver med en gran salt. 

def divisions_algoritme(dividend, divisor):
    result = []
    remainder = dividend.copy()
    list_of_remainders = []
    list_of_subtractors = []


    

    while remainder[0][2]>=divisor[0][2]:
        coeffiecient = remainder[0][0]/divisor[0][0]
        variable = remainder[0][1]
        power = remainder[0][2]-divisor[0][2]
        if power == 0:
            variable = ""            

        current_divider = [coeffiecient, variable, power]
        result.append(current_divider)


        current_subtractor = []

        for part in divisor:    
            current_subtractor_part_coeffiecient = current_divider[0]*part[0]
            current_subtractor_part_variable = part[1] or current_divider[1]
            current_subtractor_part_power = current_divider[2]+part[2]
            current_subtractor.append([current_subtractor_part_coeffiecient, current_subtractor_part_variable, current_subtractor_part_power])
        list_of_subtractors.append(current_subtractor)

        new_remainder = []
        current_remainder_part = [0, "", 0]
        found_equavilant_power = False

        for subtractor_part in current_subtractor:
            for remainder_part in remainder:
                if remainder_part[2] > subtractor_part[2]:
                    new_remainder.append(remainder_part.copy())
                    remainder.remove(remainder_part)

                if subtractor_part[2] == remainder_part[2]:
                    found_equavilant_power = True

                    current_remainder_part[0] = remainder_part[0]-subtractor_part[0]
                    current_remainder_part[1] = remainder_part[1]
                    current_remainder_part[2] = remainder_part[2]
                    if current_remainder_part[0] != 0:
                        new_remainder.append(current_remainder_part.copy())

                    remainder.remove(remainder_part)
                    
            
                    break
            
            if not found_equavilant_power:
                current_remainder_part[0] = -subtractor_part[0]
                current_remainder_part[1] = subtractor_part[1]
                current_remainder_part[2] = subtractor_part[2]
                new_remainder.append(current_remainder_part.copy())

            found_equavilant_power = False

        for remainder_part in remainder:
            new_remainder.append(remainder_part)

        if new_remainder == []:
            remainder = [[0, '', 0]]
        else:
            remainder = new_remainder
        
        list_of_remainders.append(remainder.copy())
        
        # print("Result", result)
        # print("Subtractor", current_subtractor)
        # print("Remainder", remainder)
        # print()

    # print(result)
    # print(list_of_subtractors)
    # print(list_of_remainders)


    # LaTeX

    print("\\begin{align*}")
    print(f"{BF.convert_to_readable_function(divisor, True)}\\rfloor {BF.convert_to_readable_function(dividend, True)}\\lfloor {BF.convert_to_readable_function(result, True)} \\\\")
    for subtractor, remainder in zip(list_of_subtractors, list_of_remainders):
        print(f"{BF.convert_to_readable_function(subtractor, True)} \\\\")
        print("\\hline")
        print(f"{BF.convert_to_readable_function(remainder, True)} \\\\")
    print("\\end{align*}")

    print()
    print()

    # Advanced LaTeX

    print("Husk at tilføj denne newcommand hvis ikke allerede gjort: ")
    print("\\newcommand\\ldiv[3]{")
    print("\\underline{\\smash{#1}\\hspace{.1em}}\\hspace{-.135em}\\raise.22ex\\hbox{\\textbf{\\(|\\)}} \\ \\  #2 \\ \\  \\raise.22ex\\hbox{\\(|\\)} \\hspace{-.135em}\\underline{\\smash{\\hspace{.1em} #3}}}")
    print()
    print()
    align_at_length = 100
    print(f"\\begin{{alignat*}}{{{align_at_length}}}")
    first_line = f"\\ldiv{{{BF.convert_to_readable_function(divisor, True)}}}"
    first_line += "{"

    higest_power = dividend[0][2]

    first_line += add_and_signs(dividend, higest_power)

    first_line += "&}"
    first_line += f"{{{BF.convert_to_readable_function(result, True)}}} \\\\"
    print(first_line)

    end_of_cmid = (higest_power+1)*3+1
    for subtractor, remainder in zip(list_of_subtractors, list_of_remainders):
        print(f"{add_and_signs(subtractor, higest_power)} \\\\")
        start_of_cmid = end_of_cmid-1 - subtractor[0][2]*3
        print(f"\\cmidrule{{{start_of_cmid}-{end_of_cmid}}}")
        remainder_line = f"{add_and_signs(remainder, higest_power)}"
        if remainder != list_of_remainders[-1]:
            remainder_line += " \\\\"
        print(remainder_line)
    print("\\end{alignat*}")


def add_and_signs(function, higest_power):
    new_function = ""
    numbers = "0123456789"
    first_part_here = True
    power_i = higest_power

    for part in function:
        while part[2] != power_i and power_i >= 0:
            new_function += "&&& "
            power_i-=1
            

        power_i-=1
        readable_part = BF.convert_to_readable_function([part], first_part=first_part_here)
        first_part_here = False
        and_signs_printed = 0

        if readable_part.find("+") != -1:
            readable_part = BF.insert_into_string(readable_part, "&", readable_part.find("+"))
            and_signs_printed += 1
        elif readable_part.find("-") != -1:
            readable_part = BF.insert_into_string(readable_part, "&", readable_part.find("-"))
            and_signs_printed += 1
        
        for char, i in zip(readable_part, range(len(readable_part))):
            if part[1] == "":
                if char in numbers:
                    readable_part = BF.insert_into_string(readable_part, "&"*(3-and_signs_printed), i)
                    and_signs_printed = 3
                    break
            else:
                if char == part[1] and part[1] != "":
                    break
                if char in numbers:
                    readable_part = BF.insert_into_string(readable_part, "&"*(2-and_signs_printed), i)
                    and_signs_printed = 2
                    break

        
        if part[1] != "":
            readable_part = BF.insert_into_string(readable_part, "&"*(3-and_signs_printed), readable_part.find(part[1]))


        new_function+=f"{readable_part} "
    return new_function
input_dividend = input("Input dividend:\n")
input_divisor = input("Input: divisor:\n")
# input_dividend = "Z^5-3Z^4+Z^3+4"
# input_divisor = "Z^2-3Z+2"

input_dividend = BF.convert_to_function(input_dividend)
input_divisor = BF.convert_to_function(input_divisor)

divisions_algoritme(input_dividend, input_divisor)


