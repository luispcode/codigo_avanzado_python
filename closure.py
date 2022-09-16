"""
Reglas para encontrar un closure:

•debemos tener una nested function
•la nested function debe referenciar un valor de un scope superior
•la función que envuelve la nested debe retornarla también

Se usan cuando:

cuando tenemos una clase que tiene solo un método
cuando trabajamos con decoradores """

def make_multiplier(x):

  def multiplier(n):
    return x * n

  return multiplier


times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))