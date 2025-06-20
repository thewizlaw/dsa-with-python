def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = remove_duplicate(nums)
    print(s)
    

def remove_duplicate(nums):
    i = 0
    n = len(nums)
    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    k = i + 1
    return k

main()