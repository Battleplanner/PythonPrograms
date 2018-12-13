import sys
import time
# def recurse(n):
#     print(n)
#     recurse(n + 1)
#
# recurse(1)
#The code above stopped at 996 before reaching the recursion limit

# def recurse(n):
#     print(n)
#     sys.setrecursionlimit(sys.getrecursionlimit() + 1)
#     # if n == 4000:
#     #     return
#     #This is a failsafe that makes sure the code stops at a certain point
#     recurse(n + 1)
#
# recurse(1)
#Without the failsafe, the program continued to run, stopping at 6783 before hitting the recursion limit

# def recurse(n):
#     print(n)
#     sys.setrecursionlimit(n + 100)
#     recurse(n + 1)
#
# recurse(1)
# This managed to get slightly further by making sure the recursion limit was 100 more than the number, stopping at 6787

def recurse(n):
    print(n)
    sys.setrecursionlimit(n + 70)
    time.sleep(0.01)
    recurse(n + 1)

recurse(1)
