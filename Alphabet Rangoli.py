def merge_the_tools(s, k):
    subs = int(len(s) / k)

    for i in range(subs):
    # Subsegment string
        t = s[i*k : (i+1)*k] 
    # Subsequence string having distinct characters
        x = ""
    # If a character is not already in 'x', append
        for c in t:
            if c not in x:
              x += c
    # Print final converted string
        print(x)
