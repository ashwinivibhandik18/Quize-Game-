#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Do you want to play quize game ? ")    
choice=input()
print("")
if choice.lower()!="yes":
    pass
else:
    score=0
    print("Let's play ! 🥳 ")
    print("")
    
    print("Que 1: Which one of the following is the correct extension of the Python file ? ")
    print("a) .py")
    print("b) .python")
    print("c) .p")
    print("d) None of these")
    ans1 = input("Ans: ")
    if ans1.lower()=="a":
        score=score+1
        print("Correct! 👍")      
    elif ans1.lower()==".py":
        score=score+1
        print("Correct! 👍")    
    else:
        print("Incorrect! 👎")
    print("")    
    
    
    print("Que 2: What do we use to define a block of code in Python language ? ")
    print("a) Key")
    print("b) Brackets")
    print("c) Indentation")
    print("d) None of these")
    ans2 = input("Ans: ")
    if ans2.lower()=="c":
        score=score+1
        print("Correct! 👍")
    elif ans2.lower()=="indentation":
        score=score+1
        print("Correct! 👍")    
    else:
        print("Incorrect! 👎")
    print("")    
    
    
    print("Que 3: Which character is used in Python to make a single line comment? ")
    print("a) /")
    print("b) //")
    print("c) #")
    print("d) !")
    ans3 = input("Ans: ")
    if ans3.lower()=="c":
        score=score+1
        print("Correct! 👍")
    elif ans3.lower()=="#":
        score=score+1
        print("Correct! 👍")    
    else:
        print("Incorrect! 👎") 
    print("") 
    
    
    print("Que 4: Which of the following operators is the correct option for power(ab)? ")
    print("a) a^b")
    print("b) a**b")
    print("c) a^^b")
    print("d) a^*b")
    ans4 = input("Ans: ")
    if ans4.lower()=="b":
        score=score+1
        print("Correct! 👍")
    elif ans4.lower()=="a**b":
        score=score+1
        print("Correct! 👍")    
    else:
        print("Incorrect! 👎")
    print("")    
    
        
    print("Que 5: Which one of the following has the highest precedence in the expression ? ")
    print("a) Division")
    print("b) Subtraction")
    print("c) Power")
    print("d) Parentheses")
    ans5 = input("Ans: ")
    if ans5.lower()=="d":
        score=score+1
        print("Correct! 👍")
    elif ans5.lower()=="parentheses":
        score=score+1
        print("Correct! 👍")    
    else:
        print("Incorrect! 👎")
    print("")    
        
if score>=3:
    print("You Win the game ! 🎉")
else:
    print("You Lose the game ! 🙁")
print("Your Score : "+ str(score))       
       

