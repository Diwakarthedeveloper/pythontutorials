grocery = ["Biscuits","cake","vetable oil","soap","dishwasher","Deodrant","Icecream", 56]
print(grocery)

print(grocery[6])
numbers = [2,7,9,11,3]
print(numbers[2])
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#----slicing below---
print(numbers[0:5])
print(numbers[0:])
print(numbers[:5])

print(numbers[1:]) #it will start from second position
print(numbers[:4]) #prints till 4th value
print(numbers[::-1]) #-1 will reverse the number list and other than -1 will give incorrect results after reverse
print(numbers[1:5:-1]) #this will give blank list so this is error
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.append(7)
numbers.insert(2, 67) #67 at second position
numbers.remove(9)
numbers.pop() #will remove last number
