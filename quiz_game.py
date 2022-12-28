
print('welcome to my computer quiz!') 

playing = input(" do you want to play? ")

if playing.lower() != "yes":
    print(" no problem not at all ")
    quit()
 

print("okay! Let's play :)")

score = 0

#---------1.question-------------------#

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("opps Incorrect! -----> right answer is central processing unit")    
    
#---------2.question-------------------#

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("oops  Incorrect! -----> right answer is graphics processing unit") 

#--------3.question--------------------#

answer = input("what does RAM stand for?")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("oops Incorrect! -----> right answer is random access memory") 
 
 #--------4.question--------------------#   

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print("oops Incorrect! -----> right answer is power supply unit") 
    
print("You got "+ str(score)+ " question correct out of 4" )  
print("You got "+str((score / 4)*100) + "%")  
    


         