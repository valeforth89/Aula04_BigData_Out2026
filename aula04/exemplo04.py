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

login = input("Informe o login: ")
senha = input("Informe a senha: ")

if login == "admin" and senha == "1234":
    print ("Login realizado com sucesso!")

else:
    print ("Credencias incorretas!")