def split_and_join(line):
    # write your code here
    splits = line.split();
    output = "-".join(splits)
    return output

line = input()
result = split_and_join(line)
print(result)