def TimeDiff(a, b):
    if a == 0: a = 24
    if b == 0: b = 24
    

    if b > a:
        return b - a
    else:
        return b + 24 - a

if __name__ == "__main__":
    print(TimeDiff(24, 0))
    print(TimeDiff(0, 24))
    print(TimeDiff(8, 12))  