count = int(1);
InputNumber = int(0);
fatorial = int(1);

print('o algoritmo é: ');

InputNumber = int(input('digite: '));

while (count <= InputNumber ):

    print(f'{fatorial} x {count}');

    fatorial = fatorial * count;

    count = count + 1;

print (f'resultado: {fatorial}')