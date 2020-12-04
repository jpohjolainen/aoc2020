#!/usr/bin/env python3


VALID_FIELDS = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

VALID_VALUES = {
    'byr': [1920,2002],
    'iyr': [2010,2020],
    'eyr': [2020,2030],
    'hgt': {'cm': [150,193], 'in': [59,76]},
    'hcl': 6,
    'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': 9
}

def check_validity(P):
    F = []
    print(">",P)
    valid = False
    for i in P:
        (field, val) = i.split(':')
        if field in ['byr', 'iyr', 'eyr']:
            v = int(val)
            if (v >= VALID_VALUES[field][0] and v <= VALID_VALUES[field][1]):
                F.append(field)
        if field == 'hgt':
            if 'in' in val:
                v = val.strip('in')
                if int(v) >= VALID_VALUES['hgt']['in'][0] and int(v) <= VALID_VALUES['hgt']['in'][1]:
                    F.append(field)
            elif 'cm' in val:
                v = val.strip('cm')
                if int(v) >= VALID_VALUES['hgt']['cm'][0] and int(v) <= VALID_VALUES['hgt']['cm'][1]:
                    F.append(field)
        if field == 'hcl':
            if '#' in val:
                v = val.strip('#')
                if len(v) == VALID_VALUES['hcl']:
                    F.append(field)
        if field == 'ecl':
            if val in VALID_VALUES['ecl']:
                F.append(field)
        if field == 'pid':
            if len(val) == VALID_VALUES['pid']:
                F.append(field)
    print(F, len(F))
    if len(F) != len(VALID_FIELDS):
        return False
    # for i in VALID_FIELDS:
    #     if not i in F:
    #         # print(P)
    #         return False

    return True

def main():
    valid = 0
    with open('input4.txt') as f:
        PP = []
        for line in f:
            line = line.rstrip()
            if not line:
                # print("check", PP)
                if check_validity(PP):
                    valid += 1
                else:
                    print('invalid',PP)
                PP = []
                continue
            if ' ' in line:
                line = line.split(' ')
            else:
                line = [line]
            PP.extend(line)
        if check_validity(PP):
            # print("check", PP)
            valid += 1
        else:
            print('invalid2',PP)

    f.close()
    print(valid)

if __name__ == '__main__':
    main()
