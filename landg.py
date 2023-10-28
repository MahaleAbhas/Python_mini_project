bal=0

def checkbal():
    print("Your Total Balace Are:",bal)
def deposit(add):
    global bal
    bal=bal+add
    print("You Are Deposit",add,"Rs in Your A/c")
def withdraw(sub):
    global bal
    
    if sub<bal:
        bal=bal-sub
        print("You Are WIthdraw",sub,"Rs In Your A/c")
    else:
        print("You Can't Withdraw Money From A/c Because You Have Not Enough Balance")

while True:
    ch=int(input("Bank Process\n1.Check Balance\n2.Deposit\n3.Withdraw\n5.Exit\nEnter Your Choice:"))

    if ch==1:
        checkbal()
    elif ch==2:
        a=int(input("Enter Deposit Amt:"))
        deposit(a)
    elif ch==3:
        b=int(input("Enter Withdraw Amt:"))
        withdraw(b)
    elif ch==4:
        print("My Bank Process Done")
        break
    else:
        print("Invalid Number")

    
