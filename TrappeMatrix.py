import numpy as np
import printLibrary as PL
from BasicFunctions import Fraction, convert_np_array_to_fraction
def ref(A, total_matrix_shape = (0, 0), first_run = True, set_matrix = np.array(()), TeX = False, result_matrix_line = False):

    if first_run:
        A = convert_np_array_to_fraction(A)
    if first_run:
        total_matrix_shape = A.shape

    A_height, A_width = A.shape

    non_zero_count = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i, j] != 0:
                non_zero_count += 1
    
    # if np.count_nonzero(A) == 0
    if non_zero_count == 0:
        return A
    

    if A_height == 1:
        for i in A[0]:
            if i != 0:
                first_nonzero = i
                break

        if first_nonzero != 1:
            new_A = A / first_nonzero
            step = PL.printMatrix(try_concatenate(set_matrix, A), True, result_matrix_line)
            step += "\n\\begin{array}{c}"
            step += "\n\\longrightarrow \\\\"
            step += f"\nR_{{{total_matrix_shape[0]}}}\\leftarrow R_{{{total_matrix_shape[0]}}}/{first_nonzero.return_latex_str()}"
            step += "\n\\end{array}"
            step += "\n" + PL.printMatrix(try_concatenate(set_matrix, new_A), True, result_matrix_line)
            if TeX:
                print(f"$$\n{step}\n$$")
            else:
                print(f"\\[\n{step}\n\\]")

            return new_A
        
        return A
    

    first_nonzero_found = False
    for column_index in range(A_width):
        for row_index in range(A_height):
            if A[row_index, column_index] != 0:
                first_nonzero_position = {"row": row_index, "column": column_index}
                first_nonzero_found = True
                break
        if first_nonzero_found:
            break
                

    B = np.array([A[first_nonzero_position["row"]]])
    first_row = A[0]
    for i in range(1 , len(A)):
        if i == first_nonzero_position["row"]:
            B = np.concatenate((B, [first_row]))
            continue

        B = np.concatenate((B, [A[i]]))


    
    if first_nonzero_position["row"] != 0:
        step = PL.printMatrix(try_concatenate(set_matrix, A), True, result_matrix_line)
        step += "\n\\begin{array}{c}"
        step += "\n\\longrightarrow \\\\"
        step += f"\n R_{{1}} \\leftrightarrow R_{{{first_nonzero_position["row"] + 1}}}"
        step += "\n\\end{array}"
        step += "\n" + PL.printMatrix(try_concatenate(set_matrix, B), True, result_matrix_line)
        if TeX:
            print(f"$$\n{step}\n$$")
        else:
            print(f"\\[\n{step}\n\\]")

    
    b = B[0, first_nonzero_position["column"]]
    old_B = B.copy()
    B[0] = B[0] / b


    if b != 1:
        step = PL.printMatrix(try_concatenate(set_matrix, old_B), True, result_matrix_line)
        step += "\n\\begin{array}{c}"
        step += "\n\\longrightarrow \\\\"
        step += f"\nR_{{{total_matrix_shape[0]-A_height+1}}}\\leftarrow R_{{{total_matrix_shape[0]-A_height+1}}}/{b.return_latex_str()}"
        step += "\n\\end{array}"
        step += "\n" + PL.printMatrix(try_concatenate(set_matrix, B), True, result_matrix_line)
        if TeX:
            print(f"$$\n{step}\n$$")
        else:
            print(f"\\[\n{step}\n\\]")


    first_row = B[0]
    old_B = B.copy()
    non_zero_b_found = False
    step = PL.printMatrix(try_concatenate(set_matrix, old_B), True, result_matrix_line)
    step += "\n\\begin{array}{c}"
    step += "\n\\longrightarrow"
    for row in range(1, A_height): #Skips first row
        b = B[row, first_nonzero_position["column"]]
        if b == 0:
            continue
        if b.denominator != 1 and non_zero_b_found:
            step += "\\\\ \n\\vspace{-1.1em}"
        non_zero_b_found = True
        
        B[row] = B[row] - B[0] * b
        


        fortegn = "-"
        if b < 0:
            fortegn = "+"
        if b == 1 or b == -1:
            step += f"\\\\ \nR_{{{row + total_matrix_shape[0] - A_height + 1}}}\\leftarrow R_{{{row + total_matrix_shape[0] - A_height + 1}}} {fortegn} R_{{{total_matrix_shape[0]-A_height+1}}}"
        else:
            step += f"\\\\ \nR_{{{row + total_matrix_shape[0] - A_height + 1}}}\\leftarrow R_{{{row + total_matrix_shape[0] - A_height + 1}}} {fortegn} {b.abs().return_latex_str()}R_{{{total_matrix_shape[0]-A_height+1}}}"
            if b.denominator != 1:
                step += "\\\\ \n\\vspace{-1.1em}"

    if non_zero_b_found:
        step += "\n\\end{array}"
        step += "\n" + PL.printMatrix(try_concatenate(set_matrix, B), True, result_matrix_line)
        if TeX: 
            print(f"$$\n{step}\n$$")
        else:
            print(f"\\[\n{step}\n\\]")

    set_matrix = try_concatenate(set_matrix, np.array([first_row]))

    C = B[1:]
    C = ref(C, total_matrix_shape=total_matrix_shape, first_run=False, set_matrix=set_matrix, TeX=True, result_matrix_line=result_matrix_line) 
    
    return np.vstack([first_row, C]) 

