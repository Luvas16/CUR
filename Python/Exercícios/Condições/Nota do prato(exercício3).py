#variavel
nota = float(0);
notacorte = float(7);

#input
nota = float(input('digite uma nota para Ratatouile: '))

if (nota >10 or nota < 0):
   print('invalido');
   exit();

#saída de dados
if (nota < notacorte):
   print('chato')
else:
   print('yey');

if (nota == notacorte - 0.5 or notacorte + 0.5):
   print('no limite');