# Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().
from random import randint
resultado=[]
for i in range(5):
    nomealu=input(f'aluno{i+1}:')
    not1=randint(0,10)
    not2=randint(0,10)
    med=(not1+not2)/2
    if med>6:
        resul='aprovado'
    elif med>= 3 and med<6:
        resul='recuperação'
    else:
        resul='rerpovado'
    resultado.append(f'aluno:{nomealu}|media:{med}|status:{resul}')
print(resultado)

# Cadastro Seletivo de Candidatos
# Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
# Adicione este Dicionário à lista: candidatos_validos.append(candidato)
candivali=[]
for i in range(5):
    ano=randint(1936,2026)
    idade=2026-ano
    if idade>=18:
        candidato={
         'nome': input('Digite seu nome: '),
        'contato': int(input('Digite seu número de telefone: ')),
        'email': input('Digite seu email: '),
        }
    candivali.append(candidato)
else:
    print('rejeitado')
print(candivali)
