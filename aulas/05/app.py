
print(int('5')) # converte a string '5' para o número inteiro 5
print(int(10.3)) # converte o número decimal 10.3 para o número inteiro 10 (arredondando para baixo)
print(float('10')) # converte a string '10' para o número decimal 10.0
print(float(1)) # converte o número inteiro 1 para o número decimal 1.0
print(str(1)) # converte o número inteiro 1 para a string '1'
print(bool(1)) # converte o número inteiro 1 para o valor booleano True
print(bool(0)) # converte o número inteiro 0 para o valor booleano False
print(bool('')) # converte a string vazia '' para o valor booleano False
print(bool('abc')) # converte a string 'abc' para o valor booleano True

ano = input('Ano:')

print(type(ano))

idade = 2026 - int(ano)

print('gabriel tem' + idade + ' anos')
