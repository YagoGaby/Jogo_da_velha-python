from jogo_da_velha import criarBoard, fazMovimento,  getInputValido, \
                            printBoard, verificaGanhador,  verificaMovimento
jogador = 0 #jogador1
board = criarBoard()
ganhador = verificaGanhador(board)
while(not ganhador):
    printBoard(board)
    print("!====!")
    i = getInputValido("Digite a linha: ")
    j = getInputValido("Digite a coluna: ")
    

    if(verificaMovimento(board, i, j,)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1)%2 #Serve para fazer a troca de jogadores
    else:
        print("Essa possição ja foi ocupada :(")
    


    ganhador = verificaGanhador(board)



print("#=====#")
printBoard(board)
print(f'Parabéns ao {ganhador}:' )
print("#=====#")
