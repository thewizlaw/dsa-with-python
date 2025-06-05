def main():
    N = 5283
    max = optimal(N)
    print(max)

def fprice(N):
    max_product = 1
    nums = list(map(int, str(N))) # conver number into list of integers
    for digit in nums:
        max_product = digit * max_product
    return max_product

def optimal(N):
    max_product = 1
    for digit in str(N):
        max_product *= int(digit)
    return max_product
    
main()