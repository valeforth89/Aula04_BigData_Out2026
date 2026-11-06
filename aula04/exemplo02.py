# if <condicao>
#    <identacao> <comando>
# else
#    <identacao> <comando>

# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# == igual   

# Maioridade

ano_nasc = int(input("Informe o ano de nascimento: "))

idade = 2026 - ano_nasc

if idade >= 18:
    print ("Você é maior de idade!")

else:
    print ("Você é menor de idade!")
    
print ("\nPrograma encerrado")