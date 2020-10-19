# This project is made for Emmanuel Ogunjirin (eao5xc) and Kieran Humphrey (kdh8az)
# This is for our Probability project.

# Imports needed for the projects.
import math

# Defines variables to be used in the project
BUSY_PROBABILITY = 0.2
UNAVAILABLE_PROBABILITY = 0.3
AVAILABLE_PROBABILITY = 0.5
k = pow(2, 14)
customer_limit = 6

BUSY_STRING = "BUSY"
UNAVAILABLE_STRING = "UNAVAILABLE"
AVAILABLE_STRING = "AVAILABLE"

# Defines variables that are changing
x = 1000


def rannumgen():
    """
    Function to provide information for the random number
        generator using the linear congruential random number
        generator rule

    Returns:
        [decimal]: [value of the linear congruential random number]
    """
    global x  # Accesses outside variable

    # Set some constants
    a = 9429
    c = 3967

    # Formula defines in appendix of project
    x_i = ((a * x) + c) % k
    x = x_i  # Reassigns the previous value
    u_i = x_i / k
    return u_i


# Iterates over the specific range needed
for i in range(customer_limit):
    RECALL_LIMIT = 4  # This is the maximum redial possible
    seconds = 0    # Initial time to start calling someone
    randomnumber = rannumgen()  # Runs the random number generator

    for j in range(0, RECALL_LIMIT, 1):
        seconds += 6     # Initial time to pick up phone and dial a number

        if (j <= RECALL_LIMIT):  # Checks if we are still within redial conditions
            if (randomnumber <= BUSY_PROBABILITY):
                seconds += 4    # Adds time to realize person is busy
            elif (randomnumber > BUSY_PROBABILITY and randomnumber <= AVAILABLE_PROBABILITY):
                seconds += 26   # Adds time to realize person is unavailable
            else:
                seconds += 0
                break
        else:   # If we have passed maximum number of redials
            print("Did not answer")

    print("Probability", randomnumber, "gives", seconds, "seconds")


# # For question 2A
# for i in range(customer_limit):     # Iterates over the span of customers
#     if(i >= 51 and i <= 53):   # Checks for the range we need
#         print("Value for i =", i, "is", rannumgen())        # Prints the values
