## Python Quiz Game ##

print('!!! Welcome to the world of Quiz !!!')

play=input(' Press y to continue ')
score=0

if play=='y':
    print("Let's Begin")

    qn1= input("what does 1+1 equal to? ")
    if qn1 !='2':
        print('Incorrect')
    else:
        print('Correct')
        score+=1
    
    qn2=input(" What does 5+2 equal to? ")
    if qn2 !='7':
        print('InCorrect')
    else:
        print('correct')
        score+=1
     

    qn3= input(' what does 10-5 equal to? ')
    if qn3 !='5':
            print('InCorrect')
    else:
        print('correct')
        score+=1
    
    qn4= input(' what does 10+5 equal to? ')
    if qn3 !='15':
            print('InCorrect')
    else:
        print('correct')
        score+=1
    
    qn3= input(' what does 8+7 equal to? ')
    if qn3 !='15':
            print('InCorrect')
    else:
        print('correct')
        score+=1
    print("Congrats!!! You got "+ str(score) +" out of 5")
    print(" Your Precentile is "+ str((score/5)*100) +"%")


else:
    quit()





