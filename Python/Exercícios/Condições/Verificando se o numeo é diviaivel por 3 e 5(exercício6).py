#Variáveis
numero = int(0);
resultadopor3 = int(0);
resultadopor5 = int(0);

#input
numero = int(input('digite um número: '))

#processamento
resultadopor3 = numero%3;
resultadopor5 = numero%5;

#saída de dados
if (resultadopor3 == 0):
    print('é divisível por 3');
else:
    print('não é divisível por 3');

if (resultadopor5 == 0):
    print('é divisível por 5');
else:
    print('não é divisível por 5');

if (resultadopor3 == 0 and resultadopor5 == 0):
    print('é divisível por 3 e 5');
else:
    print('não é divisível por 3 e 5');