from sys import getsizeof

# Generator Expressions

# Uma forma mais rápida para listas, dicionários e etc...
# Menos memória alocada.
# Vamores em bytes.



numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
print(getsizeof(numeros))

print()


numeros = (x * 10 for x in range(1000000))
print(type(numeros))
print(getsizeof(numeros))

