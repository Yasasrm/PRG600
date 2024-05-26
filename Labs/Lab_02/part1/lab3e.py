''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 5 (lab3e.py).
Math Quiz v2.0  
''' 

from random import randint

firstNumber = 0
secondNumber = 0
points = 0
questionCount = 0

def main():
    quizeCycle(getNewQuizQuestion())
    
def quizeCycle(ques):
    answer = getAnswerFromUser(ques)
    if answer == "q":
        printScore()
    elif answer == "s":
        getNextQuestion()
    elif int(answer) == (firstNumber + secondNumber):
        calculatePoints()
        getNextQuestion()
        print("Next question...")
    else:
        print("Incorrect. Try again.")
        quizeCycle(ques)

def getNewQuizQuestion():
  global firstNumber
  firstNumber = randint(1,10)
  global secondNumber
  secondNumber = randint(1,10)
  return "Enter the answer to %s + %s, press 's' to skip or 'q' to quit: " % (firstNumber, secondNumber)  #Question

        
def getAnswerFromUser(ques):
    return input(ques)

def printScore():
    print("Quiz over. You scored {percent:.1f}%.".format(percent = (points/questionCount)*100))

def getNextQuestion():
    global questionCount
    questionCount += 1
    quizeCycle(getNewQuizQuestion())

def calculatePoints():
    print("Correct! You have been awarded 1 point!") 
    global points
    points += 1


if __name__ == "__main__":
    main()