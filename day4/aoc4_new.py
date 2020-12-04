#!/usr/bin/env python3

VALID_VALUES = {
    'byr': [1920,2002],
    'iyr': [2010,2020],
    'eyr': [2020,2030],
    'hgt': {'cm': [150,193], 'in': [59,76]},
    'hcl': {'#': 6},
    'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': 9
}

PP = []

with open('input4.txt') as f:
    tmp = []
    for line in f:
        line = line.rstrip()
        if not line:
            PP.append(' '.join(tmp))
            tmp = []
            continue
        tmp.append(line)
    PP.append(' '.join(tmp))

# Part 1
valids = [1 for p in PP if len([1 for x in VALID_VALUES if x in [x.split(':')[0] for x in p.split(' ')]]) == len(VALID_VALUES)]
print(len(valids))

# Part 2
def check(p):
    (f,v) = p.split(':')
    if f in VALID_VALUES:
        x = VALID_VALUES[f]
        if type(x) == list and len(x) == 2:
            if int(v) >= x[0] and int(v) <= x[1]:
                return True
        elif type(x) == list:
            if v in x:
                return True
        elif type(x) == int:
            if len(v) == x:
                return True
        elif type(x) == dict:
            for y,e in x.items():
                if y in v:
                    t = v.strip(y)
                    if type(e) == int:
                        if len(t) == e:
                            return True
                    elif type(e) == list:
                        if int(t) >= e[0] and int(t) <= e[1]:
                            return True
    return False

print(len([1 for p in PP if len([1 for i in p.split(' ') if check(i)]) == len(VALID_VALUES)]))

# valid2 = 0
# for p in PP:
#     OK = 0
#     for i in p.split(' '):
#         (f,v) = i.split(':')
#         if f in VALID_VALUES:
#             x = VALID_VALUES[f]
#             if type(x) == list and len(x) == 2:
#                 if int(v) >= x[0] and int(v) <= x[1]:
#                     OK += 1
#             elif type(x) == list:
#                 if v in x:
#                     OK += 1
#             elif type(x) == int:
#                 if len(v) == x:
#                     OK += 1
#             elif type(x) == dict:
#                 for y,e in x.items():
#                     if y in v:
#                         t = v.strip(y)
#                         if type(e) == int:
#                             if len(t) == e:
#                                 OK += 1
#                         elif type(e) == list:
#                             if int(t) >= e[0] and int(t) <= e[1]:
#                                 OK += 1
#     if OK == len(VF):
#         valid2 += 1
#
# print(valid2)
