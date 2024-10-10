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
    print (x / y)
else:
    print ("You can't do that") 
    