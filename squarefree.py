def main():
    num = 72
    arr, sqr_arr = factor(num)
    count = perfect_square(arr, sqr_arr)
    print(count)

def factor(num):
    arr = []
    sqr_arr = []
    for i in range(1, num + 1):
        if num % i == 0:
            arr.append(i)

            sqrt_num = i ** 0.5
            if sqrt_num == int(sqrt_num) and i != 1:
                print("square_root: ", i)
                sqr_arr.append(i)
                
    return arr, sqr_arr


def perfect_square(arr, sqr_arr):
    count = 0

    for x in arr:
        if x == 1:
            continue
        if x in sqr_arr:
            continue
        divisible = False
        for y in sqr_arr:
            if x != y and x % y == 0:
                divisible = True
                break
        if not divisible:
            count += 1
                
    return count
    


    




main()