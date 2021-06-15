# un petit programme qui cracke un mot de passe

from string import printable
from time import *
from colorama import init, Fore

init()
GREEN = Fore.GREEN # setting up green writing in the shell for when a solution is found
RED = Fore.RED # setting up red writing in the shell for when a solution is not found


mdp = input('Mot de passe?\n')
print('\n')
time_start = time()
guess = 'X' * len(mdp)

for i in range(len(mdp)):
  for char in printable:
    if mdp[i] == char:
      guess = guess[:i] + char + guess[i+1:]
      print(f'{RED}{guess}')
      break
    print(f'{RED}{guess}')
    sleep(.05)

duration = round(time() - time_start)
print(f'\n{GREEN}Mot de passe {mdp} trouvé en {duration} secondes!')
    


