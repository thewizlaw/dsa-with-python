def main():
    arr = [7,4,8,2,9]
    n = len(arr)
    count = optimal(arr, n)
    print(count)


def count_num(arr, n):
    count = 0

    for i in range(n):
        all_small = True
        for j in range(i):
            if arr[j] >= arr[i]:
                all_small = False
                break
        if all_small:
            count = count + 1
    return count


def optimal(arr, n):
    count = 0
    max = arr[0]
    for i in range(n):
        if arr[i] >= max:
            count = count + 1
            max = arr[i]
    return count
main()


