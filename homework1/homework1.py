# --- 3.1 Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a here is an integer variable, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number that includes decimals

c = 3j
print(c)
print(type(c)) 
'''
c is a complex number, representing partly a real number, which here is 0, and partly
an imaginary number, here represented with j, which is multiplied by 3

'''
d = "hello"
print(d)
print(type(d)) # d is a String, a variable that represents text

e = [1,2,3]
print(e)
print(type(e)) # e is a list of integer variables, variables that are whole numbers without any decimals

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict, a collection of key-value pairs where each key is unique

g = (1,2)
print(g)
print(type(g)) # g is a tuple, an ordered collection of elements that are immutable, meaning those elements cannot be changed

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list of String variables, variables that represent text

i = True
print(i)
print(type(i)) # i is a boolean statement, or 'bool' for short. These variables are
# true or false statements/conditions used for a variety of programs, as inputs, outputs, conditions, etc.

j = None
print(j)
print(type(j)) # j is a NoneType, a class representing a null object, or in other words, the absnence of something, like 0.

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list including a boolean condition, a String variable, and an integer variable

l = str(14)
print(l)
print(type(l)) # l is a String variable that is being used for an integer instead of text.

m = 1e4
print(m)
print(type(m)) # m is a float, created by the formula of 1 x 10^4, where e4 is scientific notation for 10^4, and is read together as a floating-point number

'''
Answers to Questions:
1. I found 9 different data types when writing
and researching these variables.

2. All data types that I found include: int, float, complex, str, list, dict, tuple, bool, and NoneType.

3. Variables b and m have the same data type of float, variables d and l have the same data type of str, and variables e, h, and k
are all of the list data type.

4. The variable "l" had a data type of String, or 'str'. It was not an integer because it was specifically outlined as a String variable
even though it was made up of the integer 14. This means that the number 14 was read as a piece of text instead of as an actual integer value.
The command str() does this by making anything that is included within its brackets be considered a part of a line of text.

5. One more data type - bytes - shown below
'''
byte_var = b"hello"
print(byte_var)
print(type(byte_var)) # byte_var here is a part of the bytes data type, used for storing raw binary data
# such as audio files, images, etc. Here, it is being used for a String of text, but the difference
# is that this object cannot be changed, and is representing the raw byte sequences that make up the text when encoded
# using a specific encoding script


# --- 3.2 Booleans --- #
print(10 > 9)
print(10 == 9)
print(10 <= 9)
print(bool("abc"))
print(bool(123))
print(bool(["apple","cherry","banana"]))
print(bool(True))
print(bool(False))
print(bool(0))
print(bool(""))
print(bool(" "))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(True and False))
print(bool(True and True))
print(bool(False and False))
print(bool(True or False))
print(bool(True or True))
print(bool(False or False))
print(bool(not(False)))
print(bool(not(True)))

'''
Answers to Questions:
- The pattern I notice when expressions return True or False is that 
they will return true if the condition inside of them can be considered true or
if it is just simply containing a piece of data. Otherwise, the output becomes false.

- The expression that slightly suprised me with its results was 'print(bool(0))', as its output
was False. I could see the output from this expression being True since 0 was an integer,
until I realized that 0 could also be read as the absence of data, and since other boolean 
expressions that had present data were given the output of True,
a boolean expression containing only 0 might be shown as False.

- Expression returning True: print(bool((10 > 9) and (4 > 3)))

This expression will return True because the two conditions being tested are both true,
since 10 > 9 is true and 4 > 3 is true. Since both are true, the 'and' condition is met,
and the full boolean comes out to True.

- Expression returning False: print(bool((10 > 5) and (2 > 3)))

This expression will return False because, while the first condition of (10 > 5) is true,
the second given condition of (2 > 3) is false, and if either one of the conditions in a boolean expression
that contains 'and' are false, then the whole boolean expression returns False.
'''

# --- 3.31 Arithmetic Operators --- #

