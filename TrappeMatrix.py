# import numpy as np
# matrix_height = input("Matix height: ")
# matrix_width = input("Matrix width: ")

# matrix = np.zeros((matrix_height, matrix_width))
# print(matrix)
# for i in range(matrix_height):
#     for j in range(matrix_width):
#         matrix[i, j] = input("Write number: ")

# print(matrix)
import numpy as np
def ref(A, count):
    m, n = A.shape
    print(f">>{count}<<")
    print(m, n)
    print(A)
    # Trin 1: Hvis A = 0, returner 0

    if np.count_nonzero(A) == 0:
        return np.zeros((m, n))
    
    # Trin 2: Hvis m = 1 og A != 0, find den mindste søjle j med ikke-nul element
    if m == 1:
        j = np.argmax(A != 0)  # mindste søjleindeks hvor A[0, j] != 0
        print(f"j: {j}")
        return A / A[0, j]  # Del hele rækken med det første ikke-nul element
    
    # Trin 3: Hvis m > 1, find mindste j og i hvor elementet i A[i, j] != 0
    l = 0
    j_found = False
    while not j_found:
        for row in range(m):
            if A[row, l] != 0:
                j_found = True
                j = l
                break
        l+=1

    

    for j in range(n):
        for i in range(m):
            print()
            print(f"i, j: {i, j}")
            if A[i, j] != 0:
                print("break")
                break
        else:
            continue
        break

    # Trin 4: Byt første række med rækken indeholdende det ikke-nul element
    A[[0, i]] = A[[i, 0]]  # R1 ↔ Ri
    
    # Trin 5: Gør det første element i den nye første række til 1
    A[0] = A[0] / A[0, j]  # R1 ← (A[0, j])^(-1) * R1
    
    # Trin 6: Reducér de andre rækker
    for i in range(1, m):
        A[i] = A[i] - A[i, j] * A[0]  # Ri ← Ri − A[i, j] * R1
    
    # Trin 7: Kald rekursivt for under-matricen uden første række
    C = ref(A[1:], count+1)  # Kalder sig selv rekursivt på C (undermatricen)
    
    # Trin 8: Tilføj den reducerede første række tilbage
    print(f">>{count}<<")
    print()
    return np.vstack([A[0], C])  # Tilføj r (første række) øverst i resultatet

# Eksempel:


A = np.array([[1, 3, 4, 1], [0, 4, -4, 0], [-2, 0, -9, -1]], dtype=float)
print("Original matrix: ")
print(A)

print()
result = ref(A, 0)
print("Matrix on ref form: ")
print(result)


