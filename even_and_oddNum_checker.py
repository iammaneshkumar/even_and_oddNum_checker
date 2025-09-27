print("------ Hello Guys! This is a simple code to check the entred number the user is odd or even ------")
while True:
    num = input("Enter a number: ")
    if not num.isdigit():
        print("Please enter a valid number.")
        continue
    num = int(num)
    
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    
    again = input("Do you want to try again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
