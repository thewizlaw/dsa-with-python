def main():
    N = 10 # no of horses
    K = 100 # max prize money
    arr = [10, 90, 80, 20, 90, 60, 40, 60, 70, 75] #price of each horses
    max_c = horse(N, K, arr)
    print(max_c)


def horse(N, K, arr):
    total = 0
    count = 0
    max_count = 0

    for i in range(N):
        if total + arr[i] < K:
            total = total + arr[i]
            count +=1

        elif total + arr[i] > K:
            total = arr[i]
            print("max:count:", max_count)
            
            if arr[i] < K:
                count = 1 
            else:
                count = 0 
        else: # total + arr[i] == K
            count =  0
            total = 0
        max_count = max(max_count, count)
    return max_count
    
main()

        