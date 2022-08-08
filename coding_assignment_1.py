"""
This assignment was completed and submitted by
Yaw Akosah Asare
10946857
"""
# Code to find the average of prime numbers from 1 to 10000

def avg_ofPrimes():
    sum = 0
    count = 0
    for number in range(1, 10000):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
                else:
                    sum = sum + i
            count = count + 1
    print(sum / (count + 1))
avg_ofPrimes()