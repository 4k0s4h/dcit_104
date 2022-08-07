"""
This assignment was completed and submitted by
Yaw Akosah Asare
10946857
"""
def avg_ofPrimes():
    sum = 0

    for num in range(2, 10):
        i = 2
        for i in range(2, num):
            if num % i == 0:
                i = num
                break
        if i is not num:
            sum += num
    print(sum / i)
avg_ofPrimes()