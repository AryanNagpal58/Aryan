'''
--- 3.1 Vocabulary Review ---
1. Git vs. GitHub

The difference between Git and Github is that Git is a version control system for coding programs in such languages as
python, C++, Java, etc., that allows for tracking in the change of code over time, while GitHub specifically is a website that
hosts GitHub repositories and allows coders to connect and grow their programming with each other. There are local repositories that
are local to the computer, and remote repositories that are shared with others on GitHub.

2. Terminal vs. Command Line

The difference between a terminal and a comand line is that the terminal itself is a software platform that hosts the command line, which is 
then the interface that allows the coder to interact with the computer by use of commands.

3. Local vs. Remote Repository

The local repository is the copy of a program that is on one's own personal computer,
while the remote repository is the public version of said program that is available 
on GitHub and made present and accessible to the entire community.

4. Version Control

Version control is an trait of Git, which basically means that the system of Git is able to 
track the changes in code made by a user over time, allowing for a history of versions for a program that
a user is able to call back on as needed.

5. Staging Area

In git, a staging area is basically the temporary space made to gather and prepare a permanent change to the code of a repository.
It is the space between actually trying to add these changes and it becoming permanent to the updated repository. It also allows 
users to specify what changes they want to be committed and then pushed to the updated repository.

6. git add

The command 'git add' is one of the main three commands use to update a local git repository to be the new version of the
remote repository. This action basically adds any changes made by a programmer in their computer's local copy that they now
want on the remote repository. However, it does not fully add them but not fully, it only adds the changes to the staging area
before they are committed to the remote repository.

7. git commit
The command 'git commit' is the next command for updating the repository on GitHub, and basically records these changes in the 
history of a user's local repository, usually with the addition of a message from the user.

8. git push
The command 'git push' finally uploads changes the commits from the local repository to the remote repository so that the 
remote repository matches the added changes from the staging area.

9. git status

The 'git status' command gives the user a current status of the repository, including what changes have been saved or added to the staging area yet.

10. git pull

The 'git pull' command allows the version of the local repository to be synched with the remote repository's current version.

11. pwd

The 'pwd' command prints the current directory that a user is in, as in the full pathway and any repositories that are entered to
get to where the user is, in the order that they need to be accessed.

12. ls

The 'ls' command lists all pathways within the current directory, 
or in other words, all folders and files that can be accessed from 
the current folder.

13. cd

The 'cd' command allows the user to enter the pathway they type out after putting 'cd', whether it be a direct
repository or a more complex relative repository.

14. nano

The 'nano' command opens a temporary page for which code can be edited in.

15. touch

The 'touch' command creates a new file with the name that is typed right after the word 'touch'. If a file with that name already exists, 
the 'touch' command updates its Git timestamp to the current time, but does not actually change any of the code within the original file.

16. mv

The 'mv' command moves and renames files or directories for a given repository, with the first item typed after it being the item that is moved and 
the next being the new location for said item.

17. rm

The 'rm' command deletes files or directories from a repository.

18. cat

The 'cat' command in Git displays content for an item that is typed right after it, 
which can include specified traits like the type of object, the size, the output, etc.

--- 3.2 A Directory Tree ---

Questions:
• You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
- The command 'pwd' will tell me what my current working directory is.

• The terminal responds by saying you are in ∼/python decal/judy decal. What command
will list all the files in your current working directory?
- The command 'ls' will list all the files in my current working directory.

• Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
You will need to pull the brianna repo repository to find the updated file. What command(s)
will let you move to the correct repository and pull the latest changes?
- The commands that will allow me to move to the correct repository and pull the latest changes, in order,
would be 'cd /../brianna_repo' and then 'git pull origin main'. The first command moves me to the correct repository, and the
second will pull the latest version of the main repository, which should include Brianna's updates.


• How would you move this new homework.py to the homework/ folder in your personal repos-
itory?
- To move this new homework.py to the homework/ folder in my personal repository, I would
use the command line 'mv homework.py /../judy_decal/homework'

• How would you move yourself to the same repository as homework.py?
- I would move myself to the same repository as homework.py by using the 'cd' command as follows:
'cd /../judy_decal/homework'

• You want to see the contents of homework.py in your terminal, how would you do this?
- To see the content of homework.py in my terminal, I would use the command 'cat homework.py'

• Great job! You just finished the homework for this week. What command(s) allow you to
save the changes and push from your local repository to your remote repository?
- The following commands will allow me to save my changes and push from my local repository to my remote repository:
git add .
git commit -m "Done with homework5"
git push origin main

• Oh no! Git gave you the following error. What commands should you call to resolve this
error and push your homework properly? What does the error mean? (i.e. what did “Judy”
do wrong when trying to push?)
The commands that I should call to resolve this error and push my homework properly would be as follows:
git pull origin main
git status
(Once it seems that everything is checked and fine):
git add .
git commit -m "Done with homework5"
git push origin main

- What this error originally means is that the current local repository is not up to date with work
that was added to the remote repository. The command 'git pull origin main' should have fixed this,
and to check the current status, I would also call 'git status'. Once it seems that my local repository is up to date,
I would use the same commands as before to push my changes from the local repository to the remote, i.e. 'git add .',
'git commit -m "Done with homework5"', and 'git push origin main'.


• What absolute path will allow you to move to Recents/?
The absolute path that would allow me to move to recents would be:
'cd ~/Recents/'

--- 3.3 Draw Your Directory Tree ---
 Directory tree drawn and photo added to the homework5 folder


--- 4 Homework 3 Review ----
'''
# --- 4.1 Data Types --- #

#Write a function that takes any input and returns a string indicating its data type.

def checkDataType(data):
    output = type(data)
    return output

# --- 4.2 Conditionals --- #
def evenOrOdd(number):
    if (number % 2 == 0):
        return "Even"
    else:
        return "Odd"
    
# --- 5 Loops --- #
def sumWithLoop(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum

# 6 Homework 4 Review --- #
# --- 6.1 Lists --- #
def duplicateList(list):
    newList = []
    for item in list:
        newList.append(item)
        newList.append(item)

    return newList

# --- 6.2 Debugging --- #
def square(num):
    return num*num

# --- 7 Running Your Code --- #
# --- 7.1 VS Code --- #
# --- 7.2 In Your VS Code Terminal --- #
# Favorite function: sumWithLoop #

list = [50, 23, 45, 36, 11, 45]
print (sumWithLoop(list))


