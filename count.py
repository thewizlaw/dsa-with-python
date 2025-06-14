def main():
    s = "abaccb"
    ans = count_occ(s)
    print(ans)

def count_occ(s):
    count_map = {}

    for char in s:
        if char in count_map:
            count_map[char] += 1
        else:
            count_map[char] = 1
    

    if len(set(count_map.values())) == 1:
        return True
    else:
        return False

main()