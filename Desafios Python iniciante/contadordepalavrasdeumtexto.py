def contar_palavras(texto):
    palavras = texto.lower().split()
    contagem = {}

    for palavra in palavras:
        palavra = palavra.strip(",.!?;")
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    for palavra, frequencia in contagem.items():
        print(f"{palavra}: {frequencia}")

texto = input("Digite um texto: ")
contar_palavras(texto)
