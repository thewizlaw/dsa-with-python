def main():
    nums = [1]
    n =1
    arr = shuffle(nums, n)
    print(arr)


def shuffle(nums, n):
    if len(nums) < 2:
        return nums

    arr = []
    i = 0
    j = n
    while i<n and j<len(nums):
        arr.append(nums[i])
        arr.append(nums[j])
        i+=1
        j+=1

    return arr


main()