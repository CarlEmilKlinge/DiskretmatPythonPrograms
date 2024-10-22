import numpy as np


def ref(A):
    A_height, A_width = A.shape


    if np.count_nonzero(A) == 0:
        return np.zeros((A_height, A_width))
    
    if A_height == 1:

        for i in A[0]:
            if i != 0:
                first_nonzero = i
                break

        return A / first_nonzero 
    

    first_nonzero_found = False
    for column_index in range(A_width):
        for row_index in range(A_height):
            if A[row_index, column_index] != 0:
                first_nonzero_position = {"row": row_index, "column": column_index}
                first_nonzero_found = True
                break
        if first_nonzero_found:
            break
                



    B = np.zeros((A_height, A_width))
    B[0] = A[first_nonzero_position["row"]]
    B[first_nonzero_position["row"]] = A[0]
    for row in range(A_height):
        if row != 0 and row != first_nonzero_position["row"]:
            B[row] = A[row]
    


    b = B[0, first_nonzero_position["column"]]
    B[0] = B[0] / b
    
    first_row = B[0]


    for row in range(1, A_height): #Skips first row
        b = B[row, first_nonzero_position["column"]]
        B[row] = B[row] - b * B[0]


    C = B[1:]
    C = ref(C) 
    
    return np.vstack([first_row, C]) 

def reduced_ref(A):
    
    A = ref(A)
    A_height, A_width = A.shape

    for column_index in range(A_width):
        one_found = False
        for row_index in range(A_height):
            reversed_row_index = A_height-row_index-1
            if A[reversed_row_index, column_index] == 1:
                one_found = True
                one_index = reversed_row_index
                continue
            if not one_found:
                continue
            A[reversed_row_index] -= A[reversed_row_index, column_index]*A[one_index]
            
    return A




A = np.array(
    [
        [1, 0, 0, 1, 0], 
        [-2, 1, 0, 3, 1],
        [5, 0, 1, -4, 1],
        [4, 1, 1, 0, 2]
    ], 
    dtype=float)

print("Original matrix: ")
print(A)
print()

ref_form = ref(A)
print("Matrix on ref form: ")
print(ref_form)

reduced_ref_form = reduced_ref(A)
print("Matrix on reduced ref form: ")
print(reduced_ref_form)