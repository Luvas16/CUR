Inputnumber = int(0)
count = int(0)

numero = int(1)
numeropasssado = int(0)
numerofuturo = int(0)

Inputnumber = int(input('digite: '));

while (count < Inputnumber):

    numerofuturo = numeropassado + numero;

    print(f'{count} // numero: {numerofuturo}');

    numeropassado = numero;
    numero = numerofuturo;

    count = count + 1;

    print(numero);
