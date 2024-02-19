"""
Algoritmo burbuja: Consiste básicamente en ordenar un array usando dos bucles y por medio de comparación.
Se comparan los valores de dos elementos para ser ordenados, muy similar a la  función sorted() de python
pero de forma manual.
"""
def ordenadorArray(array:list) -> list:
    n = len(array)
    if n <= 0:
        raise IndexError
    else:
        for i in range(n-1):
            for j in range(n-1-i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array


if __name__ == "__main__":
    try:
        #Entrada
        array = [4,5,8,7,1]
        print(f"Tu array desordenado: {array}")
        #Procesamiento
        array_arreglado = ordenadorArray(array)
        #Salida
        print(f"Array ordenado : {array_arreglado}")
    except:
        print("Error Inesperado.")