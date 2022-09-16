import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
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
            yield aux

if __name__ == '__main__':

    fibonacci = fibo_gen()
    userlimit = int(input("Ingrese el numero limite de la secuencia: "))
    for element in fibonacci:
        if element >= userlimit:
            break
        else:
            print(element)
            time.sleep(.05)