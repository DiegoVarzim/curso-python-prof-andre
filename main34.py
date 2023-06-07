# Unpacking Lists
#  Armazenar mais de uma informação em variáveis
#  Manter a sequência dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 4, 5, 6, 7]

item1, item2, *outros, item3 = produtos



print(item1)
print(item2)
print(item3)
print(outros)
