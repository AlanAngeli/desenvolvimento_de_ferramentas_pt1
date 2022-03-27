"""Bibliotecas

random: implementa geradores de números letras e símbolos aleatórios para várias situações

string: implementa operações comuns par strings.

"""

import random
import string

#ou pode ser import random, string

#tamanho = 16 #será de 16 caracteres

tamanho = input('Digite o número de caracteres que você deseja: ')
tamanho = int(tamanho)

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+;:'
#ascii_letter envolve tanto leras maiúsculas quantos minúsculas

rnd = random.SystemRandom() #os.urandom (classe os)

print(''.join(rnd.choice(chars) for i in range(tamanho)))

