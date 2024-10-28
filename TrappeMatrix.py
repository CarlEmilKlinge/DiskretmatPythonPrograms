import numpy as np
import printLibrary as PL

def ref(A, total_matrix_height = 0, first_run = True):
    A_height, A_width = A.shape
    if first_run:
        total_matrix_height = A_height

    if np.count_nonzero(A) == 0:
        return A
    
    if A_height == 1:

        for i in A[0]:
            if i != 0:
                first_nonzero = i
                break
        
        new_A = A / first_nonzero
        if new_A != A:
            step = PL.printMatrix(A, True)
            step += "\n\\begin{array}{c}"
            step += "\n\\longrightarrow"
            step += f"\nR_{{{total_matrix_height}}}\\leftarrow \\frac{{R_{{{total_matrix_height}}}}}{{{first_nonzero}}}"
            step += "\n\\end{array}"
            step += "\n" + PL.printMatrix(new_A, True)
            
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
    C = ref(C, total_matrix_height, False) 
    
    return np.vstack([first_row, C]) 

def reduced_ref(A):
    
    A = ref(A)
    A_height, A_width = A.shape

    for column_index in range(A_width):
        one_found = False
        for row_index in range(A_height):
            reversed_row_index = A_height-row_index-1
            if A[reversed_row_index, column_index] == 1 and not one_found:
                one_found = True
                one_index = reversed_row_index
                continue
            if not one_found:
                continue
            A[reversed_row_index] -= A[reversed_row_index, column_index]*A[one_index]
            
    return A




A = np.array(
    [
        [-1, 1, -1, -1],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [-10, 10, -10, -10],

    ], 
    dtype=float)

print("Original matrix: ")
print(A)
print()

#ref_form = ref(A)
#print("Matrix on ref form: ")
#print(ref_form)

reduced_ref_form = reduced_ref(A)
print("Matrix on reduced ref form: ")
print(reduced_ref_form)