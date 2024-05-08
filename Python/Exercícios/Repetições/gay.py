import os;
import time;

inputnumber = int(1);

print('menu de seleção de algoritmos');
time.sleep(2);

while (inputnumber != 0):
    contador = 10;
    os.sistem('cls');

    print('\n-----------------------');
    print('Menu da seleção');
    print('Digite 1 para acessar a tabuada');
    print('digite 0 para acabar com tudo');

    inputnumber = int(input('Digite: '));

    if (inputnumber == 1):
        print ('/algoritmo da tabuada');

    if (inputnumber == 0):
        print ('\nencerrando. . . . ');
        break;

input ('\naperte ENTER para continuar');
