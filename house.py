def main():
    n = 7
    arr = [6, 7, 1, 3, 8, 2, 5]
    max_sum = max_fun(n, arr)
    print(max_sum)

def max_fun(n, arr):
    sum1 = 0
    max_sum = 0
    for i in range(0, n, 2):
        print(arr[i])
        sum1 = sum1 + arr[i]
        max_sum = max(max_sum, sum1)
    return max_sum




main()