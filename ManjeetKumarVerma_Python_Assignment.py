# ---------------------------------------------------Part A-----------------------------------------------------------------------
'''
Section 1:
    Question 1 : Explain one key difference in Python installation on Windows, Mac, and Linux.

    Answer:In Linux we have Python installed by default but the python version may be older, so we need to update it using terminal commands, 
            infact I couldn't find a python installer for linux.
            For Windows and macOS we have got the installer files, but we can install it using CLI as well as the installer 
            that can be downloaded from Pythons official site.

    
    Question 2 : What is the purpose of a virtual environment (venv)?

    Answer: The virtual environment allows us to have a saparate environment different form the global or other virtual environments,
            where we can have our own required versions of different dependencies without disturbing other environments.
    
    
    Question 3 : Compare venv vs conda in two points.
    
    Answer : a)venv is built-in with Python, while Conda requires installing Anaconda.
             b)Both can be used for environment management, but venv is specifically for Python, and conda can be use by
               multiple programming languages.
    
    
    Question 4 : Write the command to create and activate a venv on: Windows , Linux/Mac
    
    Answer : Windows->
                        python -m venv <environment name>
                        <environment name>\Scripts\activate
             Linux/Mac->
                        python -m venv <environment name>
                        source <environment name>\bin\activate
    
    
    Question 5 : Why is isolating dependencies important when working on multiple projects?
    
    Answer :  a) It is easy to add or remove dependencies required for a project without affecting projects in other environment.
              b) There are cases when differernt projects require different verisons of the same dependency, in such case
                 having a different environment for the project helps.

Section 2:       
    Question 1 : List two advantages of using Jupyter Notebook over a standard IDE.
    
    Answer : a)Jupiter Notebook has small cells in which we can run small codes for learning and testing.
             b)Jupyter allows you to combine live code, markdown text, mathematical equations, and visualizations in the same document, 
               making it ideal for creating well-documented analyses, reports, and tutorials.
    
    
    Question 2 : What is the main difference between VS Code and Jupyter Notebook for Python development?
    
    Answer :VS Code is a general-purpose code editor and integrated development environment (IDE), 
            while Jupyter Notebook is an environment that allows you to write and run code in individual cells,
            immediately see outputs just below each cell.


    Question 3 : Write two CLI commands to:
                    Check Python version
                    Install a package using pip

    Answer : a) python --version
             b) pip install package_name


    Question 4 : Explain the use of pip freeze > requirements.txt.
    
    Answer :This command will write list of all the python packages and their version installed, 
            in a file named requirement.txt


    Question 5 : What are shell shortcuts? Give two examples.
    
    Answer : Shell shortcuts helps us to write the shell scripts easier and faster. Two examples are:
             a) We can press the up arrow key to run the previous commands given in the shell
             b) We can use tab to complete a partial script

Section 3:
    Question 1 : Name two common debugging techniques in Python.
    
    Answer : We can use print statements to debug the code. Or there is an inbuilt python debugger (pdb)
             which allows us to set breakpoints which will pause the execution flow when it reache the breakpoint.


    Question 2 : What are dot-files? Give two examples and their purpose.
    
    Answer : Dot-file are hidden files whose name starts with a dot(.) , these files generally contains settings and configurations
            relate to Python working environment.
            a) .flake8 = it contains configurations for Flake 8 which is a popular code linter.
            b) .pylintrc = it contains configuration file for the Pylint tool, 
                which performs static code analysis and enforces coding standards


    Question 3 : Explain the difference between hard coding and using variables.
    
    Answer :Variables! As the name suggests , something that can vary depending upon the situation. Hard coding 
            means restricting the application to work on different real world scenarios. If we use variables then depending 
            upon the situations and input provided the output will vary. But if we hardcode everytime we will get the same result.

    
    Question 4 : Why are keyboard shortcuts important for a developer’s productivity? Give two examples.
    
    Answer : Keyboard shortcuts helps a developer in his day to day life of coding as it reduces the time and helps them 
            to remain focused in the code rather than doing other stuffs.
            Ex: Two popular examples are copy(ctrl + c) and paste(ctrl + v)


Section 4:
    Question 1 : What is the purpose of refactoring code? Give an example scenario.
    
    Answer : By refactoring we make our code cleaner, simpler and easy to understand.
             Two examples of refactoring->
             a) giving meaningfull name to the variables for better understanding of the code
             b) removing duplicates and unnecessary code blocks
             

    Question 2 : Mention two VS Code shortcuts that improve coding efficiency.
    
    Answer : a) placing the cursor in different places while pressing alt key lets you write same code 
            in multiple places at a time, it's very useful when we want to write repetative codes.
            b) ctrl + ` will instantly open the vs codes integrated terminal.
    
    
    Question 3 : Why should developers maintain code snippets or templates?
    
    Answer : Developers should maintain code snippets or templates because they save time and effort by avoiding 
            repetitive coding tasks, promote consistency and standardization in code style and structure, and reduce 
            errors by using pre-written, tested code blocks.


    Question 4 : Name one commonly used dot-file for Python environment setup and its function.
    
    Answer : One commonly used dot-file for Python environment setup is the .env file. Its function is to store 
            configuration settings, API keys, and other sensitive environment variables in a plain text format.


'''


