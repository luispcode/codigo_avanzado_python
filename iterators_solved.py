import time

class FiboIter():
    userlimit = int(input("Ingrese el limite de iteraciones: "))
    def __iter__(self, limit = userlimit ):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        self.limit = limit
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif self.counter == self.limit:
            raise StopIteration
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux #variable swapping.
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
            print(element)
            time.sleep(0.05)

    #Una solucion alternativa podria ser romper el ciclo usando break, cuando se obtenga un resultado de la secuencia 
    # determinado por el usuario al crear el loop for de la siguiente manera:

#  fibonacci = FiboIter()
#     userlimit = int(input("Ingrese el valor limite de la secuencia: "))
#     for element in fibonacci:
#         if element >= userlimit:
#             break
#         else:
#             print(element)
#             time.sleep(0.05)