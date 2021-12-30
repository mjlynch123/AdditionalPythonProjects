# 1. Ask user to input a number 
# 2. Print out a list of all divisors of the number.

# Get numbers in a range from 1 to 1000, we will cap the amount of divisors 
# to between these numbers.

number_inp = int(input("Please enter a number between 1 and 30: "))
divisor_list = []

for number in range(1, 1001):
    # Now we check to see if the number in the range is divisible by the inputted number.
    if number % number_inp == 0:
        # If it is we will append the number to the list
        divisor_list.append(number)

print(divisor_list)