# --- 3.1 List Operations --- #

favorite_foods = ["Pizza", "Sushi", "Steak", "Cheeseburger", "French Fries"] # Initial string list of favorite foods
print(favorite_foods[1]) #Printing the second item in the list, Sushi
print(favorite_foods[-1]) #Printing the last item in the list through negative index, French Fries
favorite_foods.append("Tacos")#Adding the item of Tacos to the list of strings

favorite_foods.insert(0, "apple")
# I was given an error while running this code because I had switched
# the placement of the String and the index
del favorite_foods[2]
print(len(favorite_foods))
# I was given an error again when trying to print this statement
# because I had ddded the len statement to the end of the list instead of putting the brackets of len()
# Rewrote as seen so that the list was instead of the length function so that VScode could read it properly as the
# value for the length of that list

for food in favorite_foods:
    print(food.upper()) #Printed a version of the list with each food being in full caps

new_list = favorite_foods[-1:1] #Created list going from end to start with nothing in between, meaning just the last and first items in the list

for food in favorite_foods:
    if food == "potato":
        #If the string was equal to the string 'potato', it would be dinged, but only if the full string was labeled 'potato' and nothing else
        print("A potato!")
    else:
        print("No potato!")

# --- 3.2 Slicing and Striding --- #

numbers = list(range(21))


def get_first_15(numbers):
    new_list = []
    #creates a new list for the returned output
    for number in numbers:
        if number < 15:
            #makes it so that only the numbers less than 15, or the first 15 from 0-14, wil be a part of the new list
            new_list.append(number)
    return new_list

def get_every_5th(lst):
    new_list = lst[::4]
    #Uses striving so that, from the index of zero, every 5th item is taken and put into the new list
    return new_list

def reverse_and_stride(lst):
    new_list = []
    i = 1
    while i <= len(lst):
        new_list.append(lst[-i])
        #Creates a new list, and appends all of the items from the original list but it reverse order
        i += 1
    #Makes the returned reversed list stride so that only every 3rd item is actually given as a part of the output for the list
    return new_list[::2]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)

# --- 3.3 Nested Lists --- #

nested_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nested_numbers[2][0:3])
#Nested list, printing the values of the 3rd row
print(nested_numbers[1][1])
#Nested list, printing the second column of the second row
nested_numbers.append([10, 11, 12])
print(nested_numbers)

def sum_nested(nested_numbers):
    sum = 0
    for row in nested_numbers:
        for column in row:
            #nested for loop to go through every item for each row, and then through each row
            sum += column
    return sum


def create_5x5():
    new_list = []
    number = 1
    for i in range(5):
        # While an error sign did not show up for this, there was an error here because I put my range as range(4), which only gave me 4 rows instead of 5
        # I fixed this by rewriting it as 'for i in range(5)'
        row_list = []
        for j in range(5):
            row_list.append(number)
            number += 1
        new_list.append(row_list)
    return new_list

list_5x5 = create_5x5()


def replace_multiples_3(list):
    #general error because this only returned an empty list, because my original code tried to create a new list that was
    #already an empty 5x5 nested list. Instead, I fixed this by starting it off new_list as a normal empty list, and then adding in lists
    #independetly with my nested for loops. I had some help from ChatGPT to understand and solve my error, which I hope is okay
    new_list = []
    for row in list:
        row_list = []
        #I had similar errors here to what I have before, where I was getting the output as just the original list
        #It seems that originally, I tried to assign every value that was a multiple of three the question mark, by calling
        #the item as list[row][column], and in doing so, it would only be a temporary change instead of a permanent change.
        #To fix this, I rewrote it with a new, empty list, and appended all items from the original list, except for the multiples of 3,
        #which I then appended the question marks instead. Again, I was able to get some help from ChatGPT when I was having trouble with some of this code, I hope that's okay.
        for column in row:
            if column % 3 == 0:
                row_list.append("?")
            else:
                row_list.append(column)
        new_list.append(row_list)
    return new_list

new_5x5_list = replace_multiples_3(list_5x5)

def not_equal_to_question(list):
    new_list = list
    sum = 0
    for row in new_list:
        for column in row:
            if column != "?":
                sum += column
            
    return sum

sum = not_equal_to_question(new_5x5_list)

    

# --- 4.1 Dictionary Operations --- #

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
# Created dictionary with keys and items for names and ages, respectively

print(ages["Katie"])
ages["Mariam"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for key, value in ages.items():
    print(f"{key}: {value}")


# --- 5.1 VS Code --- #

# --- 5.2 In Your VS Code Terminal --- #
print(replace_multiples_3(list_5x5))

# --- 5.3 On Your Terminal Application --- #









