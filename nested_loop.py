
''' Nested For Loops'''

print("__________ Model Code_________")
i = 1
while i <= 5:
    j = 1
    while j <=i:
        print(j, end = " ")
        j = j + 1
    print(" ")
    i = i + 1

# Getting a sense of it: Play around with the print statements
# Ctrl + C to breakout of an infinite loop. 

# if we move the last print statement inside the nested loop we get an infinite loop.
# Why?

print("___ Add Print Statement after j variable init ___")
print(" ")
i = 1
while i <= 5:
    j = 1
    print(f"j now equals {j}")
    while j <=i:
        print(j, end = " ")
        j = j + 1
    print(" ")
    i = i + 1

print("___ Add Print Statement after j = j + 1 ___")
print(" ")

i = 1
while i <= 5:
    j = 1
    print(f"j now equals {j}")
    while j <=i:
        print(j, end = " ")
        j = j + 1
        print(f"j now equals {j}")
    print(" ")
    i = i + 1

    print("___  ___")
print(" ")

#####

print("__________ Model Code_________")
i = 1
while i <= 5:
    j = 1
    while j <=i:
        print(j, end = " ")
        j = j + 1
    print(" ")
    i = i + 1

# Adding print statements to visualise iteration.

print("___ Count Iterations ___")
print(" ")

# The outer loop is a statement of condition - the condition of / for the operation
# Twin conditions?
# Do this 5 times. We are starting from 1. Essentially do this 5 times.

# What is the significance of the indentation of the final print statement?



iterations = 0
i = 1
while i <= 5:
    j = 1
    print(f"j = {j}")
    while j <= i:
        iterations += 1
        print(" ", j, end=" ")
        j = j + 1
    print(f"\n iteration: {iterations}\n")
    print(f"j now equals {j} > 5 means break")
    print(" ")
    i = i + 1

    print(f"Total number of iterations = {iterations}")



# A better version. Maybe remove the second as confusing - though instructive?

iterations = 0
i = 1
j = 1  # Moved outside the outer loop
while i <= 5:
    print(f"j = {j}")
    while j <= i:
        iterations += 1
        print(" ", j, end=" ")
        j = j + 1

    print(f"\niteration: {iterations}\n")
    print(f"j now equals {j} > 5 means break")
    print(" ")
    i = i + 1

print(f"Total number of iterations = {iterations}")


