# This project is made for Emmanuel Ogunjirin (eao5xc) and Kieran Humphrey (kdh8az)
# This is for our Probability project.

# Imports needed for the projects.
import math

# Defines variables to be used in the project
BUSY_PROBABILITY = 0.2
UNAVAILABLE_PROBABILITY = 0.3
AVAILABLE_PROBABILITY = 0.5
k = pow(2, 14)
customer_limit = 500

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

    x_i = ((a * x) + c) % k  # Formula defines in appendix of project
    x = x_i  # Reassigns the previous value
    u_i = x_i / k   # Formula defined in the appendix
    return u_i

# For question 2A uncomment this section to run it.
# for i in range(customer_limit):     # Iterates over the span of customers
#     if(i >= 51 and i <= 53):   # Checks for the range we need
#         print("Value for i =", i, "is", rannumgen())        # Prints the values


# Iterates over the specific range needed
for i in range(customer_limit):
    RECALL_LIMIT = 5  # This is the maximum redial possible
    seconds = 0  # Initial time to start calling someone

    print("<->")  # Separates individuals calls from each other

    for j in range(0, RECALL_LIMIT, 1):     # Redials the user as many times as needed
        randomnumber = rannumgen()  # Runs the random number generator
        seconds += 6  # Initial time to pick up phone and dial a number

        if (randomnumber <= BUSY_PROBABILITY):  # Busy probability
            seconds += 4  # Adds time to realize person is busy
            if(j != 4):  # Checks if we are not on the last try
                print("Probability", randomnumber,
                      "shows user is busy. Redialing...")
        elif (randomnumber > BUSY_PROBABILITY and randomnumber <= AVAILABLE_PROBABILITY):  # Unavailalble section
            seconds += 26  # Adds time to realize person is unavailable
            if(j != 4):  # Checks if we are not on the last try
                print("Probability", randomnumber,
                      "shows user is unavailable. Redialing...")
        else:   # Available section
            # Find the time using the inverse function
            function = -12 * math.log(1 - randomnumber)

            if (function >= 25):    # Checks if time is over what is needed
                seconds += 26   # Adds in the maximum seconds
            else:   # If time is less than what is needed
                seconds += function  # This will be x seconds
                print("Probability", randomnumber, "gives", "function",
                      function, "showing user picked up in", seconds, "seconds")
                break   # Exits the loop for this user

        if(j == 4):  # Checks if we are on the last try
            print("Probability", randomnumber, "gives", "function",
                  function, "showing user did NOT pick up in given time. User picked up in", seconds, "seconds")
