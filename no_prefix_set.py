#hackerrank.com/challenges/no-prefix-set/problem # NÃO CONSEGUI RESOLVER
def noPrefix(words):
    for i in range(0,len(words) - 1):
        if words[i] in words.remove(words[i]):
            print(words)
            print("true")
    
words = ['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']
noPrefix(words)
