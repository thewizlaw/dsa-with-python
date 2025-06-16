def main():
    x = 121
    pal = check(x)
    print(pal)

def check(x):
    digits = list(str(x))
    n = len(digits)

    i = 0
    j = n-1

    while i < j:
        if digits[i] == digits[j]:
            i+=1
            j-=1
        else:
            return False
    return True

main()