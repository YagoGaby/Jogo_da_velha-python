nada = " "
token = ["X","O"]

def criarBoard():
    board = [
        [nada, nada, nada],
        [nada, nada, nada],
        [nada, nada, nada],
    ]
    return board


def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if(i < 2):
            print("------")


def getInputValido(mensagem):
  try:
    n = int(input(mensagem))
    
    if(n>=1 and n<=3):
      return n - 1
    else:
       print("O número precisa estar entra 1 e 3!!") 
       return getInputValido(mensagem)
  except:
    print("O número precisa estar entra 1 e 3!!") 
    return getInputValido(mensagem)


def verificaMovimento(board, i , j):
  if(board[i][j]==nada):
    return True
  else:
    return False

    
def fazMovimento(board, i, j, jogador):
  board[i][j] = token[jogador]



def verificaGanhador(board):
  #primeiro as linhas
  for i in range(3):
    if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] !=nada):
      return board[i][0]
  #Colunas
  for i in range(3):
    if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] !=nada):
       return board[0][i]

  #Diagonal 1
  if (board[0][0] !=nada and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
      return board[0][0]

  #Diagonal 2
  if (board[0][2] !=nada and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
      return board[0][2]

  for i in range(3):
    for j in range(3):
      if (board[i][j] == nada):
        return False

  return "Deu Velha :| "
