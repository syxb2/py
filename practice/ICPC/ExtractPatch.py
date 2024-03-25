T = int(input())

for i in range(T):
    s = input().split(" ")
    num = 0
    for word in s:
        num += len(word)
        if num > 72:
            print("\n", end="")
            print(word, end=" ")
            num = len(word) + 1
        else:
            print(word, end="" if num == 72 else " ")
            num += 1
            if word == s[-1]:
                print("\n", end="")
