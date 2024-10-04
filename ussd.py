usrn=str(input("Enter your username :"))
pssd=str(input("Enter the password :"))
if pssd != "password":
	print("Invalid password")	
else:
	class login():
				
			def options():
				print("1.Check details\n")
				print("2.Edit details\n")
				print("3.Quit")
			ussd="*678#"
			
			iussd=str(input("Enter code :"))
			if iussd==ussd:
				options()
			else :
				print("Invalid ussd,try again")
				iussd2=str(input())
				if iussd2==ussd:
					options()
				else:
					print("Try again later...")
			
			
			def options1():
				print("1.Username is :",usrn)
				print("2.Password is :",pssd)
			def options2():
				print(usrn)
				print(pssd)
				usrn2=str(input("Enter new user name :"))
				pssd2=str(input("Enter new password:"))
				usrn=usrn2
				pssd=pssd2
			
			choice1=int(input())
			if choice1==1:
				options1()
			elif choice1==2:
				options2()
			else:
				print("Invalid Choice")
		


		