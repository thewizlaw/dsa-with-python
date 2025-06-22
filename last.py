def main():
    s = "   fly me   to   the moon  "
    s = s.strip()
    new = list(s)
    print(new)
    n = len(new)
    length = 0
    i = n-1
    while i>= 0:
        if new[i] != ' ':
            length+=1
            i-=1
        else:
            break
    print(length)

main()