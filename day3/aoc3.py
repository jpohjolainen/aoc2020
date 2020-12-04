#!/usr/bin/env python3


# def main():
#     AMAP = list(map(str.strip, open('input3.txt').readlines()))
#     lenY = len(AMAP)
#     lenX = len(AMAP[0])
#     trees = 0
#
#     moves = [(1,1), (3,1), (5,1), (7,1), (1,2)]
#
#     total = 1
#     for i in moves:
#         mx = i[0]
#         my = i[1]
#
#         y = my
#         x = mx
#         trees = 0
#         while y < lenY:
#             l = AMAP[y]
#             p = l[x%lenX]
#             if p == '#':
#                 trees += 1
#             y += my
#             x += mx
#
#         print(i,trees,total)
#         total *= trees
#     print(total)
#
# def better():
#     AMAP = list(map(str.strip, open('input3.txt').readlines()))
#     moves = [(1,1), (3,1), (5,1), (7,1), (1,2)]
#     total = 1
#     for m in moves:
#         trees = 0
#         for x,y in enumerate(range(0, len(AMAP), m[1])):
#             if (AMAP[y][x*m[0]%len(AMAP[y])] == '#'):
#                 trees += 1
#         total *= trees
#     print(total)
#
from functools import reduce

def best():
    AMAP = list(map(str.strip, open('input3.txt').readlines()))
    moves = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    print(reduce(lambda x,y: x*y, [sum([1 for x,y in enumerate(range(0, len(AMAP), m[1])) if (AMAP[y][x*m[0]%len(AMAP[y])] == '#')]) for m in moves]))


if __name__ == '__main__':
    # main()
    # better()
    best()
