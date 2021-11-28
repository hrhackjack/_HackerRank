from datetime import datetime

def time_diff(x,y):
    f= '%a %d %b %Y %H:%M:%S %z'
    x = datetime.strptime(x, f) 
    y = datetime.strptime(y, f) 
    diff = (x-y).total_seconds()  
    return abs(int(diff))

for i in range(int(input())):
    print(time_diff(input(), input()))