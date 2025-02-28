from random import sample as rs
import time
# números desordenados de 1 a 1000 elementos

class SortAlgorithm:
    # clase que ejecuta 3 métodos distintos de ordenamiento
    def __init__(self):
        self.unorganized = rs(range(0, 1000), 1000)
        self._time_spent = None # Almacena el tiempo de ejecución
        self.chosen_method = '' # Guarda el tipo de algoritmo elegído.
    
    # decorador que mide el tiempo de ejecución de cualquier método.
    def measure_time(func):
        def wrapper(self, *args, **kwargs):
            start = time.time()
            result = func(self, *args, **kwargs)
            end = time.time()
            self._time_spent = end - start  # Guarda el tiempo en la propiedad
            return result
        return wrapper
    
    @measure_time
    def merge_sort(self, data=None):
        """
        Ordena recursivamente la lista usando el algoritmo Merge Sort.
        Si no se pasa una lista, se utiliza self.unorganized.
        """
        self.chosen_method = 'merge sort'
        if data is None:
            data = self.unorganized
        
        # Una lista con 0 o 1 elementos ya está ordenada
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        # Ordenamos recursivamente la parte izquierda y la parte derecha
        left = self.merge_sort(data[:mid])
        right = self.merge_sort(data[mid:])
        # Mezclamos ambas partes ordenadas
        return self.__merge(left, right)
    
    def __merge(self, left, right):
        """
        Función privada que combina dos listas ordenadas en una sola lista ordenada.
        """
        result = []
        i, j = 0, 0
        
        # Mezcla de elementos mientras haya elementos en ambas listas
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Agrega los elementos restantes (si los hay)
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @measure_time
    def counting_sort(self, data=None):
        """
        Ordena la lista usando el algoritmo Counting Sort.
        Si no se pasa una lista, se utiliza self.unorganized.
        """
        self.chosen_method = 'counting sort'
        if data is None:
            data = self.unorganized
        
        if not data:  # Si la lista está vacía, se retorna inmediatamente.
            return data
        
        # Encuentra el valor máximo para definir el rango de conteo.
        max_val = max(data)
        # Inicializa el arreglo de conteos con ceros (desde 0 hasta max_val)
        count = [0] * (max_val + 1)
        
        # Cuenta la ocurrencia de cada número en la lista
        for num in data:
            count[num] += 1
        
        sorted_list = []
        # Construye la lista ordenada según las ocurrencias
        for num, cnt in enumerate(count):
            sorted_list.extend([num] * cnt)
        
        return sorted_list
    
    @measure_time
    def bubble_sort(self, data=None):
        """
        Ordena la lista usando el algoritmo Bubble Sort (ordenamiento por intercambio).
        Si no se pasa una lista, se utiliza una copia de self.unorganized para no modificar el original.
        """
        self.chosen_method = 'bubble sort'
        if data is None:
            data = self.unorganized.copy()  # Se usa una copia para preservar la lista original
        
        n = len(data)
        for i in range(n):
            # Con cada iteración, el mayor valor se desplaza hasta el final
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    # Intercambiar elementos
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
    
    def __str__(self):
        return f'{self.chosen_method} has taken {self._time_spent}'

if __name__ == "__main__":
    unplugged = SortAlgorithm()
    
    # Escoge uno de los siguientes métodos:s
    
    # unplugged.merge_sort()
    
    # unplugged.counting_sort()
    
    unplugged.bubble_sort()
    
    print(unplugged)