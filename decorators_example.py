from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): # la funcion wrapper recibe los argumentos de la funcion que va a envolver
        initial_time = datetime.now()
        func(*args, **kwargs) #funcion y argumentos que va a recibir.
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + "segundos")
    return wrapper

#examples:

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass
random_func()

@execution_time
def suma(a: int, b:int) -> int:
    return a + b
suma (5,5)

@execution_time
def saludo(nombre='Cesar'):
    print("Hola"+ nombre)
saludo("luis")


