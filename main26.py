'''
Function (Funções);
Parâmetro --> Argumento;
Default = Aquele que você define o valor no parâmetro;
Non-Default = Aquele que você não define o valor no parâmetro.

'''

def boas_vindas(quantidade, nome='Linda'):
    print(f'Ólá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas(6)

