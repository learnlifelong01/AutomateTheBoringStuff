def collatz(number):
    if number%2 == 0:
        return(number//2)
    else:
        return(3*number+1)

print("Enter the number")
num=1
import sys
try:
    num= int(input())
    if num<=0:
        print('please enter a positive integer')
        sys.exit()
    else:
        out = collatz(num)
        print("Your output is " + str(out))

        while (out!=1):
            out=collatz(out)
            print("Your output is " + str(out))
        
except ValueError:
    print('please enter an integer value')


