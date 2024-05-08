#variáveis

ano = int(0);
bisexto = int(0);
proximobisexto = int(0)

#input
ano = int(input('digite um ano: '))

#processamento
bisexto = ano % 4;

#saída de dados
if (ano < 0):
    print('invalido')

if (bisexto == 0):
    print(f'{ano} é bisexto')
    proximobisexto = ano + 4;
else:
    print(f'{ano} não é bisexto')
    proximobisexto =  ano - bisexto + 4;

print(f'proximo bisexto é {proximobisexto}')