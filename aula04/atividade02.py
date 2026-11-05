# if <condicao>
#    <identacao> <comando>
# else
#    <identacao> <comando>
# elif (else if)

# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# == igual   

# Bônus por desempenho de vendas

# Uma loja deseja premiar seus vendedores de acordo com o valor total de suas vendas.
# O valor do bônus vai ser acrescentado ao salário base do vendedor
#   vendas iguais ou superiores a R$ 1.000,00: bônus de R$ 150,00
#   vendas iguais ou superiores a R$ 500,00: bônus de R$ 75,00
#   vendas inferiores a R$ 500,00: sem bônus
# O programa deverá calcular o valor do bônus, somá-lo ao salário e apresentar o valor total com o bônus, quando aplicável

# Entrada
salario = float(input("Informe o valor do salário: R$ "))
venda = float(input("Informe o valor da venda: R$ "))

#Processamento

# Saída
if venda >= 1000:
    bonus = 150
    sal_bonus = salario + bonus
    print (f"\nBônus de  R$ {bonus} aplicado!")
    print (f"O salário de: R$ {salario}, com o bônus aplicado ficou em: R$ {sal_bonus}!")

elif venda >= 500:
    bonus = 75
    sal_bonus = salario + bonus
    print (f"\nBônus de  R$ {bonus} aplicado!")
    print (f"O salário de: R$ {salario}, com o bônus aplicado ficou em: R$ {sal_bonus}!")

else:
    print (f"\nNão foi aplicado bônus. :(. \nO Salário permanece em: R$ {salario}")