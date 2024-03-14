#!/usr/bin/env python3

aset = set()
bset = set()

n = input()

for i in range(int(n)):
    aset.clear()
    bset.clear()
    aset.add(0)
    bset.add(0)
    a = input()
    value = int(a)
    while (value // 10 != 0):
        t = value % 10
        value = value // 10
        aset.add(t)
    aset.add(value)

    b = input()
    value = int(b)
    while (value // 10 != 0):
        t = value % 10
        value = value // 10
        bset.add(t)
    bset.add(value)

    if (bset <= aset):
        print("Yes")
    else:
        print("No")
    


