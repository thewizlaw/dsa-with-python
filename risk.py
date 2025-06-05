def main():
    arr = [1,0,2,0,1,0,2]
    arr.sort()
    print(arr)
 
def count(arr):
    count0 = 0
    count1 = 0
    count2 = 0


    for i in arr:
        if i == 0:
             count0 += 1
        elif i == 1:
             count1 += 1
        else:
             count2 += 1
    
    new = []
    new += [0] * count0
    new += [1] * count1
    new += [2] * count2

    return new



main()
