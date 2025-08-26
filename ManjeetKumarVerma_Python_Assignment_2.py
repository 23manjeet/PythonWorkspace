# Python Basics: Variables, Operators, Input/Output
# -------------------------------------------------

# Q1: Write a Python program to store your name in a variable and print a welcome message.
# name = "Manjeet"
# print(f"Hello {name}. Welcome!")

# Q2: Create a variable a = 10 and b = 5. Print their sum, difference, and product.
# a = 10
# b = 5
# print("sum: ",a+b)
# print("difference: ",a-b)
# print("product: ",a*b)

# Q3: Write a program to take input of your age and display: "You are X years old".
# age = int(input("Enter your age: "))
# print(f"You are {age} years old")

# Q4: Assign three values to variables in one line and print them.
# a,b,c = 10,20,30
# print(a,b,c)

# Q5: Write a program to check if two numbers (input by user) are equal.
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# if(a==b):
#     print("The two numbers are equal.")
# else:
#     print("The two numbers are not equal.")

# Q6: Use the not operator to reverse a boolean expression.
# is_true = True
# print(not is_true)

# Q7: Find the floor division and modulus of 17 and 4.
# print("Floor division of 17 and 4 is: ",17//4)
# print("Modulus of  17 and 4 is: ",17%4)

# Q8: Take two inputs: a name and a city, and print a formatted string using f-strings.
# name = input("Enter a name: ")
# city = input("Enter a city name: ")
# print(f"{name} lives in {city}")

# Q9: Check if the character 'e' exists in the string "elephant".
# my_string = "elephant"
# if('e' in my_string):
#     print(f"e exists in {my_string}")
# else:
#     print(f"e doesn't exist in {my_string}")

# Q10: Use the is operator to compare two identical integers.
# a = 2
# b = 3
# print(a is b)

# Q11: Use the += operator to increase a number from 5 to 15 by adding 10.
# a = 5
# a += 10
# print(f"after adding 10 new value is {a}")

# Q12: Write a program to display the result of (6 > 3) and (4 == 4).
# print(6>3 and 4==4)

# Q13: Take a string input and use print() to print each word with a Space in between (use sep=' ').
# inputString = input("Enter your String: ")
# inputString=inputString.split()
# print(*inputString,sep=" ")

# Q14: Write a program using input() to take a name and age and print a greeting like: “Hi John, you are 21 years old!”
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hi {name}, you are {age} years old!")

# Q15: Use the print() function with end=" " to print numbers on the same line.
# for i in range(1,5):
#     print(i,end=" ")

# Q16: Write a program to calculate and display the result of 5 ** 4.
# print(5**4)

# Q17: What’s the output of print("Hi", "there", sep="__")? Try running and explaining it
# print("Hi", "there", sep="__") #print statement has two values, and we are using two underscore as a seperator for the two values.

# Q18: What happens if you try:
# age = input("Enter age: ")
# print(age + 5)
# By default input function converts everything entered to string. So if we don't typecast the age input
# we are basically inserting a string in age, and a string + integer is going to give an error.

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Git basics
# -----------
# Q1: What command initializes a new Git repository?
# ans: git init

# Q2: What’s the command to check the current Git status of a project?
# ans: git status

# Q3: Write the Git command to configure your email globally  
# ans: git config --global user.email "your_email" 
 
# Q4: Write the sequence of commands to:
#       Stage all files
#       Commit them with the message "First commit"
# ans: a) git add fileNames
#      b) git commit -m "First commit"

# Q5: What does git clone <url> do?
# ans: This command is used to create a local copy of an existing Git repository in Github using a remote URL.

# Q6: How do you create and switch to a new branch called feature-homepage?
# ans: git checkout -b feature-homepage

# Q7: What does the git pull command do?
# ans: It takes the latest changes in the github repository and copy it to our local repository.

# Q8: You made changes, but now want to undo them before staging. Which command helps?
# ans: git restore . -> To undo all the changes
#      git restore fileNames -> To uno the changes of only the specified files

# Q9: What’s the use of .gitignore?
# ans: .gitignore is a special file , if you add any files name in it the files will be ignored 
#       i.e we can't add, commit or push the files added in .gitignore

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Python Medium
# --------------
# Q1: Write a Python program that takes two inputs, compares them, and prints:
#       "First is greater"
#       "Second is greater"
#       "Both are equal"

# input1 = input("First input: ")
# input2 = input("Second input: ")

# if(input1>input2):
#     print("First is greater")
# elif(input2>input1):
#     print("Second is greater")
# else:
#     print("Both are equal")


# Q2: Use all arithmetic operators with two variables x = 15, y = 4 and print results in clear format.

# x = 15
# y = 4

# print("x+y: ",x+y)
# print("x-y: ",x-y)
# print("x*y: ",x*y)
# print("x/y: ",x/y)
# print("x%y: ",x%y)
# print("x**y: ",x**y)
# print("x//y: ",x//y)


# Q3: Take input for marks and print grades using this logic:
#       >90: Excellent
#       >70: Good
#       Else: Needs Improvement

# marks = float(input("Enter marks: "))
# if(marks>90):
#     print("Excellent")
# elif(marks>70 and marks<=90):
#     print("Good")
# else:
#     print("Need Improvement")


# Q4: Write a program using logical operators to check if a number is between 50 and 100.

# number = int(input("Enter a number: "))
# if(number>50 and number<100):
#     print("True")
# else:
#     print("False")


# Q5: Create a program that takes two inputs: num1, num2, and:
#       Adds them
#       Prints whether the sum is even or odd

