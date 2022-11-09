# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

def superDigit(n, k):
    p = n*k
    
    print(p)
    # convert p para int

    # soma todos os digitos de p
    soma = 0
    for digit in p: 
        soma = soma + int(digit)
    


    print(soma)





n = '148'
k = 3

superDigit(n,k)