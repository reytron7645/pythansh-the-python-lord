#Create a program that takes a student's score as input and prints their grade (A, B, C, D, or F) based on the following criteria:

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

marks=input('give your score :')
marks=(int(marks))
if marks >90 and marks <=100:
    print("you have passed whith grade A")
elif marks >80 and marks <=90:
    print("you have passed with grade B")
elif marks >70 and marks <=80:
    print("you have  lost by 2 wrong and whith grade C")
elif marks >60 and marks <=70:
    print("you have lost by six wrong and with grade D")
elif marks >=0 and marks <=60:
    print("you have lot by 10 wrong and whith grade F")
else:
    print("invalid score inserted")