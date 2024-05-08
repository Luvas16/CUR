#Variáveis
numero = float(0);
resultado = float(0);

#input
numero = float(input('digite um número: '))
resultado = numero%2;

#processamento
if (resultado == 0):
    print(f'{numero} é par');

if (resultado != 0):
    print(f'{numero} é impar');

#saída de dados