#!/usr/bin/env python3


def main():
    with open('input6.txt') as f:
        comb = []
        sum = 0
        for line in f:
            line = line.rstrip()
            if not line:
                sum += len(set.intersection(*[set(i) for i in comb]))
                comb = []
                continue
            comb.append(line)
        sum += len(set.intersection(*[set(i) for i in comb]))
    print(sum)

if __name__ == '__main__':
    main()
