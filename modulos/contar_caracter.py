def contar_caracteres(string):
    caracteres_ordenados = sorted(string)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')

# frase = input('Escreva a frase desejada: ')


if __name__ == '__main__':
    contar_caracteres('jorginho')
    print()
    contar_caracteres('pomodoro')

print(contar_caracteres(frase))
