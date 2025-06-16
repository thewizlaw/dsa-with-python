def main():
    nums = [-1,0,1,2,-1,-4] # -1, -1, 1, 2, 4
    s = three_sum(nums)
    print(s)

def three_sum(nums):
    nums.sort()
    final = set()
    n = len(nums)

    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                final.add((nums[i], nums[j], nums[k]))
                j+=1
                k-=1
            elif total > 0:
                k-=1
            else:
                j+=1
    return list(final)
        


main()

