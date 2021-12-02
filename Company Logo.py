from collections import Counter
for i in Counter(sorted(input())).most_common(3):
    print(*i)