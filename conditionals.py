day_of_week = input("Enter the day of weeek: ").lower()

print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
	print("I will learn LIVE DevOps")
else:
	print("I will practice DevOps")

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

choice = input("Enter the operation: (Options + , - , * , / , %)")

if choice == "+":
	sum = num1 + num2
	print("addition: ", sum )
elif choice == "-":
	diff_of_num = num1 - num2
	print("subtraction: ", diff_of_num)
elif choice == "*":
	prod_of_num = num1 * num2
	print("Multiplication: ", prod_of_num)
elif choice == "/":
	div_of_num = num1 / num2
	print("Division: ", div_of_num)
elif choice == "%":
	rem_of_num = num1 % num2
	print("reminder: ", rem_of_num)
else:
	print("Invalid")