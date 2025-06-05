def main():
    curtains = "abbbaabbb"
    L = 5
    max_count = max_a(curtains, L)
    print("max: ", max_count)

def max_a(curtains, L):
    parts = []
    n = len(curtains)
    max_count = 0
    for i in range(0, n, L): # start, end, step
        part = curtains[i: i + L] # splice- strt index: end index
        count = part.count('a')
        if count > max_count:
            max_count = count
        print(max_count)
        parts.append(part)

    print(parts)
    return max_count

main()