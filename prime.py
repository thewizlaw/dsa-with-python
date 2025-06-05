def main():
    number = int(input("Enter the Number: "))
    if is_prime(number):
        print("Its prime")
    else:
        print("Not Prime")

def is_prime(number):

    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number - 1):
            if number % i == 0:
                return False
        return True

main()
