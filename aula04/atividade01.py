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

# Desconto

# Entrada
valor = float(input("Informe o valor da compra: R$ "))

#Processamento

# Saída
if valor > 250:
    desconto = float(valor * 0.16)
    valor_final = float(valor - desconto)
    print (f"O valor com desconto aplicado ficou em: R$ {valor_final:.2f}!")

else:
    print (f"O valor da compra foi: R$ {valor:.2f}")