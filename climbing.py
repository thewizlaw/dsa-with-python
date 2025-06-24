def  main():
    n = 4
    s = stairs(n)
    print(s)

def stairs(n):
    if n ==0 or n ==1:
        return 1
    a = 1
    b = 1

    for _ in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

main()