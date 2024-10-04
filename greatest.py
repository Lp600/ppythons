numbs=[]
f = int(input("Enter first number : "))
s = int(input("Enter second number : "))
t = int(input("Enter third number : "))

def toNumbs(f,s,t):
	global nums
	numbs.clear()
	numbs.append(f)
	numbs.append(s)
	numbs.append(t)
	print(numbs)
def greaTer():
	global numbs
	greatest = max(numbs)
	return greatest
	print("Greatest is : ")	
toNumbs(f,s,t)
g = greaTer()
print("Greatest is : ",g)
