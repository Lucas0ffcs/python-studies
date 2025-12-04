
'''

ums = [-5, 3, 0, -1, 8, -2, 7]
print(nums)
filtrados = list(filter(lambda x: x > 0, nums))

print("Números de nums maiores que 0: ", filtrados)
'''



#AGORA ESSE DEBAIXO
#ELE FILTRA OS ITENS DESSA LISTA SELECIONANDO SÓ OS DE ATÉ 3 LETRAS
#EU POSSO MUDAR O CRITÉRIO, PARA FILTRAR COM ATÉ 4 LETRAS POR EXEMPLO
# 5 LETRAS
'''nomes = ["Ana", "Beatriz", "João", "Lu", "Carla"]
print(nomes)
nomeCurto = list(filter(lambda x: len(x)<=5, nomes))
print("Nomes em nomes com até 3 letras: ", nomeCurto)'''


#AGORA VOU RESOLVER UM GRAVANDO, PRA VOCE VER
# QUANDO EU FAÇO ISSO DE COLOCAR O CODIGO ENTRE ''' (3 APOSTROFES) ELE DEIXA DE SER CODIGO EXECUTAVEL
# E VIRA SO UM COMENTÁRIO
# O MESMO VALE PRA QUANDO TEM ESSE JOGO DA VELHA

#VAMOS PRO PROXIMO EXERC DO GPT

#________________________________


#O GPT FORNECEU UMA LISTA DE PALAVRAS
palavras = ["Abacate", "banana", "Ameixa", "laranja", "abóbora", "Azazel", "Aralho da leandrinha"]

#TENHO QUE CRIAR UMA NOVA LISTA QUE VAI RECEBER OS VALORES FILTRADOS, SÓ O QUE COMEÇA COM "A"
#O NOME DA LISTA VAI SER "comecaA" PORQUE COMEÇA COM "A"

comecaA = list(filter(lambda x: x[0] == "a" or x[0] == "A", palavras))
#ESSA PRIMEIRA PARTE ESTRUTURA TO_DO O DESAFIO
#FUNCIONA ASSIM: LAMBDA É UMA FUNÇÃO QUE VAI RECEBER UM VALOR COMO "X", E DEPOIS DOS ":', ESTÁ A DEFINIÇÃO DO QUE
# A LAMBDA DEVE FAZER COM ESSE X
#x[0] == "a" or x[0] == "A": SIGNIFICA QUE ELE VAI PEGAR A PRIMEIRA LETRA DE X, OU SEJA, X É UMA STRING(PALAVRA/TEXTO),
# X[0] SERIA O PRIMEIRO INDICE DE X, POR EXEMPLO: SE X = "PERA", X[0] = "P", X[1] = "E", X[2] = "R", X[3] = "A",
# X TEM 4 LETRAS MAS AO INVES DE COMEÇAR NO 1 E IR ATÉ O 4, COMEÇA NO 0 E VAI ATE 3.

#AGORA É SO COLOCAR A LISTA JUNTO
#PRONTO: filter(lambda x: x[0] == "a" or x[0] == "A", palavras): ISSO AQUI FAZ COM QUE CADA ITEM DA LISTA palavras,
# que são de fato palavras(poderia criar uma lista chamada palavras que é composta de numeros), e 1 por 1, OS ITENS
# DA LISTA palavras vao se tornar X, e por fim será realizada a verificação se a primeira letra de cada item começa com
# 'a' ou 'A'
#POR FIM SO ADICIONAR O print(), PARA EXIBIR O RESULTADO
print("Filtra os elementos de 'palavras' que começam com a letra 'A': ", comecaA)











