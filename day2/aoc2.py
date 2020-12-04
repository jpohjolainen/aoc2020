#!/usr/bin/env python3


def main():
    valid = 0
    f = open("input2.txt")
    for x in f.readlines():
        (c, l, p) = x.split(' ')
        l = l[0]
        (min, max) = c.split('-')
        ## first part
        # if (p.count(l) >= int(min) and p.count(l) <= int(max)):
        #     valid += 1

        ## second part
        min = int(min) - 1
        max = int(max) - 1
        if (p[min] == l or p[max] == l):
            if (p[min] == l and p[max] == l):
                continue
            valid += 1
    print(valid)
    f.close()


if __name__ == '__main__':
    main()
