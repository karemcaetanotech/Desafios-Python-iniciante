import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print("Sua senha gerada é:", gerar_senha(12))
