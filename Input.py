from TrappeMatrix import reduced_ref, ref
from ChineseRemainder import chinese_remainder, back_substitution
from DivisionsAlgoritme import divisions_algoritme
# from euclideanAlgorithm import euclidean_algorithm

import BasicFunctions as BF
import numpy as np




A = np.array(
    [
        [-2, 4, 0],
        [1, 1, 3]
    ])

print("Copy")
print()
# reduced_ref(A, TeX=True, result_matrix_line=True)
A = [2, 3, 5]
M = [3, 5, 7]
chinese_remainder(A, M)

print()
print("End copy")






# input_dividend = input("Input dividend:\n")
# input_divisor = input("Input: divisor:\n")
# # input_dividend = "Z^5-3Z^4+Z^3+4"
# # input_divisor = "Z^2-3Z+2"

# input_dividend = BF.convert_to_function(input_dividend)
# input_divisor = BF.convert_to_function(input_divisor)

# divisions_algoritme(input_dividend, input_divisor)






# aValues = [2,3,4,5]
# modValues = [2,3,5,7]
# chinese_remainder(aValues, modValues)