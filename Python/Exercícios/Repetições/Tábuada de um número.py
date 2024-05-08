tabuada = int(0)
numero = int(10)
contador = int(0)

numero = int(input('digite um número: '))

while (contador <= 10):
    tabuada = numero * contador
    print(f'{numero} * {contador} = {tabuada}')
    contador = contador + 1

if (contador > 10):
    print('')
    exit()