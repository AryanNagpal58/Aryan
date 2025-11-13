name = "Aryan"
print("Hello, ", name)

def add(a,b):
    print(a + b)

add(40,60)

def add(a,b):
    return a + b

#definition of the word add is not static within the computer's memory

c = add(a=40, b=60)
print(c)

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    #else:
        #return "Zero"
    
#print(check_number(0))

#def can_vote(age, is_citizen):
   # if age >= 18 and is_citizen:
   #     print("You can vote!")
   # else:
   #     print("You cannot vote")

#can_vote(19, True)

#def is_weekend(day):
#    if day == "Saturday" or day == "Sunday":
#       return "It's the weekend!"
#    else:
#        return "It's not the weekend"
    
#    print(is_weekend("Sunday"))

#for i in range(5):
#    print(i)

'''
fruits = ["Apple", "Banana", "Cherry"]
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

print_fruits(fruits)

def countdown(start):
    while start > 0:
        print(start)
        start -= 1
    print("Lift off!")

countdown(5)

'''