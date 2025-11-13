
# -- Class 6 Discussion Scratch_Notes --- #

'''
Each function starts with a def statement,
followed by the name of the function.
In the parenthesis are the arguments, the used variables and more

function ends with a colon in python
If we are using a print function, we cannot use the
output from this function later, because it is then not a returned object(?)

We can use the output of a function in other expressions
or functions if the function has an output with a return statement


'''
'''
# --- Class 7 Lecture Notes --- #

numbers = [1, 2, 3, 4, 5, 5, 5]
#print(numbers)

fruits = ["apple", "banana", "cherry"]
#print(fruits)

mixed = ["hellow", 5, True, None]
#print(mixed)

#print(fruits[2])
#print(fruits[0])
#fruits[0] = "grape"
#print(fruits)

#print(numbers)
#numbers.append(6)
#print(numbers)

#print(mixed)
#mixed.insert(1, False)
#print(mixed)

#print(fruits)
#fruits.remove("banana")
#print(fruits)

#print(fruits)
#fruits.pop(0)
#print(fruits)

#for fruit in fruits:
#    print(fruit)

# --- Class 7 Practice Question #1 ---#
colors = ["red", "blue", "purple"]

print(colors[1])
print(colors[-1])
print(colors)
colors.append("yellow")
print(colors)
for color in colors:
    print(color)

# --- slicing and striding --- #
nums = [10, 20, 30, 40, 50, 60]
print(nums)
# slicing, starting at index 1, and stopping after printing the number at index 3, 
# or just 1 minus the ending index
print(nums[1:5])
print(nums[:3])
print(nums[3:])
print(nums[:])

my_nums = [20, 40, 60, 80, 100, 120]
print(my_nums)
print(my_nums[::2])
print(my_nums[1::2])

# --- Class 7 Practice Question #2 --- #
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters[1:5])
print(letters[::2])
print(letters[::-1])
print(letters[-3:])

# --- Dictionaries --- #

student = {
    "name": "Ariana",
    "year": 4,
    "major": "Computer Science"
}

print(student)
print(student["year"])
student["year"] = 5
print(student["year"])

student["school"] = "UC Berkeley"

print(student)

del student["school"]

print(student)


print(student.keys())
print(student.values())

print(student.items())

for key in student:
    print(f"{key} = {student[key]}")

    for key, value in student.items():
        print(f"{key} = {value}")

# --- Class 7 Practice Question #3 --- #

pet = {
    "name": "Luna",
    "type": "cat",
    "age": 3
}

print(pet["name"])
pet["age"] = 4
pet["favorite toy"] = "string"
for key, value in pet.items():
    print(f"{key} = {value}" )

'''






