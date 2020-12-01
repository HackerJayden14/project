import func

title = {"- Operators -"}
operators = ["Add","Subtract","Multiply","Divide"]
for i in title:
	print(i,"\n")
	for j in operators:
		print(" ",j)
		
print()
while True:
	user_input = input("Enter an Operator: ")
	if user_input in operators:
		break
	else:
		print("Invalid choice. Choose another operator.")
		continue


if user_input == operators[0]:
    f = int(input("Enter your first number: "))
    s = int(input("Enter your second number: "))
    print()
    print("Answer: {}".format(func.plus(f,s)))

elif user_input == operators[1]:
    f = int(input("Enter your first number: "))
    s = int(input("Enter your second number: "))
    print()
    print("Answer: {}".format(func.minus(f,s)))

elif user_input == operators[2]:
    f = int(input("Enter your first number: "))
    s = int(input("Enter your second number: "))
    print()
    print("Answer: {}".format(func.multiply(f,s)))

elif user_input == operators[3]:
    f = int(input("Enter a number: "))
    s = int(input("Enter divisor: "))
    print()
    print("Answer: %.2f" % (func.divide(f,s)))


while True:
	print()
	while True:
		x = input("Calculate again?(y/n) ")
		if x == "y":
			print()
			while True:
				user_input = input("Enter an Operator: ")
				if user_input in operators:
					break
				else:
					print("Invalid choice. Choose another operator.")
					continue
			if user_input == operators[0]:
				f = int(input("Enter your first number: "))
				s = int(input("Enter your second number: "))
				print()
				print("Answer: {}".format(func.plus(f,s)))
				print()
				
			elif user_input == operators[1]:
				f = int(input("Enter your first number: "))
				s = int(input("Enter your second number: "))
				print()
				print("Answer: {}".format(func.minus(f,s)))
				print()
				
			elif user_input == operators[2]:
				f = int(input("Enter your first number: "))
				s = int(input("Enter your second number: "))
				print()
				print("Answer: {}".format(func.multiply(f,s)))
				print()

			elif user_input == operators[3]:
				f = int(input("Enter a number: "))
				s = int(input("Enter divisor: "))
				print()
				print("Answer: {}".format(func.divide(f,s)))
				print()
				continue
		
		elif x == "n":
			break
			
		else:
			print("Invalid choice")
			continue
	break
