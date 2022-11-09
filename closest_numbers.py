# https://www.hackerrank.com/challenges/closest-numbers/problem


def closestNumbers(arr):
    sorted_arr = sorted(arr)
    diferenca = [0]*(len(arr)- 1)

    for i in range(0,len(arr)-1):      
        diferenca[i] = abs(sorted_arr[i] - sorted_arr[i+1])
    
    # minimum differnce
    minimum_diff = min(diferenca)
    
    # printa valores com a menor diferenca
    for i in range(0,len(diferenca)):
        if diferenca[i] == minimum_diff:
            print(sorted_arr[i])
            print(sorted_arr[i+1])
        else:
            pass


    

    





arr = [-20,-3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
#arr = [1,2,3,4]

closestNumbers(arr)