def reduced_ref(A, TeX = False, result_matrix_line = False):
    
    A = ref(A, TeX = TeX, result_matrix_line=result_matrix_line)
    print("Over er den på trappeform")
    print()
    A_height, A_width = A.shape

    pivot_count = 0
    for column_index in range(A_width):
        one_found = False
        old_A = A.copy()
        step = PL.printMatrix(old_A, True, result_matrix_line)
        step += "\n\\begin{array}{c}"
        step += "\n\\longrightarrow"

        column_changed = False
        for row_index in range(A_height):
            reversed_row_index = A_height-row_index-1
            if reversed_row_index < pivot_count and not one_found:
                continue
            if A[reversed_row_index, column_index] == 1 and not one_found:
                one_found = True
                one_index = reversed_row_index
                pivot_count += 1
                continue
            if not one_found:
                continue
            current_to_be_removed = A[reversed_row_index, column_index]
            
            if current_to_be_removed != 0:
                if current_to_be_removed.denominator != 1 and column_changed:
                    step += "\\\\ \n\\vspace{-1.1em}"
                column_changed = True
                A[reversed_row_index] -= A[one_index]*current_to_be_removed

                fortegn = "-"
                if current_to_be_removed < 0:
                    fortegn = "+"
                if current_to_be_removed == -1 or current_to_be_removed == 1:
                    step += f"\\\\ \nR_{{{reversed_row_index + 1}}} \\leftarrow R_{{{reversed_row_index + 1}}} {fortegn}R_{{{one_index + 1}}}"
                else:
                    step += f"\\\\ \nR_{{{reversed_row_index + 1}}} \\leftarrow R_{{{reversed_row_index + 1}}} {fortegn}{current_to_be_removed.abs().return_latex_str()}R_{{{one_index + 1}}}"
                    if current_to_be_removed.denominator != 1:
                        step += "\\\\ \n\\vspace{-1.1em}"
        if column_changed:
            step += "\n\\end{array}"
            step += "\n" + PL.printMatrix(A, True, result_matrix_line)
            if TeX:
                print(f"$$\n{step}\n$$")
            else:
                print(f"\\[\n{step}\n\\]")
    print("Over er den på reduceret trappeform")
    print(f"Der er {pivot_count} pivot elementer")
    print()
    return A

def try_concatenate(matrix1, matrix2):
    if matrix1.shape != (0,):
        return np.concatenate((matrix1, matrix2))
    else:
        return matrix2


A = np.array(
    [
        [2,2,0],
        [-1,1,2],
        [0,2,2],
        [0,1,1],
    ])


print("Copy")
print()
reduced_ref(A)
print()
print("End copy")