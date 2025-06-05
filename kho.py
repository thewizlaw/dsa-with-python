def main():
    n = 5
    arr = [1, 2, 3, 2, 3]
    count = optimal(n, arr)
    print(count)

def kho_kho(n, arr):
    i = 0
    j = 1
    count = 0
    while i < n and j < n:
        understand = False
        print("arr[i]: ", arr[i])
        print("arr[j]: ", arr[j])
        if arr[i] != arr[j]:
            count +=1
            understand = False
        elif arr[i] == arr[j]:
            understand = True
        i+=1
        j+=1
    if(understand):
            count +=1
        
    return count

def optimal(n, arr):
    correct = 0
    incorrect = 0
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            correct += 1
    print("correct: ", correct)
    incorrect = (n - 1) - correct
    return incorrect
main()