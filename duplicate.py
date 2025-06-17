def main():
    nums = [1,2,3,1]
    s = duplicate(nums)
    print(s)

def duplicate(nums):

    len1 = len(nums)
    unique = set(nums)
    len2 = len(unique)

    if len1 == len2:
        return False
    else:
        return True

main()