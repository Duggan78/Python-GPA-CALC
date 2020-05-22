# Welcome To My GPA Calculator!!!!
# I made one of these in Java and found it helped my understanding so I am going to do it in Python
# Things to know- This does not calculate weighted averages, only unweighted.
# I am going to default to 5 classes for this calculator.

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

# Pretty happy with this now- I may come back and add some if statements to convert into the 4.0 scale. Not sure yet.
# testing commit












