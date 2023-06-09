#  Array (Matriz)
#  Utilizar quando tiver uma lista muito grande e com problema de performance.

# Similar as listas
#  Melhor performance


from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]


print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])


print(letras)
print(numeros_i)
print(numeros_f)





