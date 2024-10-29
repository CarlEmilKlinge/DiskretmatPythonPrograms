import numpy as np
import printLibrary as PL
import BasicFunctions as BF
def ref(A, total_matrix_shape = (0, 0), first_run = True, set_matrix = np.array(())):
    if first_run:
        total_matrix_shape = A.shape

    A_height, A_width = A.shape

    if np.count_nonzero(A) == 0:
        return A
    
    if A_height == 1:

        for i in A[0]:
            if i != 0:
                first_nonzero = i
                first_nonzero = BF.try_parse_int_or_float(first_nonzero)
                break

        new_A = A / first_nonzero
        if not np.all(new_A == A):
            step = PL.printMatrix(try_concatenate(set_matrix, A), True)
            step += "\n\\begin{array}{c}"
            step += "\n\\longrightarrow \\\\"
            step += f"\nR_{{{total_matrix_shape[0]}}}\\leftarrow R_{{{total_matrix_shape[0]}}}/{first_nonzero}"
            step += "\n\\end{array}"
            step += "\n" + PL.printMatrix(try_concatenate(set_matrix, new_A), True)
            print(f"$$\n{step}\n$$")
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
    
    if first_nonzero_position["row"] != 0:
        step = PL.printMatrix(try_concatenate(set_matrix, A), True)
        step += "\n\\begin{array}{c}"
        step += "\n\\longrightarrow \\\\"
        step += f"\n R_{{1}} \\leftrightarrow R_{{{first_nonzero_position["row"] + 1}}}"
        step += "\n\\end{array}"
        step += "\n" + PL.printMatrix(try_concatenate(set_matrix, B), True)
        print(f"$$\n{step}\n$$")

    
    b = B[0, first_nonzero_position["column"]]
    b = BF.try_parse_int_or_float(b)
    old_B = B.copy()
    B[0] = B[0] / b
    if b != 1:
        step = PL.printMatrix(try_concatenate(set_matrix, old_B), True)
        step += "\n\\begin{array}{c}"
        step += "\n\\longrightarrow \\\\"
        step += f"\nR_{{{total_matrix_shape[0]-A_height+1}}}\\leftarrow R_{{{total_matrix_shape[0]-A_height+1}}}/{b}"
        step += "\n\\end{array}"
        step += "\n" + PL.printMatrix(try_concatenate(set_matrix, B), True)
        print(f"$$\n{step}\n$$")


    first_row = B[0]
    for row in range(1, A_height): #Skips first row
        
        b = B[row, first_nonzero_position["column"]]
        b = BF.try_parse_int_or_float(b)
        old_B = B.copy()
        B[row] = B[row] - b * B[0]
        
        if b != 0:
            step = PL.printMatrix(try_concatenate(set_matrix, old_B), True)
            step += "\n\\begin{array}{c}"
            step += "\n\\longrightarrow \\\\"
            fortegn = "-"
            if b < 0:
                fortegn = "+"
            step += f"\nR_{{{row + total_matrix_shape[0] - A_height + 1}}}\\leftarrow R_{{{row + total_matrix_shape[0] - A_height + 1}}} {fortegn} {abs(b)}R_{{{total_matrix_shape[0]-A_height+1}}}"
            step += "\n\\end{array}"
            step += "\n" + PL.printMatrix(try_concatenate(set_matrix, B), True)
            print(f"$$\n{step}\n$$")

    set_matrix = try_concatenate(set_matrix, np.array([first_row]))

    C = B[1:]
    C = ref(C, total_matrix_shape, False, set_matrix) 
    
    return np.vstack([first_row, C]) 

def reduced_ref(A):
    
    A = ref(A)
    print()
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
            old_A = A.copy()
            current_to_be_removed = A[reversed_row_index, column_index]
            current_to_be_removed = BF.try_parse_int_or_float(current_to_be_removed)
            A[reversed_row_index] -= current_to_be_removed*A[one_index]
            
            if current_to_be_removed != 0:

                step = PL.printMatrix(old_A, True)
                step += "\n\\begin{array}{c}"
                step += "\n\\longrightarrow \\\\"
                fortegn = "-"
                if current_to_be_removed < 0:
                    fortegn = "+"
                if current_to_be_removed == -1 or current_to_be_removed == 1:
                    step += f"\nR_{{{reversed_row_index + 1}}} \\leftarrow R_{{{reversed_row_index + 1}}} {fortegn}R_{{{one_index + 1}}}"
                else:
                    step += f"\nR_{{{reversed_row_index + 1}}} \\leftarrow R_{{{reversed_row_index + 1}}} {fortegn}{abs(current_to_be_removed)}R_{{{one_index + 1}}}"

                step += "\n\\end{array}"
                step += "\n" + PL.printMatrix(A, True)
                print(f"$$\n{step}\n$$")
    return A

def try_concatenate(matrix1, matrix2):
    if matrix1.shape != (0,):
        return np.concatenate((matrix1, matrix2))
    else:
        return matrix2


A = np.array(
    [
        [1, 0, 0, 1, 0],
        [-2, 1, 0, 3, 1],
        [4, 1, 1, 0, 2],
        [4, 1, 1, 0, 2]
    ], 
    dtype=float)

reduced_ref(A)