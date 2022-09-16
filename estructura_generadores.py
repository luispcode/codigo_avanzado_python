"""Sugar syntax de los iteradores :

yield es como return pero a diferencia de return no termina la funcion,
sino que pausa la funcion hasta donde estaba ese yield.
la proxima vez que se ejecuta continua con el yield siguiente."""

# Generator expression
my_list = [0,1,4,7,9,10]
my_second_list = [x*2 for x in my_list] 
#las list comprehension guardan toda la lista en memoria para funcionar.
my_second_gen = (x*2 for x in my_list) # es como un iterador pero escrito de manera elegante.
# los Generator expressions utiliza un elemnto de la lista a la vez para funcionar.

def my_gen( ):
    """Un ejemplo de generadores"""
    print('Hello world!')
    n = 0
    yield 
   
    print('Hello heaven!')
    n = 1
    yield n 
    print('Hello hell!')
    n = 2
    yield n
a = my_gen( )
print(next(a)) #Hello world!
print(next(a)) #Hello heaven!
print(next(a)) #Hello hell!
print(next(a)) #StopIteration