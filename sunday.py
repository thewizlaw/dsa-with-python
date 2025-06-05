def main():
    start = input("Enter the start of week: ")
    n = int(input("Enter no. of days: "))
    count = count_sundays(start, n)
    print(count)

def count_sundays(start, n):
    week = {
        "sun" : 0,
        "mon" : 1,
        "tue" : 2,
        "wed" : 3,
        "thu" : 4,
        "fri" : 5,
        "sat" : 6,
    }

    current_day = week[start]
    count = 0

    for i in range(n):
        if current_day == 0:
            count+=1
        current_day = (current_day + 1) % 7
    return count

main()