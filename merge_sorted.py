def main():
    nums1 = [-1,0,0,3,3,3,0,0,0]
    m = 4

    nums2 = [1]
    n = 1

    s = merge_arr(nums1, m, nums2, n)
    print(s)

def merge_arr(nums1, m, nums2, n):
    length = len(nums1)
    j = 0

    for i in range(m-1, length):
        if nums1[i] == 0:
            nums1[i] = nums2[j]
            j+=1
    nums1.sort()

    return nums1

main()