#!/usr/bin/env python3


def main():
    lines = []
    with open('input5.txt') as f:
        lines = map(str.rstrip, f.readlines())
    f.close()

    ID_max = 0

    IDS = []
    for r in lines:
        seatr = list(range(0,128))
        seatc = list(range(0,8))
        for x in r:
            if x == 'F':
                n = len(seatr) // 2
                seatr = seatr[:n]
            elif x == 'B':
                n = len(seatr) // 2
                seatr = seatr[n:]
            if x == 'L':
                n = len(seatc) // 2
                seatc = seatc[:n]
            elif x == 'R':
                n = len(seatc) // 2
                seatc = seatc[n:]
        ID = seatr[0] * 8 + seatc[0]
        ID_max = max(ID_max, ID)
        IDS.append(ID)
        # print(r,seatr,seatc, ID, ID_max)
    print(ID_max)

    ALLIDS = [x * 8 + y for x in range(0,128) for y in range(0,8)]
    l = range(0, min(IDS))
    h = range(max(IDS), 128*8+8)
    A = set(ALLIDS).difference(IDS)
    B = set(A).difference(l)
    C = set(B).difference(h)
    print(C)


if __name__ == '__main__':
    main()
