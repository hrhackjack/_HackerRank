def nonDivisibleSubset(k, s):
    counts = k * [0]
    for i in s:
        counts[i % k] += 1

    sum = 0
    for i in range(1, (k+1)//2):
        if counts[i] > counts[k-i]:
            sum += counts[i]
        else:
            sum += counts[k-i]

    if counts[0] > 0:
        sum += 1
    if k % 2 == 0 and counts[k//2] > 0:
        sum += 1
    return sum