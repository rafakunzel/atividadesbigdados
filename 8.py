# 1. Controle de Pesca
# Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
# traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
# pagar uma multa de R$ 4,00 por quilo excedente.
# ● O programa deve ler o peso de peixes (em quilos) pescado no dia.
# ● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
# retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
# ● Se o valor da multa retornado for maior que zero, mostre a multa.
# ● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
# pagar."
# ● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
# o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.

def calculomulta(pesototal):
    limite=100
    excesso=pesototal-100
    if excesso>100:
        multa=excesso*4
        print(f'O valor da multa é:{multa}')
    else:
        print('Dentro do limite')

# # Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
# # pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
# # ● Fórmula: IMC = PESO / (ALTURA * ALTURA)
# # ● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
# # os valores e retornará o IMC calculado.
# # ● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
# # valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
# # ○ Valores de Referência:
# # ■ Menor que 18.5: "Abaixo do peso"
# # ■ 18.5 a 24.9: "Peso normal"
# # ■ 25.0 a 29.9: "Sobrepeso"
# # ■ 30.0 ou mais: "Obesidade"
# # ● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura,
# # chamar as duas funções e imprimir o resultado formatado.
def calculoIMC(peso,altura):
    imc=peso/(altura*altura)
    return imc
def classificacao(imc):
    if imc<18.5:
        print('abaixo do peso')
    elif 18.5<imc<24.9:
        print('peso normal')
    elif 25.0<imc<29.9:
        print('sobrepeso')
    else:
        print('obesidade')

n=input('Digite quantas vezes vai repitir loop:')
cont=1
while cont!=n:
    peso=float(input('digite seu peso:'))
    altura=float(input('digite sua altura:'))
    imc=calculoIMC(peso,altura)
    print(imc)
    classfi=classificacao(imc)

# # 3. Conversor de Temperatura
# # Crie um programa que permita ao usuário converter temperaturas entre Celsius e
# # Fahrenheit.
# # ● Função 1: Crie uma função celsius_para_fahrenheit(temp_c) que recebe a
# # temperatura em Celsius e retorna o valor em Fahrenheit.
# # ○ Fórmula: F = (C * 9/5) + 32
# # ● Função 2: Crie uma função fahrenheit_para_celsius(temp_f) que recebe a
# # temperatura em Fahrenheit e retorna o valor em Celsius.
# # ○ Fórmula: C = (F - 32) * 5/9
# # ● O programa principal deve perguntar ao usuário qual conversão ele quer fazer (ex:
# # "1 para C->F" ou "2 para F->C"), pedir o valor, chamar a função correta e mostrar o
# # resultado.
# # Desafio: Criar uma única função que faça qualquer uma das conversões,
# # sempre perguntando ao usuário qual é desejada
    
def celsiusforfahre():
    c=int(input('Digite a temperatura em gruas celsius:'))
    F=(c*(9/5)+32)
    return F
def fahrebheitforcelsus():
    f=int(input('Digite a temperatura em gruas fahrenheit:'))
    C=(f-32)*(5/9)
    return C
def trocadetemp():
    print('digite 1 para fazer a troca de celsius para fahrebheit')
    print('digite 2 para fazer a troca de fahrebheit para celsius')
    num=int(input('Digite 1 ou 2'))
    if num==1:
        def celsiusforfahre():
            c=int(input('Digite a temperatura em gruas celsius:'))
            F=(c*(9/5)+32)
            return F
    else:
        def fahrebheitforcelsus():
            f=int(input('Digite a temperatura em gruas fahrenheit:'))
            C=(f-32)*(5/9)
            return C
# 1. Verificador de Ano Bissexto
# Crie uma função chamada eh_bissexto(ano):
# ● A função deve receber um ano (inteiro) como parâmetro.
# ● Ela deve retornar True (Booleano) se o ano for bissexto, e False caso contrário.
# ● Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
# menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
# e 2100 não são).
# ● No programa principal, peça um ano ao usuário e imprima "O ano X É bissexto" ou
# "O ano X NÃO é bissexto", baseado no retorno da função.

def anobissexto(ano):
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        print(f'{ano} é bissexto')
    else:
        print(f'{ano} não é bissexto')
x=2028
bissext0=anobissexto(x)

# # 2. Contagem de Caracteres
# # Crie uma função chamada contar_caractere(texto, caractere_procurado):
# # ● A função deve receber uma string texto e uma string caractere_procurado (de um só
# # caractere).
# # ● Ela deve retornar o número de vezes que o caractere_procurado aparece no texto.
# # (Não diferencie maiúsculas de minúsculas!)
# # ● Dica: Use um loop for para percorrer o texto e use .lower() para tratar os caracteres.
# # ● No programa principal, peça ao usuário uma frase e uma letra, e mostre o resultado
# # da contagem.
def contcaracter(texto,letra):
    for _ in texto:
        texto.lower
        cont=texto.count(letra)
        return cont

palavras='amarelinha'
letra='a'
contar=contcaracter(palavras,letra)
print(contar)

# 3. Simulador de Dado
# Usando o módulo random, crie uma função rolar_dado(lados).
# ● A função deve receber o número de lados do dado (ex: 6, 10, 20).
# ● Ela deve retornar um número aleatório entre 1 e o número de lados (use
# random.randint(1, lados)).
# ● No programa principal, crie um "simulador de batalha":
# ○ Peça ao usuário para "Rolar para o Ataque (d20)". Chame a função
# rolar_dado(20).
# ○ Peça ao usuário para "Rolar para o Dano (d8)". Chame a função
# rolar_dado(8).
# ○ Imprima os resultados de cada rolagem
from random import randint
def rolardado(lado):
    faces=randint(1,lado)
    return faces
