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
#     will be verified by someone , if correct then the pull request will be accepted and then the branch changes will be merged
#     in the main branch.

# Q3: What’s the difference between git reset --soft HEAD~1 and git checkout -- <file>? When would you use each?

# Q4: How can code reviews improve code quality? Mention two benefits.
# Q5: In a GitHub repo, you’re on a branch and want to merge your code into main.
#       What Git commands would you run?

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Python + Git Medium
# -------------------
# Q1: You're working in a team of 4. Two members pushed changes to the same file.
#   Simulate a small scenario:
    #   You make a change
    #   Another person edits the same line
    #   Show how Git would display the conflict and how you’d manually fix it.
# Q2: Write a Python program that:
    # Takes a user's name, age, and city.
    # Checks if age > 18.
    # If yes, prints: “Hello , you are eligible to vote in .”
    # Else: “Sorry , you are too young.”
# Q3: Simulate the following Git workflow in 5 commands:
#   You clone a repo, create a branch, make changes, commit, and push it.
# Q4: Write a Python snippet using at least 3 different operators (bitwise, logical, comparison) in a real-world context (e.g., security check, eligibility, etc.)
# Q5: You accidentally committed sensitive data. How would you undo the last commit but keep changes in your working directory? Then re-commit without the sensitive file.