n,m = map(int,input().split())
ilist = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
#Union set A & B
C = A | B
#Exclude all numbers which doesn't exit in both A & B
ilist = (i for i in ilist if i in C)
#Add 1 if number is in set A else subtract 1
print(sum(1 if i in A else -1 for i in ilist ))