def case_1(a,b):
	print(a+b)
def case_2(a,b):
  	print(a-b)
def case_3(a,b):
  	print(a*b)
def case_4(a,b):
  	print(a/b)
while True:
	print("1.Addition")
	print("2.Substraction")
	print("3.Multiplicatio")
	print("4.Division")
	print("5.Exit")
	c=int(input("Enter option"))
	if c==1:
	    a=int(input("Enter first no."))
	    b=int(input("Enter second no."))
	    case_1(a,b)
	elif c==2:
	    a=int(input("Enter first no."))
	    b=int(input("Enter second no."))
	    case_2(a,b)
	elif c==3:
	    a=int(input("Enter first no."))
	    b=int(input("Enter second no."))
	    case_3(a,b)
	elif c==4:
	    a=int(input("Enter first no."))
	    b=int(input("Enter second no."))
	    case_4(a,b)
	elif c==5:
		break
	else:
	  print("Invalid number")
	  pass
