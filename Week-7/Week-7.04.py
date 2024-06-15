Christmas Discount

An e-commerce company plans to give their customers a special discount for Christmas.

They are planning to offer a flat discount. The discount value is calculated as the sum of all the prime digits in the total bill amount.

Write an python code to find the discount value for the given total bill amount.
 
Constraints

1 <= orderValue< 10e100000

Input

The input consists of an integer orderValue, representing the total bill amount.

Output

Print an integer representing the discount value for the given total bill amount.

Example Input

578

Output

12

For example:

Test	Result

print(christmasDiscount(578))	12



def christmasDiscount(n):

    res=0

    while n!=0:

        rem=n%10

        flag=0

        for i in range(1,rem+1):

            if rem%i==0:

                flag+=1

        if flag==2:

            res=res+rem

        n=n//10

        

    return res

         
