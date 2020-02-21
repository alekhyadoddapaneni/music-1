l1 = []
ch = 'y'
print("WELCOME TO MADHURA WINES ")
while(ch == 'y'):
    
    w_b =str(input("enter your favourate brand:  "))
    l1.append(w_b)
    ch =str(input(" you want one more favourate brand then enter (y/n):  "))
print("your order is ",l1)
c = str(input("do you want to modify your order(y/n) :  "))
if(c == 'y'):
    print("1. add a new brand")
    print("2. modify the brand")
    print("3. remove the brand")
    s =  int(input("select  above one option:  "))
    if(s == 1 ):
    	w_b =str(input("enter your new favourate brand:  "))
    	l1.append(w_b)
    	rint("your order is ",l1)
    elif(s == 2 ):
        m =int(input("enter your modify item no  :  "))
        r =str(input("enter your new brand  :  ")) 
        l1[m-1] = r
        print("your new order is ",l1)
    elif(s == 3):
        m  = input(" which brand no you want remove :")
        l1.remove(m)
        print("your new order is : ",l1)
print("thank you sir ")
