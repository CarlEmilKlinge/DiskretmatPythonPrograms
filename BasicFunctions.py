def findInversion(a, m):
    for i in range(m):
        if a * i % m == 1:
            return i
    return None

def insert_into_string(text, insert, index):
    return text[:index] + insert + text[index:]


def convert_to_function(func):
    split_function = []
    last_split_location = 0
    for char, i in zip(func, range(len(func))):
        if (char == '+' or char == '-') and i != 0:
            split_function.append(func[last_split_location:i])
            last_split_location = i
    split_function.append(func[last_split_location:])
    super_split_function = []
    for part in split_function:
        current_split = [1, "", 1]
        if "^" in part:
            up_location = part.find("^")
            current_split[2] = try_parse_int_or_float(part[up_location+1:])

            
            current_split[1] = part[up_location-1]

            coeffiecient = try_parse_int_or_float(part[:up_location-1])
            if coeffiecient == None:
                current_split[0] = 1
            else:
                current_split[0] = coeffiecient
            super_split_function.append(current_split)
            continue

        number = try_parse_int_or_float(part)

        if number == None:
            current_split[1] = part[-1]
            coeffiecient = try_parse_int_or_float(part[:-1])
            if coeffiecient == None:
                current_split[0] = 1
            else:
                current_split[0] = coeffiecient
            super_split_function.append(current_split)
            continue
        
        current_split[0] = number
        current_split[2] = 0
        super_split_function.append(current_split)

    return super_split_function

def convert_to_readable_function(func, LaTeX = False):
    readable_function = ""
    first_part = True
    for part in func:
        coefficient = part[0]
        variable = part[1]
        power = part[2]



        coefficient_int = try_parse_int_or_float(coefficient)
        if coefficient_int != None:
            coefficient = coefficient_int
        
        power_int = try_parse_int_or_float(power)
        if power_int != None:
            power = power_int

        if coefficient >= 0 and not first_part:
            readable_function += "+"
        first_part = False
        
        if variable == "":
            readable_function += str(coefficient)
            continue
        if coefficient != 1:
            readable_function += str(coefficient)
        readable_function += variable
        if power >= 2:
            if LaTeX:
                readable_function += "^{" + str(power) + "}"
            else:
                readable_function += f"^{power}"
    return readable_function


def try_parse_int(input):
    try:
        return int(input)
    except:
        return None
    
def try_parse_int_or_float(input):
    output = try_parse_int(input)
    if output == None:
        try:
            return float(input)
        except:
            return None
    return output