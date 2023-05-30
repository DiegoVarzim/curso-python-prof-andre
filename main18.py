#  Enviar um e-mail com os detalhes da compra online (Máximo 3 tentativas) para compras confirmadas.

compra_confirmada = False
dados_compra = 'Compra no valor de R$ 12.50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviada para o seu e-mail')
        break
else:
    print('Falha na compra')
