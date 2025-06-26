from collections import Counter

def main():
    nums = [3,2,3]
    mosts = most(nums)
    print(mosts)

def most(nums):
    counter = Counter(nums)
    return counter.most_common(1)[0][0]

main()