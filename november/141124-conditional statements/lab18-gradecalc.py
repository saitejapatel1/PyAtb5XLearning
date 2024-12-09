#A=90-100
#b=80-89
#c=70-79
#d=60-69
#e=50-59
#f=0-35

score=int(input("enter your score\n"))

if score>=90 and score<=100:
    print("your grade is->","A")
elif score>=80 and score<=89:
    print("your grade is->","B")
elif score>=70 and score<=79:
    print("your grade is->","C")
elif score>=60 and score<=69:
    print("your grade is->","D")
elif score>=50 and score<=59:
    print("your grade is->","E")
elif score>=1 and score<=35:
    print("your grade is->","F")




else:
    print("you are border passed students who got minimum skills ")

