# This project is made for Emmanuel Ogunjirin (eao5xc) and Kieran Humphrey (kdh8az)
# This is for our Probability project.

# Imports needed for the projects.
import math

# Defines variables to be used in the project
k = pow(2, 14)
customer_limit = 500

# Defines variables that are changing
x = 1000


def rannumgen():
    """
    Function to provide information for the random number
        generator using the linear congruential random number
        generator rule

    Returns:
        [int]: [value of the linear congruential random number]
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


# Iterate of
for i in range(3):
    print(rannumgen())
