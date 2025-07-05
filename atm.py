n=int(input("enter your password"))
if(n==123):
    print("your password id correct now enter your choose")
    m=int(input("enter,1 to withdraw,2 to check balance,3 to deposite"))
    if(m==1):
        u=int(input("enter the amount to withdraw"))
        if(u<=20000):
            print("withdraw succesfully")
            print("thank you")
        else:
            print("the amount limit is only 20000")
            print("try less than 20000")
    elif(m==2):
        print("your balance amount is 309807")
        print("thank you")
    elif(m==3):
        w=int(input("enter the amount to deposite"))
        print("amount deposite succesfully")
        print("thank you")
    else:
        print("you dont choose any given number thank you")
else:
    print("invalid password")
                    
