# Arman Ashrafian
# 4-5-2017
# show powers of 2 that add up to a decimal number
import math

def main():
    binary_nums = []
    num = float(input("Enter Number: "))
    power = getStartingPower(num)

    numCopy = num   #starting point
    while(numCopy > 0):
        if(numCopy - math.pow(2, power) >= 0):
            numCopy -= math.pow(2,power)
            binary_nums.append("2^%d" % power)
        power -= 1

    outputList(binary_nums)


def getStartingPower(num):
    count = 0
    while(num > 1):
        num = num * .5
        count += 1
    return count

def outputList(arr):
    for num in arr:
        print(num)

if __name__ == '__main__':
    main()
