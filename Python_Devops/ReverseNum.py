from typing import Iterator

def reverseNumber(num):
    rev=0
    while num!=0:
        rev = (rev * 10) + (num % 10)
        num = num // 10 # to get floor divison, 15/2 = 7.5 -> 7

    return rev

num=int (input("Enter any number here :"))
print("the reversed number is :", reverseNumber(num))