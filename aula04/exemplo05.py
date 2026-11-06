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
# AND / OR

# Login e Senha

valor = float (input("Valor total da compra: "))
fidelidade = input("Cliente possui fidelidade? (S/N): ").lower()[0]
print (fidelidade)

if valor > 100 or fidelidade == "s":
    print ("Cliente tem direito a um brinde!")

else:
    print ("Sem brinde dessa vez!")