n,li =input(), input().split()
print(all(map(lambda n: int(n)>-1, li)) and any(map(lambda n: n == n[::-1], li)) )