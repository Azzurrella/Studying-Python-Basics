x = int(input ("Give me a number: "))
y = int(input ("Give me a second number: "))
t = input ("Give me a mathematical act: ")
if (t == "+"):  
    print(x + y)
elif (t == "-"):
    print (x - y)
elif (t == "*"):
    print(x * y)
elif (t == "/"):
    if (y == 0):
        print ("Mamma mia! you cant do that!")
    else:
        print (x / y)
else:
    print ("Mamma mia! You can't do that!")