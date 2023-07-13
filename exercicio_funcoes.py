# 1ª questão
print('Escreva uma função que receba dois números e retorne a soma deles')
print()

def soma():
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    return (f'O resultado da soma é {a+b}')

resultado_soma = soma()
print(resultado_soma)

print()
print('*'*50)
print()

# 2ª questão

print('Escreva uma função que receba uma temperatura em graus Celsius\n\
e retorne a temperatura equivalente em graus Fahrenheit')
print()

def temperatura():
    t = float(input('Digite uma temperatura em Celsius: '))
    return (f'A temperatura em Fahrenheit é {t*1.8 + 32} graus') 

resultado_temp = temperatura()
print(resultado_temp)

print()
print('*'*50)
print()

# 3ª questão

print('Escreva uma função que verifique se um número é par')
print()

def par():
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        return f"{numero} é par"
    return f"{numero} é impar"

resultado_par = par()
print(resultado_par)

print()
print('*'*50)
print()

# 4ª questão

print('Escreva uma função que receba uma lista de números\n\
e retorne o maior número dessa lista') 
print()

def lista_1():
    lista = input('Digite a lista de números:')
    lista_separada = lista.split(',')


    lista = []
    for i in lista_separada:
        lista.append(int(i))
    maximo = max(lista)
    return  f'O valor máximo da lista é {maximo}'

valor_maximo = lista_1()
print(valor_maximo)

print()
print('*'*50)
print()

# 5ª questão

print('Escreva uma função que calcule o fatorial de um número')
print()
def fatorial():
    numero = int(input('Digite um número: '))
    y = 1
    for i in range(1, numero + 1):
        y*= i
    return f'O fatorial de {numero} é igual a {y}'

resultado_fatorial = fatorial()
print(resultado_fatorial)

print()
print('*'*50)
print()

#6ª questão


print('Escreva uma função que receba uma string e retorne a mesma string invertida.')
print()

def string():
    palavra = input('Digite uma palavra: ')
    return palavra[::-1]

resultado_str = string()
print(resultado_str)

print()
print('*'*50)
print()

# 7ª questão


print('Escreva uma função que receba uma lista de números\n\
e retorne a média desses números')
print()

def lista_2():
    lista_2 = input('Digite uma lista de números:')
    lista_sep_2 = lista_2.split(',')

    lista = []
    for j in lista_sep_2:
        for j in lista_sep_2:
            lista.append(int(j))
    media =sum(lista) / len(lista)
    return f'A média dos valores da lista é {media}'


resultado_lista_2 = lista_2()
print(resultado_lista_2)

print()
print('*'*50)
print()

# 8ª questão


print('Escreva uma função que receba uma lista de strings e retorne a quantidade\n\
de strings que possuem mais de cinco caracteres')
print()

def contador():
    lista_str = input('Digite uma lista de palavras: ')
    lista_sep_str = lista_str.split(',')

    lista_completa_str = []
    for s in lista_sep_str:
        lista_completa_str.append(s)
    
    c = 0
    for string in lista_completa_str:
        if len(string) > 5:
            c += 1
    return f'Existem {c} palavras com mais de 5 letras na lista.'

quantidade = contador()
print(quantidade)

print()
print('*'*50)
print()

# 9ª questão

print('Escreva uma função que receba uma lista de números e retorne uma nova lista\n\
       contendo apenas os números pares.')
print()

def lista_3():
    lista_3 = input('Digite uma lista de número: ')
    lista_sep_3 = lista_3.split(',')

    lista = []
    for n in lista_sep_3:
        lista.append(int(n))
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return f'A lista de números pares da lista informada é {lista_pares}'


lista_pares = lista_3()
print(lista_pares)






