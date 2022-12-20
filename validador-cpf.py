import re
import sys
#cpf_usuario = '06447659680'.replace('.' , '')\
#.replace('-', '')\
#.replace(' ','')
entrada = input('CPF: Digite')
cpf_usuario = re.sub(r'[^0-9]','', entrada)
entrada_e_sequencial = entrada == entrada[0] * len(entrada)
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_usuario[:9]
contador_regressivo1 = 10
resultado1 = 0
for digito1 in nove_digitos:
    resultado1+=(int(digito1) * contador_regressivo1)
    contador_regressivo1-=1
digito1 = (resultado1 * 10 % 11)
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)

cpf_usuario = '06447659680'
dez_digitos = cpf_usuario[:9] + str(digito1)
contador_regressivo2 = 11
resultado2 = 0
for digito2 in dez_digitos:
    resultado2+=(int(digito2) * contador_regressivo2)
    contador_regressivo2-=1
digito2 = (resultado2 * 10 % 11)
digito2 = digito2 if digito2 <= 9 else 0
print(digito2)
 
novo_cpf = f'{nove_digitos}{digito1}{digito2}'
print(novo_cpf)

if cpf_usuario == novo_cpf:
    print(f'CPF {novo_cpf} válido')    
else:
    print('CPF inválido')
