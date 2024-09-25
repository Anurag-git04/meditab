
num = 153

def armstrome(n):

    sum = 0
    
    temp = n
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    if n == sum:
        return 1
    else :
        return 0
a = armstrome(num)
if a == 1:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
