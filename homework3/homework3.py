# --- 3.1 Say Goodbye --- #

def say_goodbye(name):
    #prints "Goodbye,", followed by whatever name that is given as the String argument of the function
    print("Goodbye,", name)

# --- 3.2 Area of a Circle --- #

def circle_area(radius):
    # Calculates '(area of circle) = pi * (r^2)
    pi = 3.14
    circle_area = pi * (radius ** 2)
    print(circle_area)

# --- Subtract, ultiply and Divide --- #

def subtract(a,b):
    # subtracts whatver number 'a' by number 'b'
    return a - b

def multiply(a,b):
    # multiplies number 'a' by number 'b'
    return a * b

def divide(a,b):
    # divides number 'a' by number 'b'
    return a / b

# --- 5.1 What Should I Wear? --- #



def min_and_max_temp(readings):
    min = readings[0] # gives a starting value for the minimum as the first integer in the list of readings
    max = readings[0] # gives a starting value for the maximum as the first integer in the list of readings
    for temp in readings: # runs a for loop through the list of readings, calling each one the 'temp'
        # if the selected integer from the list is less than the current minimum value, then it becomes the new minimum value
        if min > temp: 
            min = temp
        # if the selected integer from the list is more than the current maximum value, then it becomes the new maximum value
        if max < temp:
            max = temp
    # returns here both the minimum and maximum values after looping through the entire list
    return (min, max)

# --- 5.2 Check if it's the Weekend --- #

def is_weekend(day_number):
    # Given that each day in a week is given a number from 1-7, with Monday being 1, Tuesday being 2, etc., a weekend day
    # would be given the number 6 or 7
    # Here, the boolean statement is checking if the given number that represents a day of the week is either 6 or 7, meaning it is the weekend
    # Will return true if it is the weekend, and false if not
    return day_number == 6 or day_number == 7




# --- 5.3 Fuel Efficiency Calculator --- #

def fuel_efficiency(distance, fuel):
    #Using the two variables, distance and fuel, as part of a formula for finding fuel efficiency, by just dividing distance by fuel
    return distance / fuel

# --- 5.4 Secret Code --- #

def encryption(code_number):
    #Creates a remainder variable that will equate to the last digit in whatever number is given,
    #Creates a floor number, which is basically all digits of 'code_number' except the last, by doing division by 10 and rounding down the output
    #then using 'f"{}{}"', creates a string in which that remainder is the first digit in a new number, and the rest of the digits is the floor
    remainder = code_number % 10
    floor = code_number // 10
    output = f"{remainder}{floor}"
    return output

# --- 6.1 Oski Stole Your Power --- #

def power(x,y):
    #Creates an original output of 1, which is what the product of x to the power of y would be if y=0.
    #Them, if y >= 1, that value of output will be multiplied by x. The for loop makes it so that y becomes 1 less every time,
    #so at some point, y=0 and the loop stops, at the same time that output = x to the power of y
    output = 1
    for __ in range(y):
        output *= x

    return output

# --- 6.2 Min & Max with Loops! --- #

# --- 6.2.1 For Loops --- #

def find_min_with_for(list):
    #Gives a starting minimum value as the first value in the list
    min = list[0]
    #Runs through every number in the list, and if it is smaller than the current minimum, it replaces the minimum as the new minimum value
    for number in list:
        if number <= min:
            min = number

    return min


def find_max_with_for(list):
    #Gives a starting maximum value as the first value in the list
    max = list[0]
    #Runs through every number in the list, and if it is larger than the current max, it replaces the max as the new maximum value in the list
    for number in list:
        if number >= max:
            max = number

    return max

# --- 6.2.2 While Loops --- #

def find_min_with_while(list):
    #Gives a starting minimum value as the first value in the list
    min = list[0]
    #Creates an index variable that acts as the position of a value in the list that it tests
    index = 0
    #Runs the index through the length of the list, making the loop go through every value in the list and check and replace
    #the minimum value if it is smaller than the current minimum value
    while index < len(list):
        if min > list[index]:
            min = list[index]
        index += 1

    return min

def find_max_with_while(list):
    #Gives a starting maximum value as the first value in the list
    max = list[0]
    #Creates an index variable that acts as the position of a value in the list that it tests
    index = 0
    #Runs the index through the length of the list, making the loop go through every value in the list and check and replace
    #the maximum value if that current value at the index is greater than the current max
    while index < len(list):
        if max < list[index]:
            max = list[index]

        index += 1

    return max

# --- 6.3 Calculate the Sum --- #

def calculate_sum(number_for_sum):
    #Gives a starting value for the sum of 0, just to initialize the variable
    sum = 0
    #Loops through the following expressions to add the last digit of the given number to the sum, and then delete said digit from the original number
    while number_for_sum >= 1:
        remainder = number_for_sum % 10
        sum += remainder
        number_for_sum = number_for_sum // 10
    #ends with a sum that is equal to all digits from the given 'number_for_sum' added together
    return sum

# --- 7.1 In Your VS Code Terminal: --- #

# --- Chosen function: calculate_Sum --- #

number_for_sum = 54321

result = calculate_sum(number_for_sum)
# The sum of 5, 4, 3, 2, and 1, which should be 15

print("The result of calculating the sum of the digits")
print(f"{number_for_sum}")
print(f"should be: {result}")

# --- 7.2 On Your Terminal Application (Importing Functions) --- #




 





