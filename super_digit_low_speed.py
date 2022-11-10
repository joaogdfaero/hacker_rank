# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

def superDigit(n, k):
    p = n*k
    
    print(p)
    # convert p para int

    # soma todos os digitos de p
    soma = 0

    x = len(p)

    while x > 1: 
        soma = 0
        for digit in p:
            soma = soma + int(digit)
        print("P agora é")
        p = str(soma)
        x = len(p)
        print(p)
    
    return p
    

n = '9875'
k = 1

superDigit(n,k)