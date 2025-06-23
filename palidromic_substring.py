def main():
    s = "babad"
    palindrome = substring(s)
    print(palindrome)
    
def substring(s):
    n = len(s)
    res = ""
    max_len = 0
    
    for i in range(n):

        left = i
        right = i

        while left >= 0 and right < n and s[left] == s[right]:
            curr_len = right - left + 1

            if curr_len > max_len:
                max_len = curr_len
                res = s[left:right + 1]
            left-=1
            right+=1
        
        left = i
        right =  i + 1

        while left >=0 and right < n and s[left] == s[right]:
            curr_len = right - left + 1

            if curr_len > max_len:
                max_len = curr_len
                res = s[left:right + 1]
            left-=1
            right+=1

    return res


main()