def main():
    nums = [-4,-1,0,3,10]
    s = square_sort(nums)
    print(s)

def square_sort(nums):

    left = 0
    right = len(nums) - 1
    arr = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            arr.append(nums[left] ** 2)
            left+=1
        else:
            arr.append(nums[right] ** 2)
            right-=1
    arr.reverse()
    return arr
        
    
main()