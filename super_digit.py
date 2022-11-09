# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

def superDigit(n, k):
    p = n*k
    
    print(p)
    # convert p para int

    # soma todos os digitos de p
    soma = 0
    for i in range(0,len(p)-1): #-> ERRADP POIS PEGA ALGUNS ELEMENTOS 2X, NÃO A SOMA DE TODOS
        print('int(p[i])')
        print(int(p[i]))
        print('int(p[i+1])')
        print(int((p[i+1])))

        soma = soma + int(p[i])+int(p[i+1])

    print(soma)





n = '148'
k = 3

superDigit(n,k)