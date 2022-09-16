# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)
         
# Iterando un iterador, estructura interna de un ciclo for.
while True:
    try:
         element = next(my_iter)
         print(element)
    except StopIteration:
         break

"""como construir un iterador"""

class EvenNumbers:
    """Clase que implementa un iterador
    de todos los números pares, o los números
    pares hasta un máximo"""
    def _init_(self, max=None):
        self.max = max
    def _iter_(self):
        self.num = 0
        return self
    def next__(self):
        if not self.max or self.num == self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration