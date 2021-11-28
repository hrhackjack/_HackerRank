lowr,upp,odd,evn=[],[],[],[]

for i in sorted(input()):
    if i.isalpha():
        x = lowr if i.islower() else upp
    else:
        x = odd if int(i)%2 else evn
    x.append(i)
print("".join(lowr+upp+odd+evn))