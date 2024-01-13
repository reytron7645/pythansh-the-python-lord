op1=int(input("ENTER A NUMBER : "))
op2=int(input("ENTER A NUMBER : "))
opp=input("ENTER AN OPPERATOR : ")
if opp=="*":
    print(op1*op2)
elif opp=="+":
    print(op1+op2)
elif opp=="-":
    print(op1-op2)
elif opp=="/":
    print(op1/op2)
else:
    print("INVALID OPPERATOR")