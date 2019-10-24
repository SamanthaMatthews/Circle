
ans = True

while ans:

	print("Please choose an option below!\n")
	print("1. Calculate circumference")
	print("2. Calculate area")
	print("0. EXIT")
	
	ans = input()
	if ans == "1":

		print("What is the radius of the circle?")
		
		userRadius = float(input())
		
		userCircumference = userRadius * 3.14 * 2
		
		print("The circumference of that circle that has a radius of " + str(userRadius) + " is " + str(userCircumference) + "!\n")
		
	elif ans == "2":
	
		print("What is the radius of the circle?")
		
		userRadius = float(input())
		
		userArea = userRadius * userRadius * 3.14
		
		print("The area of a circle with a radius of " + str(userRadius) + " is " + str(userArea) + "!\n")
		
	elif ans == "0":
	
		break