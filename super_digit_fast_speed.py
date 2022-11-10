# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

def superDigit(n, k):
    p = n*k

    # checa single digits
    if k == len(n) == 1:
        print(int(n))
        return int(n)

    soma = 0
    for digit in p:
        soma = soma + int(digit)

    return superDigit(str(soma*k),1)
    

n = '9875'
k = 1

superDigit(n,k)