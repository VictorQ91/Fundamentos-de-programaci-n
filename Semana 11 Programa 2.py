def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def sort_specific_row(matrix, row_index):
    matrix[row_index] = quick_sort(matrix[row_index])

# Función para imprimir la matriz
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de ejemplo
    matrix = [
        [1, 4, 3, 2],
        [6, 5, 8, 7],
        [9, 0, 2, 3]
    ]

    print("Matriz original:")
    print_matrix(matrix)

    # Ordenar la fila específica (en este caso, la fila 1)
    row_index = 1
    sort_specific_row(matrix, row_index)

    print("\nMatriz con la fila {} ordenada:".format(row_index))
    print_matrix(matrix)