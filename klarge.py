def main():
    N = 2
    K = 3 
    KHF = factor(N, K)
    print(f"{K}th Highest Factor: ", KHF)

def factor(N, K):
    arr = []
    
    for i in range(1, N+1):
        if N % i == 0:
            arr.append(i)
    
    length = len(arr)

    if K < len(arr):
        return arr[length - K]
    else:
        return 1

main()