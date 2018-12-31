age = 24
# Convert an integer to a string
print("My age is " + str(age) + " years")

# Replacement fields format method
# {0} is the number of parameters
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "January", "March", "May",
        "July", "August", "October", "December"))

print()
print("""January: {2} {3}
February: {0} {3}
March: {2} {3}
Apri: {1} {3}
May: {2} {3} 
June: {1} {3}
July: {2} {3}
August: {2} {3}
September: {1} {3}
October: {2} {3}
November: {1} {3}
December: {2} {3}""".format(28,30,31,"days"))

# This was on Python 2.7
print()
print("My age is %d years" %age )
print("My age is %d %s, %d %s" %(age, "years", 6, "months"))

for i in range (1, 12):
    print( "No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3 ))

print()
print("Pi is approximetly %12.50f" %(22/7))

# Python 3
# Using replace fields {x:y} where x is the parameter to be replaced and y is the width
print()
for i in range (1, 12):
    print( "No. {0:2} squared is {1:4} and cubed is {2:4}" .format(i, i ** 2, i ** 3 ))

# In this example figures are allocated on the left sense
print()
for i in range (1, 12):
    print( "No. {0:2} squared is {1:<4} and cubed is {2:<4}" .format(i, i ** 2, i ** 3 ))

print()
print("Pi is approximetly {0:12.50}".format(22 / 7))

