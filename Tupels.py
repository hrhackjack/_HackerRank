n = int(input())
ilist = []
ilist = map(int, input().split())
#ilist = [int(x) for x in input.split()]
ituple = tuple(ilist)
print(hash(ituple))
