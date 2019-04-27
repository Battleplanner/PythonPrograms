class Main:
# Note to self: Later, have it so that they write the equation itself, not just the values.
    def __init__(self):
        """Initiates the Main class, gets the inputs from the user and organises them"""
        print("Please give the values of the quadratic equation")
        print("Remember, the format is ±ax^2 ± bx ± c. Use - and + to show whether it is positive or negative")
        self.values = []

    def user_input(self):
        a = int(input("Please input 'a' here: "))
        if a == 0: # The rule is that 'a' cannot be 0
            print("That number is unacceptable. Please input another")
            a = int(input("Please input 'a' here: "))
        b = int(input("Please input 'b' here: "))
        c = int(input("Please input 'c' here: "))

        print("Thank you")
        return [a, b, c]

    def choose_method(self):
        while True:
            if self.values[0] == 1: # if 'a' is equal to 1
                self.StandardMethod(self.values) # Use the normal method
                break
            elif self.values[0] != 1: # If 'a' isn't equal to 1
                self.GroupMethod(self.values) # use the group method
                break
            else:
                print("That isn't valid") # Otherwise, if it's a letter or something, print this and repeat the loop.

    def main_loop(self):
        running = True
        self.values = self.user_input(self) # Runs the user_input method
        self.choose_method(self) # Runs the choose_method method

        while running == True:
            if self.solve_again() == False:
                running == False
            else:
                print("Alright then! From the top.")


    def format_answer(self):
        pass

    def solve_again(self):
        """Asks to see if the user wants to solve another equation"""

        positive_responses = ["Yes", "yes", "y", "Y", "yeah", "YEAH", "Yeah", "YES"]
        negative_responses = ["No", "no", "n", "N", "Nah", "nah", "NO"]

        while True:
            answer = str(input("Do you want to solve another equation? "))
            if answer in positive_responses:
                return True
                break
            elif answer in negative_responses:
                print("That's okay. Hope I helped!")
                return False
            else:
                print("That isn't a valid response!")

class StandardMethod(self, values):
    """The method of solving the equation when a = 1"""


    """Finds the factors of c and puts them in a list"""
    factor_list = []
    for i in range(1, int(self.values[2] ** 0.5) + 1):  # For every number between 1 and the square root of c
        if self.values[2] % i == 0:  # If c is a multiple of i ( no remainder)...
            factor_list.append((int(i), int(self.values[2] / i)))  # Apeend the int versions of the factor pair to the factors list



    """Chooses the factor pair that adds/subtracts to equal b, and returns the pair and whether they're negative or not"""

    for i in factor_list:

        if (i[0] + i[1] == self.values[1]):  # If both factors are positive
            sign1 = "+"
            sign2 = "+"
            factor_pair = i
            break

        elif (i[0] - i[1] == self.values[1]):  # If factor 1 is positive and factor 2 is negative
            sign1 = "+"
            sign2 = "-"
            factor_pair = i
            break

        elif (i[1] - i[0] == self.values[1]):  # If factor 2 is positive and factor 1 is negative
            sign1 = "+"
            sign2 = "-"
            factor_pair = i
            break

        elif ((i[1] * -1) - i[0] == self.values[1]):  # If factor 1 is negative and factor 2 is negative
            sign1 = "+"
            sign2 = "-"
            factor_pair = i
            break

    """Formats the answer into a way that is readable by humans"""

    answer = "(x {} {})(x {} {})".format(sign1, factor_pair[0], sign2, factor_pair[1])
    print("The answer is {}".format(answer))
    self.solve_again(self)


class GroupMethod:
        """ The method of solving the equation when a != 1"""

        # This section is for checking for a gcf. If there is, then a different form of factoring can commence
        # Example: 2x^2 + 10x + 12 becomes 2(x^2 + 5x + 6).

        # Which can then be done using the standard method (i.e end result will be 2(x + 2)(x + 3)

        def check_for_common_factor(self):
            """Finds the GCD of the terms, if there is any, and factorises using that"""

            gcd = None # Initialises the gcd variable

            # For every number between the smallest of the terms (a, b, c) to 0, counting down
            for i in range(min(self.values), 0, -1):
                for num in self.values: # For each term ...
                    if num % i != 0: # If there is a remainder, then there is no common factors among all three term
                            break
                else: # Otherwise, the number is the highest common divisor
                    gcd = i # Note: The reason it is the HIEGHEST is because it counts down, so the first variable is higher.
                    break

            if gcd != None: # If there is a common factor
                factorised_terms = [gcd, (x // gcd for x in self.values)]
                print(factorised_terms)





        # If there isn't a common factor between all the values, then the other method is required


        # Step 1: Multiply ax^2 and c (-3x^2 * -8 = -24x^2)

        # Step 2: Find 2 numbers that multiply to get acx^2 and add to get bx ( -12x * 2x = -24x^2, -12x + 2x = -10x)

        # Step 3: Rewrite equation (i.e 3x^2 - 10x - 8 = 3x^2- 12x + 2x - 8

        # Step 4: Group together terms that share common factors (3x^2- 12x + 2x - 8 becomes 3x(x-4) + 2(x-4)

        # Step 5: Rewrite (as the terms in the brackets are the same): 3x(x-4) + 2(x-4) becomes (3x + 2)(x - 4)


def main():
    print("Welcome to the Quadratic Factoring Program!")


if __name__ == "__main__":
    main()