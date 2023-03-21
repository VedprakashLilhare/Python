number = int(input("Enter number for factorial"));
fact = 1;
if number<0:
    print(" Factorial number is not exist for Nagetive Number");
elif number==0:
    print("Factorial of 0 is 1");
else:
    for i in range(1,number+1):
        fact= fact*i;
    print("Factorial of",number,"is= ",fact)
