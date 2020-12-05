#!/usr/bin/env python3


def main():
    with open('input5.txt') as f:
        lines = map(str.rstrip, f.readlines())
    f.close()

    ids = [sum([1 << (9-x) for x in range(10) if s[x] in ['B', 'R']]) for s in lines]
    print("part1", max(ids))

    ids_sorted = sorted(ids)
    print("part2", [ids_sorted[i] + 1 for i in range(len(ids)-1) if ids_sorted[i+1] != ids_sorted[i] + 1][0])


if __name__ == '__main__':
    main()
