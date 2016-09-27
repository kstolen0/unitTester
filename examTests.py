
#   COMMENT YOUR CODE! :@

import json
import random

def main():
    try:
        f = open('units.txt','r')
        units = json.load(f)
        f.close()
    except Exception:
        print("No units found")
        print("Please add units")
        units = []

    while True:
        if len(units) > 0:
            print("Please select a unit, or add a unit.")
            for i in range(0,len(units)):
                 print(i+1, '. ', units[i])

        print("a .  Add unit")
        print("e .  Exit program")

        unitSel = input('')
        try:
            unitSel = int(unitSel)
            try:
                LoadQuestions(units[unitSel-1])
            except IndexError:
                print("index out of range\n")
        except Exception:
            if unitSel == "a" or unitSel == "A":
                units = AddUnit(units)
            elif unitSel == "e" or unitSel == "E":
                print("Good luck")
                break



def AddUnit(units):
    try:
        unitTitle = input("Enter the unit title: ")
        units.append(unitTitle)

        f = open('units.txt','w')
        json.dump(units,f,indent=4)
        f.close
    except Exception as e:
        print(e.strerror)
    finally:
        return units

def LoadQuestions(unit):
    try:
        unitfile = unit + ".txt"
        f = open(unitfile,'r')
        questions = json.load(f)
        f.close()
    except Exception:
        print("No questions found.")
        questions = []


    while True:
        print('\n',unit,' test')
        uInput = input("\nChoose [t]est, [a]dd question, [l]ist, [d]elete, [q]uit: ")
        uInput = uInput.strip()

        if uInput == 't':
            TestExam(questions)
        elif uInput == 'a':
            questions = AddQuestion(questions,unitfile)
        elif uInput == 'l':
            ListQuestions(questions)
        elif uInput == 'd':
            questions = DeleteQuestion(questions,unitfile)
        elif uInput == 'q':
            print("good luck")
            break
        else:
            print("Invalid input")


def SaveFile(questions,unitfile):
    f = open(unitfile,'w')
    json.dump(questions,f,indent=4)
    f.close
    return questions

def TestExam(questions):
    random.shuffle(questions)
    score = 0
    total = 0
    testLen = int(input("How questions would you like, between 1 and " + str(len(questions)) + ":\t"))
    for i,q in enumerate(questions,start=1):
        if i > testLen:
            break

        keyCount = 0
        print(i,',',q[0])
        userAnswer = input("")
        for i in range(2,len(q)):
            total+=1
            if q[i].lower() in userAnswer.lower():
                keyCount+=1
        print("\nNumber of matched keywords in answer: ", keyCount)
        print("\nExam Answer: ", q[1],'\n\n')
        score += keyCount
    print("You scored ", score, " out of ", total)
    print("\n\t", int((score/total*100)), "%\n")


def DeleteQuestion(questions,unitfile):
    try:
        print("Enter the question number you wish to delete, between 1 and ", len(questions))
        delInt = input("")
        try:
            delInt = int(delInt)
            del questions[delInt-1]
        except Exception:
            print("invalid input")
    except Exception as e:
        print(e.strerror)
    finally:
        return SaveFile(questions,unitfile)

def AddQuestion(questions,unitfile):
    try:
        lstQuestion = []
        qNum = len(questions) + 1
        lstQuestion.append(input("Enter question " + str(qNum) + ": "))
        lstQuestion.append(input("\nEnter answer: "))

        while True:
            keyword = input("Enter key word for right answer (enter \'e\' to exit): ")

            if keyword == 'e':
                break
            else:
                lstQuestion.append(keyword)

        questions.append(lstQuestion)
    except Exception as e:
        print(e.strerror)
    finally:
        return SaveFile(questions,unitfile)

def ListQuestions(questions):
    for i,q in enumerate(questions,start=1):
        print(i,'.',q[0],'\n')

main()
