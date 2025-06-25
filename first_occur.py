def main():
    haystack = "sadbutsad"
    needle = "sad"
    s = occur(haystack, needle)
    print(s)

def occur(haystack, needle):
    needle_list = list(needle)
    len_h = len(haystack)
    len_n = len(needle)

    for i in range(len_h - len_n + 1):
        count = 0
        j = 0
        index = i

        while j < len_n and haystack[i + j] == needle_list[j]:
            count+=1
            j+=1

        if count == len_n:
            return index
        
            
    return -1

    
main()

