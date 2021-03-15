#Conversor de número inteiro decimal para binário
#Por Yasmine Lopes
##################

#Ler o número inteiro. Input do usúario 'Digite um número inteiro'
num = int(input('Vamos descobrir o valor binário de um número!? \nDigite um número inteiro...'))
#Converter valores
print('{} quando convertido para binário tem valor igual a {}'.format(num, bin(num)))