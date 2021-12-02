import numpy
# from numpy import linalg

# n = int(input())
# a = numpy.array([input().split() for _ in range(n)], float)
# print(round(linalg.det(a),2))

print(round(numpy.linalg.det(numpy.array([input().split() for _ in range(int(input()))],float)),2))