# num1 = int(input("Enter 1st input: "))
# num2 = int(input("Enter 2nd input: "))

# sum = num1+num2

# if(sum%2==0):
#     print("Sum is Even")
# else:
#     print("Sum is odd")


# Q6: Write a small program using input() to ask for a number, and:
#       Check if it's divisible by 5 and 3
#       Print appropriate message

# num = int(input("Enter a number: "))
# if(num % 5 ==0 and num % 3 == 0):
#     print("The provided number is divisible by 5 and 3")
# else:
#     print("The provided number is not divisible by 5 and 3")


# Q7: Demonstrate bitwise AND and OR with values 6 and 3, and explain the result in a comment.

# a = 6      # in binary: 110
# b = 3      # in binary: 011

# print(a & b)  # Output: 2
# # 110 & 011 = 010 = 2 (decimal)

# print(a | b)  # Output: 7
# # 110 | 011 = 111 = 7 (decimal)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Git Scenario Based Questions
# ----------------------------
# Q1: You and your friend edit the same file. After pulling their changes, Git shows a conflict.
#       What are your next steps to resolve it?

# ans: My first step would be to see the file having conflict by using -> git status
    #    Then I have to open the file manually in a code editor, and see which changes are to be kept
    #    in code(my friends changes, my changes or both the changes). After the conflict is resolved we will add
    #    the file to staged area, commit it and push the files.

# Q2: You want to contribute a feature to a project hosted on GitHub.
#       What steps do you take from creating a branch to merging it via a pull request?

# ans: First I will create a separate branch for my changes using the command "git checkout -b <branch_name>".
#     This will create a new branch and swith in to the branch. After switching in the branch I will do my chagnes in code.
#     Then I will add the changes to staging area by using "git add <file_names>". Then commit the changes by using "git commit -m 'message'".
#     Now I will push the code in remote repository by using "git push origin <branch_name>".
#     After the local process is done we will go to github and create a new pull request for the changes we pushed. This pull request
#     will be reviewed by someone , if correct then the pull request will be accepted and then the branch changes will be merged
#     in the main branch.

# Q3: What’s the difference between git reset --soft HEAD~1 and git checkout -- <file>? When would you use each?
# ans: "git reset --soft HEAD~1" deletes the last commit but keeps the changes in staged area.
#     "git checkout -- <file>" reverts only the specified files in your working directory back to their last committed state,
#     discarding any changes made since the last commit.

# Q4: How can code reviews improve code quality? Mention two benefits.
# ans: Code reviews can help to catch bugs and issues in our  code. 
#     It also helps in fast development of bug free code.

# Q5: In a GitHub repo, you’re on a branch and want to merge your code into main.
#       What Git commands would you run?
# ans: step1= switch to main branch in local = "git checkout main"
#     step2= pull the latest code in main branch from github to avoid any conflicts in future. = "git pull origin main"
#     step3= merge the code of your branch in the main branch = "git merge <branch_name>"
#     step4= push the code to main in github = "git push origin main"

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Python + Git Medium
# -------------------
# Q1: You're working in a team of 4. Two members pushed changes to the same file.
#   Simulate a small scenario:
#       You make a change
#       Another person edits the same line
#       Show how Git would display the conflict and how you’d manually fix it.

# ans: Suppose our project has a file name AdminUser.txt. In the file there is a variable adminUser having a value "ABC".
#     Now I changed the value of the variable to "Manjeet" and pushed and merged the code in main branch.
#     Another person changed the variable to "Devin" in his branch and trying to push the code in main. He will get a conflict
#     as we both have changed the same line of code, so git detected and overlapping text and thus the merge conflict.
#     Now git will display the conflict as this:
#     <<<<<<< HEAD
#     adminUser = "Manjeet"
#     =======
#     adminUser = "Devin"
#     >>>>>>> other-branch

#     As we get the merge conflict we need to choose which line of code we want to keep and then push the code manually.


# Q2: Write a Python program that:
    # Takes a user's name, age, and city.
    # Checks if age > 18.
    # If yes, prints: “Hello , you are eligible to vote in .”
    # Else: “Sorry , you are too young.”

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# if(age>18):
#     print("Hello , you are eligible to vote in .")
# else:
#     print("Sorry , you are too young.")

# Q3: Simulate the following Git workflow in 5 commands:
#   You clone a repo, create a branch, make changes, commit, and push it.

# ans: a) git clone <url>
#     b)git checkout -b <branch_name>
#     c)after making changes, git add .
#     d)git commit -m "message"
#     e)git push origin <branch_name>


# Q4: Write a Python snippet using at least 3 different operators (bitwise, logical, comparison) in a real-world context (e.g., security check, eligibility, etc.)

# age = 20
# has_permission = True
# flags = 6  # binary 110

# # Comparison operator: check if age is at least 18
# is_adult = (age >= 18)

# # Bitwise operator: check if the 2nd bit (value 2) is set in flags
# has_flag = (flags & 2) != 0

# # Logical operator: check if user is adult and has permission and the flag
# if is_adult and has_permission and has_flag:
#     print("Access allowed")
# else:
#     print("Access denied")


# Q5: You accidentally committed sensitive data. How would you undo the last commit but keep changes in your working directory? Then re-commit without the sensitive file.

# ans: To undo the last commit I will use:- git reset --soft HEAD~1
#     To remove the sensitive file from staging area:- git restore --staged <sensitive-file-path>
#     Now simply commit the files in staged area:- git commit -m "changes without sensitive file"