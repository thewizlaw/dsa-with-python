def main():
    arr = [6,0,1,8,0,2]
    n = len(arr)
    result =  empty_pack(arr, n)
    print(result)

def empty_pack(arr, n):
    emp = [0] * n
    i = 0
    j = 0
    for i in range(n):
        if arr[i] != 0:
            emp[j] = arr[i]
            j+=1
    return emp

main()