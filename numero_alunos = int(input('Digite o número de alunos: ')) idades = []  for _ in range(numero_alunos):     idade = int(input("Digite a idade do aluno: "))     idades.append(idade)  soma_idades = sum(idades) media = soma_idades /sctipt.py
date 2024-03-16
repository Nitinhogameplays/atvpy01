quantidade_alunos = int(input('Digite o número de alunos na turma: '))

idades = []
soma_idades = 0

for _ in range(quantidade_alunos):
    idade = int(input("Digite a idade do aluno: "))
    idades.append(idade)

indice = 0
while indice < len(idades):
    soma_idades += idades[indice]
    indice += 1

media_idades = soma_idades / quantidade_alunos

print("A média de idade da turma é:", media_idades)
