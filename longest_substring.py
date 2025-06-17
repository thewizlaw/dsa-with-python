def main():
    s = "pwwkew"
    final = longest_substring(s)
    print(final)

def longest_substring(s):
    new_set = set()
    left = 0
    n = len(s)
    max_length = 0

    for right in range(n):
        while s[right] in new_set:
            new_set.remove(s[left])
            left+=1
        
        current_len = (right - left) + 1
        max_len = max(max_length, current_len)
        new_set.add(s[right])
    return max_len

          
            
main()

     

