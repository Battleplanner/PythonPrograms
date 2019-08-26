"""

This is a program designed to help someone understand the concept of recursion.

A recursive function is a function that calls itself until a base condition is met.

So what does this mean? Well it means that the function in question will continue to call itself until
the thing it was waiting for becomes true.

The factorial of a number is simply the product of all the positive integers less than or equal to that number.

It is denoted with n!. For example 5! = 5 * 4 * 3 * 2 * 1 = 120.

You can use a recursive function to find the factorial of a given number.

"""
number = 0


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


factorial(5)

"""

So what exactly did this do? First, we have the base condition:

if number == 0 or number == 1:
    return 1
    
This is the way to exit the recursive function. The function will not end until this is true (or the computer runs out
of memory). 

Then we have the recursive bit:

else:
    return number * factorial(number - 1)
    
If you look closely, you can see that the function calls itself again, with a slightly different parameter. Rather
than calling itself with the original parameter it was given, it gives the new copy of the function the original
parameter minus 1. I'll show you why this is important later.

Finally, the code runs the recursive function with the parameter 5. This means we want to find the factorial of 5.

So how does this work in context?

Giving the parameter 5, we can see that it doesn't pass the base condition. 5 is neither 0 nor 1, and so it moves on.
The function then runs itself, but with the original parameter (5) minus 1 (i.e 4). The function is now awaiting the
result of factorial(4), so that it can multiply it by its original parameter (5) and return to the caller of the
function.

So now that the function has run itself and awaiting response, we can see what happens to the second iteration.
The function is now running with the parameter 4, which doesn't meet the base condition. It does the same thing as the
first function, and multiplies its parameter (4) by the return value of itself with the parameter 3 (4 - 1). This means
that this iteration of the function is now awaiting the return value of itself with the new parameters.

So now we're looking at the function thats been run for a third time, this time with the parameter 3. Once again, 3
doesn't meet the base condition (0 or 1), and so continues to the else statement. It then tries to return its parameter
(3) multiplied by the result of itself with the parameter (2). Awaiting the response, we follow the new iteration.

The new iteration is running with the parameter 2. Once again, it doesn't meet the base condition, so it tries to 
return its original parameter (2) multiplied by the result of the same function with the parameter 1.

Now it gets interesting. The new instance of the function has the parameter 1, which meets the base value. This returns
1 back to the previous function (i.e the function with the parameter of 2. The previous function, now knowing the
value of the called function, it can return (2 * 1) to the function that called it.

The function that called it (i.e the function with the original parameter of 3) now can return (3 * 2) (With 2 being
the result of the function it called) to the function that called it. Said function (the function with the original
parameter of 4) can now return (4 * 6) (Keep in mind that 6 is the result of 2 * 3) to the function that called it.

That function (with the original parameter of 5) is the first function to be called. It can now return the result of
(5 * 24) to the thing that called it. That would be factorial(5), the thing that started it all. And thats how
you can get the value of 5!. Thats also the concept of recursive functions.

Of course, there's a lot more to cover, like how it compares to iterative programming, other parts of recursion, etc -
but you know what, I'm too lazy to do that now. So as it stands, this is what you get. You're welcome.

"""