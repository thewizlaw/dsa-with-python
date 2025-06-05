def main():
    N = 99
    R = 3
    
    # Step 1: sum digits of N
    digit_sum = sum_digit(N)
    
    # Step 2: multiply the digit sum by R
    multiplied_sum = final_sum(digit_sum, R)
    
    # Step 3: sum digits of the multiplied sum
    last_sum = sum_digit(multiplied_sum)
    
    print("Final result:", last_sum) 

def sum_digit(n):
    total = 0
    for digit in str(n):
        total += int(digit) 
    print("Sum of digits:", total)
    return total

def final_sum(digit_sum, r):
    multiplied = digit_sum * r
    print("Multiplied sum:", multiplied)
    return multiplied

main()
