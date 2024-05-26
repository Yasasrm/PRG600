''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 5 (lab3e.py).
Math Quiz v2.0  
''' 

from random import randint

#global variable initialization
firstNumber = 0
secondNumber = 0
points = 0
questionCount = 0

#start
def main():
    quizeCycle(getNewQuizQuestion())

#quiz question cycle until press q    
def quizeCycle(ques):
    answer = getAnswerFromUser(ques)
    if answer == "q": #exit from the question loop
        printScore()
    elif answer == "s": #skip to next question
        getNextQuestion()
    elif int(answer) == (firstNumber + secondNumber): #calculate points and go to next question
        calculatePoints()
        print("Next question...")
        getNextQuestion()
    else:
        print("Incorrect. Try again.") #repeat same question
        quizeCycle(ques)

#return new question
def getNewQuizQuestion():
  global firstNumber
  firstNumber = randint(1,10)
  global secondNumber
  secondNumber = randint(1,10)
  return "Enter the answer to %s + %s, press 's' to skip or 'q' to quit: " % (firstNumber, secondNumber)  #Question

#return user's input (Assumption: User will only insert numbers, q or s)       
def getAnswerFromUser(ques):
    return input(ques)

#print final score
def printScore():
    global questionCount
    if questionCount == 0: 
        questionCount = 1 #to eliminate division by zero
    print("Quiz over. You scored {percent:.1f}%.".format(percent = (points/questionCount)*100))

#move to next question
def getNextQuestion():
    global questionCount
    questionCount += 1
    quizeCycle(getNewQuizQuestion())

#points calculator
def calculatePoints():
    print("Correct! You have been awarded 1 point!") 
    global points
    points += 1

#entry point
if __name__ == "__main__":
    main()