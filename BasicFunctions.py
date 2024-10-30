import math
import numpy as np

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
            current_split[2] = try_parse_int(part[up_location+1:])

            
            current_split[1] = part[up_location-1]

            coeffiecient = try_parse_int(part[:up_location-1])
            if coeffiecient == None:
                if part[:up_location-1] == "-":
                    current_split[0] = -1
                else:
                    current_split[0] = 1
            else:
                current_split[0] = coeffiecient
            super_split_function.append(current_split)
            continue

        number = try_parse_int(part)

        if number == None:
            current_split[1] = part[-1]
            coeffiecient = try_parse_int(part[:-1])
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

def convert_to_readable_function(func, LaTeX = False, first_part = True):
    readable_function = ""
    for part in func:
        coefficient = part[0]
        variable = part[1]
        power = part[2]


        coefficient_int = try_parse_int(coefficient)
        if coefficient_int != None:
            coefficient = coefficient_int
        
        power_int = try_parse_int(power)
        if power_int != None:
            power = power_int

        if coefficient >= 0 and not first_part:
            readable_function += "+"
        first_part = False
        
        if variable == "":
            readable_function += str(coefficient)
            continue
        if coefficient == -1:
            readable_function += "-"
        elif coefficient != 1:
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
        output = int(input)
    except:
        return None
    if input != output:
        return None
    return output
    
def try_parse_int_or_float(input):
    output = try_parse_int(input)
    if input != output:
        output = input
    
    if output == None:
        try:
            return float(input)
        except:
            return None
    return output

class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)


    def __add__(self, number, reduce = True):
       
        if type(number) == Fraction:
            extended_number = number.extend(self.denominator)
            extended_self = self.extend(number.denominator)
            return_fraction = Fraction(extended_self.numerator + extended_number.numerator, extended_self.denominator)
        else:
            return_fraction = Fraction(self.numerator + number * self.denominator, self.denominator)
        if reduce:
            return_fraction = return_fraction.reduce()
        return return_fraction
    
    def __sub__(self, number, reduce = True):
        if type(number) == Fraction:
            extended_number = number.extend(self.denominator)
            extended_self = self.extend(number.denominator)
            return_fraction = Fraction(extended_self.numerator - extended_number.numerator, extended_self.denominator)
        else:
            return_fraction = Fraction(self.numerator - number * self.denominator, self.denominator)

        if reduce:
            return_fraction = return_fraction.reduce()
        return return_fraction

    def __mul__(self, number, reduce = True):
        
        if type(number) == Fraction:
            return_fraction = Fraction(self.numerator * number.numerator, self.denominator * number.denominator)
        else:
            return_fraction = Fraction(self.numerator * number, self.denominator)

        if reduce:
            return_fraction = return_fraction.reduce()
        return return_fraction
    
    def __truediv__(self, number, reduce = True):
        if type(number) == Fraction:
            return_fraction = Fraction(self.numerator * number.denominator, self.denominator * number.numerator)
        else:
            return_fraction = Fraction(self.numerator, self.denominator*number)
        if reduce:
            return_fraction = return_fraction.reduce()
        return return_fraction

    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)

        return_fraction = Fraction(self.numerator/gcd, self.denominator/gcd)
        return return_fraction
        
    def extend(self, number):
        return_fraction = Fraction(self.numerator * number, self.denominator * number)
        return return_fraction

    def return_fraction(self):
        return self.numerator, self.denominator
    
    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"
    
    def return_latex_str(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"\\frac{{{self.numerator}}}{{{self.denominator}}}"

    def return_as_float(self):
        return self.numerator/self.denominator

    def __eq__(self, number):
        if type(number) == Fraction:
            reduced_self = self.reduce()
            reduced_number = number.reduce()
            return reduced_self.return_fraction() == reduced_number.return_fraction()
        return self.return_as_float() == number
    
    def __ne__(self, number):
        if type(number) == Fraction:
            reduced_self = self.reduce()
            reduced_number = number.reduce()
            return reduced_self.return_fraction() != reduced_number.return_fraction()
        return self.return_as_float() != number
    
    def __lt__(self, number):
        if type(number) == Fraction:
            return self.return_as_float() < number.return_as_float()
        return self.return_as_float() < number

    def __gt__(self, number):
        if type(number) == Fraction:
            return self.return_as_float() > number.return_as_float()
        return self.return_as_float() > number
    
    def __le__(self, number):
        if type(number) == Fraction:
            return self.return_as_float() <= number.return_as_float()
        return self.return_as_float() <= number

    def __ge__(self, number):
        if type(number) == Fraction:
            return self.return_as_float() >= number.return_as_float()
        return self.return_as_float() >= number
    
    def abs(self):
        return Fraction(abs(self.numerator), abs(self.denominator))

def convert_to_fraction(number):
    fraction = Fraction(1, 1)

    while try_parse_int(number) == None:
        number*=10
        fraction /= 10
    fraction *= number

    return fraction

def convert_np_array_to_fraction(array):
    output = np.array(
        [
            [Fraction(*convert_to_fraction(array[0][0]).return_fraction())]
        ]
    )
    for i in range(1, len(array[0])):
        if type(array[0][i]) == Fraction:
            output = np.column_stack((output, Fraction(*array[0][i].return_fraction())))
            continue
        output = np.column_stack((output, Fraction(*convert_to_fraction(array[0][i]).return_fraction())))

    for i in range(1, len(array)):
        part = np.array(
            [
                [Fraction(*convert_to_fraction(array[i][0]).return_fraction())]
            ]
        )
        for j in range(1, len(array[i])):
            if type(array[i][j]) == Fraction:
                part = np.column_stack((part, Fraction(*array[i][j].return_fraction())))
                continue

            part = np.column_stack((part, Fraction(*convert_to_fraction(array[i][j]).return_fraction())))
        output = np.concatenate((output, part))
    return output
