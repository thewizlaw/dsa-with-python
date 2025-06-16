def main():
    nums = [2,7,11,15]
    target = 9
    s=two_sum(nums, target)
    print(s)


def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in hashmap:
            return hashmap[comp], i
        hashmap[num] = i
    return []
    
    
    
main()