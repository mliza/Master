#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
number = int(input("Please enter a number: "))

if number == 0: 
    print( str(number) +  " is not a valid number! ")
elif number % 2 == 0:
    print( str(number) + " is an even number! ")
else:  
    print( str(number) + " is an odd number! ")

