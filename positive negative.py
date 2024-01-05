# to check whether the number is positive or negative
print("Check whether the number you enter is +ve or -ve")
num = float(input("Enter the number to check: "))
if num < 0:
    print(f"The number {num} is negative!")
elif num == 0 :
    print(f"The number {num} is zero!")
elif num > 0:
    print(f"The number {num} is positive!")
else:
    print("Pls enter a valid option")
