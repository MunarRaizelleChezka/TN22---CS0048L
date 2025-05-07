'''
Temperature Converter
'''

initialTemp = 0
celsTemp = 0
fahrTemp = 0

def temp_converter():
    global initialTemp
    global celsTemp
    global fahrTemp
    while True:
        print ("\nMenu:")
        print ("[1] - Convert Celsius to Fahrenheit")
        print ("[2] - Convert Fahrenheit to Celsius")
        print ("[3]  - Exit")
        
        choice = input ("Enter your choice from (1-3): ")

        if choice == "1":
            initialTemp = float(input("Enter temperature in Celsius: "))
            fahrTemp = (initialTemp * 9/5) + 32
            print (f"Temperature in Fahrenheit: {fahrTemp:.2f}")
        elif choice == "2":
            initialTemp = float(input("Enter temperature in Fahrenheit: "))
            celsTemp = (initialTemp - 32) * (5/9)
            print (f"Temperature in Fahrenheit: {celsTemp:.2f}")
        elif choice == "3":
            print ("Exiting temperature converter...")
            break 
        else:
            print ("Invalid Choice!")
    
temp_converter()
