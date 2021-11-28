def minion_game(string):
    string = string.upper()
    l=len(string)
    vowel = 0
    consonant = 0
    for i in range(l):
        if string[i] in 'AEIOU':
            vowel+=(l-i)
        else:
           consonant+=(l-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')