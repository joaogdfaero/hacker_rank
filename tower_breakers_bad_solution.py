# HACKER RANK - TOWER BREAKERS

def towerBreakers(n, m):
    # Write your code here
    # n = number of towers
    # m = height of tower
    towers = [1]*n
    towers = [i * m for i in towers]
    print(towers)

    deu_1 = 0

    def evenly_divides(integer): # método para achar o menor número divisível > 1
        if integer == 1:
            deu_1 = 1
            return 0
        else:
            numeros_anteriores = list(range(1,integer)) # cria uma lista com os números anteriores
        for i in range(0,len(numeros_anteriores)):
            if integer % numeros_anteriores[i] != 0: #or numeros_anteriores[i]== 1: #torna zero todos aqueles números que não são divisíveis ou são o 1
                #print("está anulando")
                #print(numeros_anteriores[i])
                numeros_anteriores[i]=0
        
        max_divisivel = max(numeros_anteriores) #maximo número divisível
        #print(max_divisivel)
        return max_divisivel
        

    # players jogam
    counter = 0 #contador para saber quem está jogando
    while True:
        if len(towers) == 1:
            for i in range(0,len(towers)):
              counter = counter + 1
              max_index = towers.index(max(towers))
              towers[max_index] =  evenly_divides(towers[max_index])
              print("towers é")
              print(towers)
            if 0 in towers:
                break
        else:
            for i in range(0,len(towers)-1):
               counter = counter + 1
               max_index = towers.index(max(towers))
               towers[max_index] =  evenly_divides(towers[max_index])
               print("towers é")
               print(towers)
            if 0 in towers:
               break

    print(counter)

    print(towers)

    # define o vencedor
    if deu_1 == 1:
        if (counter % 2) == 0:
            print("2 venceu")
        else:
            print("1 venceu")
    else:
        if (counter % 2) == 0:
          print("1 venceu")
        else:
          print("2 venceu")




n=1 # DÁ PROBLEMA PRA ESSA ENTRADA
m=4 
towerBreakers(n,m)