global unaverage
cit104 = int(input("Enter marks for CIT 104 : "))
cir206 = int(input("Enter marks for CIR 206 : "))
cis221 = int(input("Enter marks for CIT 104 : "))
cit421 = int(input("Enter marks for CIT 104 : "))
cit117 = int(input("Enter marks for CIT 104 : "))
unaverage = (cit104+cir206+cis221+cit421+cit117)/5
def grdFinder(unaverage):
	print("Average : ",unaverage)
	if unaverage < 39:
		print("Grade : F\nComment : RESIT")
	elif unaverage < 49:
		print("Grade : D\nComment : BY A WHISKER")
	elif unaverage < 59:
		print("Grade : C\Comment : AVERAGE")
	elif unaverage < 69:
		print("Grade : B\GOOD")
	elif unaverage <= 100:
		print("Grade : A\nComent : WELLDONE")
grdFinder(unaverage)