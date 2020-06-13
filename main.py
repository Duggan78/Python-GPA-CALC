# Welcome To My GPA Calculator!!!!
# I made one of these in Java and found it helped my understanding so I am going to do it in Python
# Things to know- This does not calculate weighted averages, only unweighted.
# I am going to default to 5 school classes for this calculator.

# declaring the variables first is probably not needed but it helps for organization.
GPA1 =()
GPA2 =()
GPA3 =()
GPA4 =()
GPA5 =()
# yes I know, Capitalizing the first word in the variable name is not how to properly name a variable
# Just doing it for looks right now


# Going to set the value of each variable using the input function
# Not sure if "function" is the correct name for this but.. oh well!

GPA1 = input(print("enter your grade *in percent* that you have in your first class: "))
GPA2 = input(print("enter your grade *in percent* that you have in your second class: "))
GPA3 = input(print("enter your grade *in percent* that you have in your third class:"))
GPA4 = input(print("enter your grade *in percent* that you have in your fourth class:"))
GPA5 = input(print("enter your grade *in percent* that you have in your fifth class:"))

# adding up the total of each grade before
GPAsum = int(GPA1) + int(GPA2) + int(GPA3) + int(GPA4) + int(GPA5)
print(int(GPAsum))

# here is the correct unweighted GPA Number
gpaNumber = int(GPAsum) / 5
print(int(gpaNumber))

# Going to create a long if statement with embedded else if statements.
# This is going to be used to output what the GPA would roughly be on the 4.0 scale.
# This is unweighted so AP and Honors classes will not count.
if gpaNumber >= 93:
    print("4.0")
elif gpaNumber >= 90:
    print("3.7")
elif gpaNumber >= 87:
    print("3.3")
elif gpaNumber >= 83:
    print("3.0")
elif gpaNumber >= 77:
    print("2.3")
elif gpaNumber >= 73:
    print("2.0")
elif gpaNumber >= 70:
    print("1.7")
elif gpaNumber >= 67:
    print("1.3")
elif gpaNumber >= 65:
    print("1.0")
elif gpaNumber < 65:
    print("0... you have failed badly.")

# That was pretty easy. Bot Gavin Belson will be next.







