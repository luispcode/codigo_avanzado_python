import time
def fibo_gen(userlimit: int) -> int:
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            if aux >= userlimit:
                break
            else:
                yield aux

if __name__ == '__main__':

    userlimit = int(input("Ingresa el numero limite de la iteracion: "))
    fibonacci = fibo_gen(userlimit)
    for element in fibonacci:
        print(element)
        time.sleep(.05)