# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

def superDigit(n, k):
        
    # check single digits
    if k == len(n) == 1:
        print(int(n))
        return int(n)

    res = 0
    for num in n:
        res += int(num)
        print("res é")
        print(res)
        print("k é")
        print(k)


    return superDigit(str(res*k),1)
    

n = '9875'
k = 4

superDigit(n,k)