# -----------------------------------------------------Part B------------------------------------------------------------------------

# --------------------Section 1---------------------------

# Question 1 : Print “Hello, Python World!”.

# print("Hello, Python World!")


# Question 2 : Store your name, age, and city in variables and print them in a single line.

# name,age,city = "Manjeet",25,"Banglore"
# print(f"My name is {name} ,I am {age} years old, I live in {city}")


# Question 3 : Write a program to take user input for name and greet them

# name = input("Please enter your name: ")
# print("Hi",name, ", Welcome!")


# Question 4 : Convert temperature from Celsius to Fahrenheit.

# celsius = float(input("Enter the temperature in celcius: "))
# farenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C is equal to {farenheit}°F")


# Question 5 : Write a program to swap two numbers without using a third variable

# a = 2
# b = 3
# a = a+b
# b = a-b
# a = a-b
# print(f"a is {a}, b is {b}")


# Question 6 : Create a program that calculates the square and cube of a number.

# a = 2
# print(f"square of {a} is {a**2} and cube of {a} is {a**3}")


# Question 7 : Take three numbers as input and print the largest.

# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))
# c = int(input("Enter the 3rd number: "))
# print(max(a,b,c))


# Question 8 : Write a program to calculate the sum of all elements in a list.

# a = [2,3,4]
# count = 0
# for i in a:
#     count+=i
# print(f"sum of all elements in the list is: {count}")


# Question 9 : Write a script that checks Python version using sys module.

# import sys
# print(f"Python version: {sys.version}")


# Question 10 : Write a script that takes user input and saves it to a file named output.txt.

# fileInput = open("D:\\oputput.txt","w")
# userInput = input("Enter the text to show in the file: ")
# fileInput.write(userInput)
# fileInput.close()


# -------------------------section 2---------------------------------

# Question 1 : Write a script to count the number of words in a given string.

# givenString = "Hello, Python World!"
# givenString = givenString.split(" ")
# print(f"The number of words in the given string is: {len(givenString)}")


# Question 2 : Take a sentence from the user and print:
    # Total words
    # Total characters (excluding spaces)

# usersSentence = input("Enter your sentence: ")
# usersSentence = usersSentence.split(" ")

# print(f"total words in the sentence is : {len(usersSentence)}")

# count = 0
# for i in usersSentence:
#     count+=len(i)
# print(f"total character in the sentence is : {count}")



# Question 3 : Write a program to simulate a simple calculator (add, subtract, multiply, divide).

# def add(a,b):
#     print(f"The sum is {a+b}")
# def sub(a,b):
#     print(f"The difference is: {a-b}")
# def mul(a,b):
#     print(f"The product is: {a*b}")
# def div(a,b):
#     print(f"The division is: {a/b}")
# while(True):
#     print("Choose 1 for Add")
#     print("Choose 2 for Sub")
#     print("Choose 3 for Mul")
#     print("Choose 4 for Div")
#     print("Choose 5 for Exit")
#     choice = int(input("Enter you choice: "))
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the second number: "))
#     match choice:
#         case 1:
#             add(a,b)
#         case 2:
#             sub(a,b)
#         case 3:
#             mul(a,b)
#         case 4:
#             div(a,b)
#         case 5:
#             break


# Question 4 : Take a comma-separated list of integers from input, then print:
    # Sorted list
    # Sum of numbers

# stringLst = input("Enter comma-separated list of integers: ")
# stringLst = stringLst.split(",")

# print("Sorted List: ",end=" ")
# stringLst.sort()
# print(stringLst)

# count = 0
# for i in stringLst:
#     count += int(i)
# print("Sum of numbers: ",count)


# Question 5 : Write a script that reads a text file and counts how many times the word “Python” appears.

# texts = open("D:\\Test.txt","r")
# txtString = texts.read()
# print(f"The word \"Python\" appeared {txtString.count("Python")} times.")
# texts.close()


# Question 6 : Write a program to generate a multiplication table for a given number up to 10.

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n}X{i}={n*i}")


# Question 7 : Create a script that prints the current working directory using os module.

# import os
# print(os.getcwd())


# Question 8 : Write a program to create and activate a virtual environment using Python code.

# import venv
# venv.create('myenv', with_pip=True)
# print("Virtual environment 'myenv' created.")

# import numpy as np

# a = np.array([1,2,3])
# b = np.array([4,5,6])

