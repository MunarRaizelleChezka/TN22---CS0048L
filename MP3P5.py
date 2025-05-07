'''
Student Grade Calculator
'''

def aveCalc():
    subject = []
    score = []
    while True:
        print ("Menu: ")
        print ("[1] ~ Add Score")
        print ("[2] ~ Calculate Average")
        print ("[3] ~ Exit")
        
        choice = input ("Enter your choice from (1-3): ")

        if choice == "1":
            subj = input("Enter the subject: ")
            grade_input = input("Enter the score: ")
            
            if grade_input.replace('.', '', 1).isdigit():
                grade = float(grade_input)
                subject.append(subj)
                score.append(grade)
                print("Score added.")
            else:
                print("Invalid score! Please enter a numeric value.")
        
        elif choice == "2":

            if score:
                average = sum(score) / len(score)
                print(f"Average Grade: {average:.2f}")
            else:
                print("No scores to calculate average.")

        elif choice == "3":
            print ("Thank you for using Student Grade Calculator!")
            break 
        else:
            print ("Invalid Choice! Please enter a number from 1 to 3.")
    
aveCalc()
