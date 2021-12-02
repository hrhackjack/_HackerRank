def print_rangoli(n):
    string = "abcdefghijklmnopqrstuvwxyz"
    items = [string[i] for i in range(n)]
    li = list(range(n))
    li = li[:-1] + li[::-1]
    #print(li)
    for i in li:
        tmp = items[-(i+1):]
        #print(tmp)
        row = tmp[::-1]+tmp[1:]
        #print(row)
        print("-".join(row).center(n*4-3, "-"))
