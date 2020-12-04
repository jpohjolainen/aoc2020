#!/usr/bin/env python3

def main():
    NUMS = []
    with open('input1.txt') as f:
        NUMS = list(map(str.strip, f.readlines()))
    l = len(NUMS)
    # a = 0
    # f = False
    # while a < l:
    #     b = a + 1
    #     while b < l:
    #         c = b + 1
    #         while c < l:
    #             if (int(NUMS[a]) + int(NUMS[b]) + int(NUMS[c]) == 2020):
    #                 print("GOT IT:", int(NUMS[a]) * int(NUMS[b]) * int(NUMS[c]))
    #                 f = True
    #                 break
    #             c += 3
    #         if f:
    #             break
    #         b += 2
    #     if f:
    #         break
    #     a += 1

    # f = False
    # for a in NUMS:
    #     for b in NUMS[1:]:
    #         for c in NUMS[2:]:
    #             if (int(a)+int(b)+int(c) == 2020):
    #                 print("GOT IT TOO!", int(a)*int(b)*int(c))
    #                 f = True
    #                 break
    #         if f:
    #             break

    # for a in range(0,l):
    #     for b in range(a+1,l,2):
    #         for c in range(b+1,l,3):
    #             if (int(NUMS[a]) + int(NUMS[b]) + int(NUMS[c]) == 2020):
    #                 print("GOT IT:", int(NUMS[a]) * int(NUMS[b]) * int(NUMS[c]))
    #                 return

    import time

    NUMS = list(map(int, map(str.strip, open('input1.txt').readlines())))

    tic = time.perf_counter()
    print([NUMS[a]*NUMS[b]*NUMS[c] for a in range(0,len(NUMS),2) for b in range(a+1,len(NUMS),2) for c in range(b+1,len(NUMS),3) if NUMS[a] + NUMS[b] + NUMS[c] == 2020])
    print(f'time: {time.perf_counter() - tic:0.4f}s')

    from itertools import combinations
    tic = time.perf_counter()
    print([x[0]*x[1]*x[2] for x in combinations(NUMS, 3) if sum(x) == 2020])
    print(f'time: {time.perf_counter() - tic:0.4f}s')


    # import timeit
    # #
    # print(timeit.timeit('[NUMS[a]*NUMS[b]*NUMS[c] for a in range(0,len(NUMS),2) for b in range(a+1,len(NUMS),2) for c in range(b+1,len(NUMS),3) if NUMS[a] + NUMS[b] + NUMS[c] == 2020]', setup='NUMS = list(map(int, map(str.strip, open(\'input1.txt\').readlines())))', number=1))
    #
    # print(timeit.timeit('[NUMS[a]*NUMS[b]*NUMS[c] for a in range(0,len(NUMS)) for b in range(a+1,len(NUMS),2) for c in range(b+1,len(NUMS),3) if NUMS[a] + NUMS[b] + NUMS[c] == 2020]', setup='NUMS = list(map(int, map(str.strip, open(\'input1.txt\').readlines())))', number=1))

    #
    # total = 0
    # for a in range(0,len(NUMS),2):
    #     for b in range(a+1,len(NUMS),2):
    #         for c in range(b+1,len(NUMS),3):
    #             total += 1
    #             if (NUMS[a] + NUMS[b] + NUMS[c] == 2020):
    #                 print("GOT IT:", NUMS[a] * NUMS[b] * NUMS[c])
    #                 print("iter:", total)
    #                 return


if __name__ == '__main__':
    main()
