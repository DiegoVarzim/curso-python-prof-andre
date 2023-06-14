# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instâncias)
    #  Classes são utilizadas para agrupar dados e funções, podendo reutilizar.

#  -----

# Class: Frutas
#  Objects: Abacate, Banana...


#  Criar a classe (CONSTRUCTOR)
class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
  
#  criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Diego', 'Varzim', '15/01/2009')
usuario3 = Funcionarios('Júlia', 'Lemos', '10/01/2009')


# print
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)





# #  criar os parâmetros do usuario1
# usuario1.nome = 'Elena'
# usuario1.sobrenome = 'Cabral'
# usuario1.data_nascimento = '12/01/2009'

# #  criar os parâmetros do usuario2
# usuario2.nome = 'Diego'
# usuario2.sobrenome = 'Varzim'
# usuario2.data_nascimento = '15/01/2009'




