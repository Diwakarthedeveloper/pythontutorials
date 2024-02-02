from typing import ItemsView


expenses= [243,8579,3245,2456,7896,3259]
#finding sum of the expenses using for loop
total = 0
# for item in expenses:
#     total = total +item
# print("the sum of total expenses=",total)

for i in range (len(expenses)):
    print('Month:',(i+1,'Expenses:',expenses[i]))
    total = total + expenses[i]

print('Total expensesis = ', total)