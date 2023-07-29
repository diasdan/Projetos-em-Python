import random, string

length = 16 #tamanho da senha - 16 número indicado na segurança da informação

chars = string.ascii_letters + string.digits + 'ç~^!@#$%&*()+=_-;:><?' #letras maiusculas e minusculas + digitos + caracteres especiais

rnd = random.SystemRandom() # utiliza outra biblioteca, a biblioteca os, a classe urandom, que gera numero aleatórios através de fontes fornecidas pelo SO

print(''.join(rnd.choice(chars) for i in range(length))) #o rnd choice vai gerar um caractere aleatório, e para cada um o for irá gera um caractere aleatório

