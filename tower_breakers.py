# HACKER RANK - TOWER BREAKERS

def towerBreakers(n, m):
    # Write your code here
    # n = number of towers
    # m = height of tower
    towers = [1]*n
    towers = [i * m for i in towers]
    #print(towers)

    def evenly_divides(integer): # método para achar o menor número divisível > 1
        numeros_anteriores = list(range(1,integer)) # cria uma lista com os números anteriores
        for i in range(0,len(numeros_anteriores)):
            if integer % numeros_anteriores[i] != 0 or numeros_anteriores[i]== 1: #torna zero todos aqueles números que não são divisíveis ou são o 1
                #print("está anulando")
                #print(numeros_anteriores[i])
                numeros_anteriores[i]=0
        
        max_divisivel = max(numeros_anteriores) #maximo número divisível
        #print(max_divisivel)
        return max_divisivel

    
    


        
    
    # players jogam
    counter = 0 #contador para saber quem está jogando
    while True:
        for i in range(0,len(towers)):
          counter = counter + 1
          max_index = towers.index(max(towers))
          towers[max_index] =  evenly_divides(towers[max_index])
        if 0 in towers:
            break

    
    print(counter)

    print(towers)
    



    
    

    


n=2
m=6
towerBreakers(n,m)