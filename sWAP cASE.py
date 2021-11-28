def swap_case(s):
    ns = ''
    for letter in s:
        if letter.isupper():
            ns+= letter.lower()
        else:
            ns+= letter.upper()
    return ns