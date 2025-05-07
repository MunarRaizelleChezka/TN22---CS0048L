'''
Simple Calculator
'''

result = 0

def calc():
    global result
    while True:
        print ("\nMenu:")
        print ("[1] - Add")
        print ("[2] - Subtract")
        print ("[3] - Multiply")
        print ("[4] - Divide")
        print ("[5] - Exit")
        
        choice = input ("Enter your choice from (1-5): ")

        if choice == "1":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 + num2
            print (f"Result: {result}")
        elif choice == "2":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 - num2
            print (f"Result: {result:}")
        elif choice == "3":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 * num2
            print (f"Result: {result:}")
        elif choice == "4":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if num1 == 0:
                print("Result is automatically 0.")
            elif num1 < num2:
                print("Invalid input! Second number must be greater than the first number.")
            else: 
                result = num1 // num2
                print (f"Result: {result}")
        elif choice == "5":
            print ("Closing calculator...")
            break 
        else:
            print ("Invalid Choice!")
    
calc()
