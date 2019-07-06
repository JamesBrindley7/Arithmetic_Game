from random import randint

class Arithmetic(object):
    
    def start(self):
        print("Welcome to the arithmetic game") 
        user_choice = input("(1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random Sums (6) Quit\n")
        num_range = 4
        if user_choice == "1":
            print("You have chosen Addition...")
            a.add(num_range, 0, 0)
        elif user_choice == "2":
            print("You have chosen Subtraction...")
            a.sub(num_range, 0, 0)
        elif user_choice == "3":         #Depending on the user choice call the correct method e.g. add or subtract etc
            print("You have chosen Multiplication...")
            a.mult(num_range, 0, 0)
        elif user_choice == "4":
            print("You have chosen Division...")
            a.div(num_range, 0, 0)
        elif user_choice == "5":
            print("You have chosen Random Sums...")
            a.ran(num_range, 0)
        elif user_choice == "6":
            print("Quitting...")
            quit()
        else:
            print("Please enter a number between 1 and 6 to enter the game")
            a.start()
    
    def add(self, num_range, rand, streak):  #Add method, takes the max number, if its being called from the random sums method and if the user has answered previous questions right or wrong
        x = randint(1, num_range)
        y = randint(1, num_range)   #Generates random numbers within the range
        right_answer = (x+y)        #Calculates the right answer and prints the equation into the terminal
        print("What is ", x, "+", y, "?")
        num_range,streak = a.answercheck(num_range,streak,right_answer) #Submits the real answer and gets the inputed answer and checks if its right or wrong
        if rand == 1:
            a.ran(num_range,streak)     #If it was called by the random sums then return to that so it can call another
        else:
            self.add(num_range, 0,streak) #Else call itself again so the user can player another question
        
    def sub(self, num_range, rand, streak): #Subtract method, takes the max number, if its being called from the random sums method and if the user has answered previous questions right or wrong
        x = randint(1, num_range)
        y = randint(1, num_range)   #Generates random numbers
        right_answer = (x-y)      
        if right_answer >= 0:        #Checks if the answer is above 0, if not then restart and select new numbers
            print("What is ", x, "-", y, "?")  #Prints the equation
            num_range,streak = a.answercheck(num_range,streak,right_answer) #Submits the real answer and gets the inputed answer and checks if its right or wrong
        if rand == 1:
            a.ran(num_range,streak) #If it was called by the random sums then return to that so it can call another
        else:
            self.sub(num_range,0,streak) #Else do another subtract
            
    def mult(self, num_range, rand, streak): #multiplication method, takes the max number, if its being called from the random sums method and if the user has answered previous questions in a streak
        x = randint(1, num_range) #Generates random numbers
        y = randint(1, num_range)
        right_answer = (x*y)    #Calculates right answer
        print("What is ", x, "*", y, "?")  
        num_range,streak = a.answercheck(num_range,streak,right_answer) #Submits the real answer and gets the inputed answer and checks if its right or wrong
        if rand == 1:
            a.ran(num_range,streak) #If called by random sums then go back and call another random equation
        else:
            self.mult(num_range,0,streak)       #Else do another multiplication
            
    def div(self, num_range, rand, streak):
        x = randint(1, num_range)       #Generate a random number
        y = randint(1, num_range)
        if x % y == 0:          #Checks if x is divisible by y (If not then skip and do another)
            right_answer = int(x/y)     #Store right answer and print equation
            print("What is ", x, "/", y, "?") 
            num_range,streak = a.answercheck(num_range,streak,right_answer) #Submits the real answer and gets the inputed answer and checks if its right or wrong
        else:
            self.div(num_range, rand, streak)   #If the numbers don't divide then try another until one does divide by the other
        if rand == 1:
            a.ran(num_range, streak) #If called by random sums then go back and call another random equation
        else:
            self.div(num_range,0,streak) 
            
    def ran(self, num_range, streak):
        descison = randint(0, 3)        #Generates a random number to determine if its going to be a add, sub, multiply or divide equation
        if descison == 0:
            a.add(num_range, 1,streak)
        elif descison == 1:
            a.sub(num_range, 1,streak)
        elif descison == 2:
            a.mult(num_range, 1,streak)     #Call right method and says its called by the random method by putting the variable to 1
        elif descison == 3:
            a.div(num_range, 1,streak)
            
    def answercheck(self, num_range,streak,right_answer):        #All equations call this method with their range, streak number and right answer to check it
        user_answer = a.userinput() #Gets the user input and saves it in user_answer
        if user_answer == right_answer:         #Checks if its the right answer
            print("That is correct, well done! Press Y to try another sum or N to stop: ")
            a.playagain()                     #If it is then call the right answer method that prints that the user has the right answer and asks if they want to do another one
            streak = a.positivestreak(streak)
            num_range, streak = a.checkstreak(num_range,streak)  #Determines if the difficulty should be increased or decreased (3 wrong = decrease and 3 right = increase)
        else:
            print("Not right, the correct answer is: ", right_answer ," Press Y to try another sum or N to stop: ")
            a.playagain()     #If its wrong then call the wrong answer method that prints out the right answer and checks if the player wants to play again
            streak = a.negetivestreak(streak)
            num_range, streak = a.checkstreak(num_range,streak) #Determines if the difficulty should be increased or decreased
        return num_range,streak #Returns the range if there's a new one and a streak if there's a new one and goes back to the method for the next question
        
    
    def checkstreak(self, num_range, streak):
        if streak == 3:     #Checks if the streak is at 3 right, if so then change it back to 0 and increase the difficulty aka the number range
            streak = 0
            num_range = num_range + 1
            if num_range > 10:
                num_range = 10
                print("Highest Level - Difficulty Not Changed - ( Range: 0 -", num_range,")")
            else:
                print("Difficulty Increased - ( Range: 0 -", num_range,")")
        elif streak == -3: #Checks if the negative streak is at 3 wrong, if so then change it back to 0 and decrease the difficulty aka the number range
            streak = 0
            streak = 0
            num_range = num_range - 1
            if num_range < 4:
                num_range = 4
                print("Lowest Level - Difficulty Not Changed - ( Range: 0 -", num_range,")")
            else:
                print("Difficulty Decreased - ( Range: 0 -", num_range,")")
        
        return num_range, streak        #Return the new number range and streak
    
    def playagain(self): #If the answer was wrong then start a loop asking the player if they want to play again
        cont = input()
        if cont == "N" or cont == 'n': #If no then go back to main menu
            a.start()
        elif cont == "Y" or cont == 'y':
            return
        else:
            print("Please type either Y to try another sum or N to stop: ") 
            self.playagain()      #call again to allow the user to type another letter, only goes out of this if either y nor n is entered
        
    def userinput(self):
        while True:
            try: 
                user_answer = int(input(""))       #Takes the user input and converts it to an integer
                return user_answer
            except ValueError:                      #If the value isn't an integer then print only integers and call the method again until an integer is entered
                print ("Only integers")
        
    def positivestreak(self, streak):
        if streak < 0:                      #Resets the streak if it was a negative one
                return 0
        else:
            return (streak + 1)                 #Adds one to the streak
    
    def negetivestreak(self, streak):
        if streak > 0:                      #Resets the streak if it was a positive one
                return 0
        else:
            return (streak - 1)                 #Adds one to the streak
                
a = Arithmetic()  
a.start()
