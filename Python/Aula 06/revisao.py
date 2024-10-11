def maior(valores: list[float]) -> float | None:
    '''
    Uma função para retornar o maior valor de uma lista. 
    Retorna "None" caso a lista esteja vazia. 
    '''
    maior_valor = None

    for valor in valores:
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
    
    return maior_valor


print(maior([-5, -7, -12]))
print(maior([54, 76, 87, 98, 56, 86]))
print(maior([]))