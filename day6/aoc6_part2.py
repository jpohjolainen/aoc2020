#!/usr/bin/env python3


def main():
    with open('input6.txt') as f:
        comb = []
        sum = 0
        for line in f:
            line = line.rstrip()
            if not line:
                ## Taking a set (set of string separates by character, so 'hey' => {'h','e','y'})
                ## * unpacks the sets into individual blocks for set.interaction to only
                ## match chars that are in all individual set, so f.ex [{'a'},{'ab'},{'abc'}] each
                ## have 'a' common in all sets
                sum += len(set.intersection(*[set(i) for i in comb]))
                comb = []
                continue
            comb.append(line)
        sum += len(set.intersection(*[set(i) for i in comb]))
    print(sum)

if __name__ == '__main__':
    main()
