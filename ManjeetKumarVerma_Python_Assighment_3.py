
# Python Basics:
# --------------
# Question1: Create a variable of each type: string, integer, float, and boolean. Print their types using type().

# strVar = "Apple"
# intVar = 3
# floatVar = 4.2
# boolVar = True

# print(type(strVar))
# print(type(intVar))
# print(type(floatVar))
# print(type(boolVar))


# Question2: Convert a float value to an integer, and then to a string. Show the output at each step.

# floatVar = 3.5

# intVar = int(floatVar)
# print(intVar)

# strVar = str(intVar)
# print(strVar)


# Question3: Use an f-string to display: "Hello <name>, you are <age> years old".

# name = "Manjeet"
# age = 24
# print(f"Hello {name}, you are {age} years old")


# Question4: Make a list with at least 5 items of different data types. Access and print the second item.

# arr = [2,"Tiger",True,3.5,False]
# print(arr[1])


# Question5: Add a new element to a list using .append() and then remove the last element using .pop().

# arr = [2,"Tiger",True,3.5,False]
# arr.append(4)
# print(arr)

# arr.pop()
# print(arr)


# Question6: Reverse a list using .reverse() and print it.

# arr = [1,2,3,4,5]
# arr.reverse()
# print(arr)


# Question7: Create a dictionary with 3 key–value pairs and print only its keys.

# my_dict = {"a":1,"b":2,"c":3}
# for i in my_dict:
#     print(i)


# Question8: Given two lists keys = ["id", "name", "age"] and values = [101, "Aman", 25], create a dictionary using zip() and print it.

# keys = ["id", "name", "age"]
# values = [101, "Aman", 25]
# my_dict = dict(zip(keys,values))
# print(my_dict)


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Control flow:
# -------------

# Question1: Write a program that checks if a number is greater than, equal to, or less than 100.

# num = int(input("Enter a number: "))
# if(num>100):
#     print("number is greater than 100")
# elif(num == 100):
#     print("number is equal to 100")
# else:
#     print("number is less than 100")


# Question2: Create a program that takes two numbers as input and checks:
#             If both are greater than 10
#             If at least one is greater than 10
#             If neither is greater than 10

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if(num1>10 and num2>10):
#     print("both are greater than 10")
# elif(num1>10 or num2>10):
#     print("at least one is greater than 10")
# elif(num1<10 and num2<10):
#     print("neither is greater than 10")


# Question3: Use a for loop to print all elements in a list along with their index using enumerate().

# lst = [22,45,17,14,32]
# for index,value in enumerate(lst):
#     print(index,value)


# Question4: Write a while loop that prints numbers from 1 to 10, but skips 5 using continue.

# num = 1
# while(num<=10):
#     if(num==5):
#         num+=1
#         continue
#     print(num)
#     num+=1


# Question5: Create two lists of equal length and print their paired elements using zip().

# lst1 = ["a","b","c"]
# lst2 = [1,2,3]
# zipped = zip(lst1,lst2)

# for element in zipped:
#     print(element)

# Question6: Write a for loop to print numbers from 1 to 20, but stop when you reach 15 using break.

# for i in range(1,21):
#     print(i)
#     if(i == 15):
#         break

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Functions:
# ----------

# Question1: Write a function square(num) that returns the square of the given number.

# def square(num):
#     return num**2

# print(square(5))


# Question2: Create a function check_even(num) that returns True if the number is even, else False.

# def check_even(num):
#     if(num % 2 == 0):
#         return True
#     else:
#         return False
    
# print(check_even(43))


# Question3: Write a function greet_user(name) that returns a greeting message using f-strings.

# def greet_user(name):
#     print(f"Hello {name}, Welcome!")

# greet_user("Manjeet")


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Git Essentials:
# ---------------

# Question1: Which Git command stages all files in the current directory?
# git add .

# Question2: What does git commit -m "message" do?
# This command will save all the staged changes to our local repository. 
# The message that we give here can be seen in our commit history.

# Question3: Write the Git command to push changes to the main branch of the remote repository.
# git push origin main

# Question4: Explain in one line what origin means in Git.
# it is a place holder for the remote repository url.



