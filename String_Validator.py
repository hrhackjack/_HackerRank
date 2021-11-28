def alnum(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;
        
def al(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False;

def dig(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

def lw(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False; 
     
def up(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;
 
s = input()
    
alphanum = alnum(s)
alpha = al(s)
digits = dig(s)
lwr = lw(s)
uppr = up(s)
print(alphanum)
print(alpha)
print(digits)
print(lwr)
print(uppr)