print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2, / performs division
print(5 % 2) # 1, % performs division and outputs remainder
print(3 ** 2) # 9, ** performs an exponentional equation in which the first integer
# is taken to the power of the second integer
print(15 // 2) # 7, // seems to divide the first integer by the second, and round the 
#output down to the next possible integer

# --- 3.3.2 Comparison Operators --- #

print(5 == 2) #
print(10 != 10) #
print (2 < 5) #
print( 12 > 5) #
print(5 <= 6) #
print(1 >= 10) #

# --- Assignments Operators --- #
x = 5
x += 5
x -= 4
x *= 3

# 3.3.4 Logicial Operators --- #
'''
Answer the following questions as comments:
1. The operator 'and' divides a boolean expression into two parts, and will make it so that the
boolean expression returns true only if both conditions linked by the 'and' operator return 
the same value, whether that be True or False.

Expressions with 'and' operator returning True and False, respectively, below.
'''
print(bool((11==11) and (10 > 2)))
print(bool((10==1) and (10 > 2) ))

'''
2. The operator 'or' divides an expression with a boolean output of either True or False. 
However, differently from the 'and' operator, the 'or' operator only needs one of the conditions
it links to to be True for the full expression to output True. Only if both conditions are false
does the expression return False.

Expressions shown below:
'''
print(bool((10 > 5) or (10 < 2)))
print(bool((10 < 5) or (10 < 2)))

'''
3. The operator 'not' reverses what would be the original output from a given expression.
If the original expression would return True, the 'not' operator will make the expression return False,
and vice versa.
'''
print(bool(not (10 < 5)))
print(bool(not (10 > 5)))

'''

More Questions:
1. What is the difference between / and //?
The difference between / and // is that / will divide two integers and
output a float, or decimal number, that is equal to that division equation. 
Using //, on the other hand, will round down the product of the division to the next lowest integer
2. What is the difference between % and //?
The difference between % and // is that the output of % is the remainder from a division equation while
// will output the rounded-down product of a division equation.
3. What operator would you use to calculate the remainder
when dividing two numbers? Give an example?
The operator I would use to calculus the remaind when dividng two numbers would be %.
An example of this has been given below: print(10 % 3), which should output the remaind of 10 divided by 3, 1
'''
print(10 % 3)
'''
4. How do assignment operators work?
Assignment operators work by assigning specific data to the variables they operate on
so that those variables are now equal to specific information.

'''

# --- 3.4 Strings --- #

my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(7 * my_string) # Prints 'hello' seven times in a row with no spaces in between

'''
3.4.1 Questions
1. Slicing is where you select a fraction of the data within an object and extract it.
The manipulations above that used slicing would be any that used the [] brackets to
represent where to start and stop the slicing of an object.
'''
name = "Oski"
print("Hello, my name is", name)

print(f"Hello, my name is {name}")

'''

2. The result is a String of text that includes both the part in quotations and the String variable 'name'.
3. The result is a String of text made by replacing it with its assigned value of 'Oski', and then running the printed String
4. The difference between these two would be that the first function just prints text and then adds the String variable 'name' 
to the end of the print, while the second function prints an F-String,
a String that includes the variable 'name' actually embedded in the text instead of just added on
at the end.

'''

 # -- 3.5 Terminal Commands -- #

'''
1. cd 
-> the 'cd' command changes directories within a terminal, moving from one folder to another
Ex: cd Users

2.ls 
-> the 'ls' command lists the full pathway of a directory, as in all
folders and files used to make up that specific pathway. If a path is not given, it
just lists all files and folders in the directory.
Ex: ls Users

3. ls-a 
-> the 'ls-a' command lists all directories of a specific path,
including some that may be hidden if they begin with a dot. Like the 'ls'
command, if no path is specified, it just lists all objectis in the directory.
Ex: ls-a python_decal_fa25

4. mkdir 
-> the command 'mkdir' creates a new directory, adding it as the newest layer
to a pathway that is being opened.
Ex: mkdir homework2

5. cat 
-> the command 'cat' can be used to display all content of a given file, even more than one
Ex. cat homework 1

6. pwd 
-> the 'pwd' command displays the current pathway that a user is on, listing layer by layer 
each directory
Ex: pwd 'first_name last_name'

7. cd .. 
-> the command 'cd ..' can be used to move up one level within a pathway,
moving from the child directory to the parent directory
Ex: running 'cd..' while on a specific user's directory will take the user to the parent desktop directory

8. cd . 
-> the command 'cd .' can be used to move to the current level within a pathway,
keeping a user in the same directory but in a way refreshing the directory
Ex: running 'cd.' while in a specific folder will keep the user in that folder, but
will show any updates made to that folder in terms of content inside

9. cd ~ 
-> the command 'cd ~' can be used to travel to the home directory, or highest level
directory within the pathway that the user is on.
Ex: running 'cd ~' while on the pathway 'Users/"first_name last_name"/Personal_Files' will return
the user to the home directory of 'Users'

10. cp 
-> the 'cp' command is used to copy files and directories
Ex:

11. mv 
-> the 'mv' command moves files from one given directory to another. It can
also be used to rename a file.
Ex: moving the file 'homework1' from its current directory to the 'python_homework' folder:
mv homework1 python_homework

12. rm
-> the 'rm' command removes a file from a given directory or removes a directory
from a given pathway
Ex: removing the file 'scrap_code' from the folder 'homework1':
rm scrap_code

13. clear
-> the 'clear' command clears out any content within a directory
Ex: to clear out all content in folder 'homework1':
clear homework1

14. grep
-> the 'grep' command allows users to search within one or more files for a specified line of data,
such as strings, expressions, etc. Command 'grep' will then output all lines within a given 
directory that include that specific data being searched for.
Ex: to search for the function 'print(bool(10 > x))':
grep print(bool(10 > x))

Questions:
1. Three other commands would include the 'touch' command, the 'less' command, and
the 'head' command.

    The 'touch' command creates a new empty file within a directory, such as by running:
    touch new_document.py

    The 'less' command runs a given file and displays its output, or may just display the
    content of a text file if it is used for a text file. For example, if there were notes
    shown in comment form in a file labeled 'scrap_notes', the 'less' command can be used as follows:
    less scrap_notes

    The 'head' command displays the beginning portion of one or more files, usually the first
    10 lines by default. This can be used for searching for specific versions of files and/or organizing.
    The example below runs a command asking for the first 10 lines of code for the file 'homework1.py'
    head homework1.py


2. The difference between commands 'ls' and 'ls -a' is that the 'ls -a' command will display files
that start with dot(.), which are otherwise hidden when 'ls' lists out all content.

3. A hiddle file is any file that begins with dot(.), which the command 'ls' will not output as part 
of a list of content by default because files beginning with (.) are read by the command as "clutter" data, ie.,
data that is not worth showing to the user.

4. Three other flags that can be used on the command line include '-tmp','-F', and '-v'.
The '-tmp' flag is used to create temporary directories. They are added to the end
of a 'mkdir' command to make the following file a temporary one.
The '-f' is used with varius other commands, such as 'cp' or 'rm', to force
through a command even if an obstacle is found. It will force a given command to
go through without any further confirmation.
The '-v' flag is used usually in two separate instances. The first use is to display
the more detailed processes done when running a program, including individual file processes
and outputs from different commands. The second use is to display what version of a file
is being shown currently. The first use if more notably shown with '-v' and the second
is usually more seen with '-V'.


'''
