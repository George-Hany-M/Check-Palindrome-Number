# My Name : George Hany
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse.

# input the number from the user
num = input('The number is : ')

# boolean to chech if the number is palindrome or not ?!
flag = True

length = len(num)
limit = length // 2
for index in range(limit): # 0 1 2 3 4 5
    if num[index] != num[length - index - 1]:
        flag = False
        break
    
if flag:
    print('Yes, given number is palindrome number')
else:
    print('No,  given number is not palindrome number')
