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

# Login e Senha

# Entrada

login = input("Informe o login: ")
senha = input("Informe a senha: ")

# Saída

if login == "admin" and senha == "1234":
    print ("Login realizado com sucesso!")

else:
    print ("Credencias incorretas!")