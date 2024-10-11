def vogais(texto: str) -> dict[str, int]:
    qtd_vogais = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for letra in texto:
        if letra.lower() in qtd_vogais.keys():
            qtd_vogais[letra.lower()] += 1

    return qtd_vogais


frase = input('Digite uma frase: ')
qtd_vogais = vogais(frase)

# Iterando Dicionário
for k, v in qtd_vogais.items():
    print(f'A quantidade de "{k}" é {v}')