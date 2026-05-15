# Você recebeu informações sobre um aluno e precisa gerar uma mensagem automática da plataforma.
nome = "Maria"
sobrenome = "Oliveira"
curso = "python é legal"
frase = 'Ela disse: "Estou aprendendo Python!"'

# Resolva as tarefas abaixo:

# Mostre a primeira letra do nome.
print(f'A primeira letra do nome é: {nome[0]}')
# Mostre a última letra do sobrenome usando índice negativo.
print(f'A última letra do sobrenome é: {sobrenome[-1]}')
# Mostre as 3 primeiras letras do nome usando slice.
print(f'As 3 primeiras letras do nome é: {nome[:3]}')
# Mostre as 4 últimas letras do sobrenome usando slice.
print(f'As 4 últimas letras do sobrenome: {sobrenome[-4:]}')
# Transforme `curso` em letras maiúsculas.
print(f'`curso` em letra maiúscula: {curso.upper()}')
# Verifique se `"Python"` existe dentro de `curso`.
print(f'`"Python"` existe dentro de `curso`: {"Python" in curso} (True = Sim, False = Não)')
# Descubra em qual posição começa a palavra `"legal"` em `curso`.
print(f'Qual posição começa a palavra `"legal"` em `curso`: {curso.find("al")}')
# Troque `"legal"` por `"incrível"` usando `replace()`.
print(curso.replace('legal', 'incrível'))
# Mostre quantos caracteres existem em `curso`.
print(len(curso))
# Crie uma mensagem usando **f-string**: Maria Oliveira está matriculada no curso PYTHON É LEGAL.

# Bonus:
# Sem criar novas variáveis, imprima: "M. Oliveira estuda PYTHON É LEGAL"


print(curso.replace('legal', 'incrível').replace('incrível', 'legal', 1))
# print(curso[:15] +  curso.split('python é legal ')[1].replace('legal', 'incrível'))
