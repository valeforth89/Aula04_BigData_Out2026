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

# Entrada
ano_nasc = int(input("Informe o ano de nascimento: "))

#Processamento

idade = 2026 - ano_nasc



# Saída
if idade >= 18:
    print ("Você é maior de idade!")

else:
    print ("Você é menor de idade!")
    
print ("\nPrograma encerrado")