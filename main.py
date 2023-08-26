import unittest
import random

class radndomNumberGame:
    
    def __init__(custom):
        custom.num = custom.random()
      
    def validateRandomnumbers(custom, temp):
        # validate the number should be four digit number: 
        GuessNumber = [int(digit) for digit in str(temp)]
        selected_number = [int(digit) for digit in str(custom.num)]
        
        # combination of the  common digits between the selected_number and guessed number with each other
        digits = set(selected_number) & set(GuessNumber)
        
        # checking and comparision of numbers for guess and selected both 
        # checking to the both digits of selected_number and guess numbers with each others
        num1 = sum(1 for t_digit, g_digit in zip(selected_number, GuessNumber) if t_digit == g_digit)
        
        # the number of counts of digits which was correct but are in wrong position. 
        temp2 = len(digits) - num1

        return f"{num1} (circles) {temp2} (X)"
        
    def random(custom):
        return random.randint(1000, 9999)
    

if __name__ == '__main__':
    print("--------------welcome to number guessing game -----------------")
    
    while True:
        game = radndomNumberGame() 
       # setting count as zero 
        temp2 = 0

        while True:
            inputs = input("--------- Enter your guess (press q to exit from the game Thanks ): ")
           # if user press q then game is over 
            if inputs.lower() == 'q':
                break

            if not inputs.isdigit() or len(inputs) != 4:
                print("!sorry wrong input please enter the correct 4 digit numbers Thanks!")
                continue

            temp = int(inputs)
            result = game.validateRandomnumbers(temp)  
            temp2 = temp2 + 1
            print(result)
            # if the output of the result is 4 circle and zero X 
            if result == "4 (circle) 0 (temp)": 
                print(f"---Congratulation You have  guessed the number in {temp2} attempts.-----------------")
                break
        # if the Game end ask user if he wants to play again
        retry = input("Do you want to play the game again (y/n) ")
        if retry.lower() != 'y':
            break
