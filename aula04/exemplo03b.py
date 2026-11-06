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

# Maioridade


pontuacao = int(input("Informe a pontuação do jogador: "))



# exemplo?: 100 pontos "da erro" pq faz duas verificações e trata as duas pq os IF são independentes

if pontuacao >= 100:
    pontuacao = pontuacao + 10
    print (f"Excelente! Você tem: {pontuacao} pontos!")

if pontuacao >= 50:
    pontuacao = pontuacao + 5
    print (f"Bom desempenho! Você tem {pontuacao} pontos!")

else:
    print (f"Baixo desempenho! Você tem {pontuacao} pontos :(")