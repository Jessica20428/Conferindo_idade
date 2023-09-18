#Conferindo_idade.py

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print(f'{nome} tem {idade} anos é maior de idade.')
else:
    print(f'{nome} tem {idade} anos é menor de idade.')