#program to check if a student pass the assesment  or not
while(True):
    #accepting the marks
    marks_obtained=int(input("Enter marks "))
    #condition for passing assessment
    if(marks_obtained>=40):
        print("Result: Pass")
        print("Congratulations! You have cleared the statement")
        break
    #condition for failing the assessment
    elif(marks_obtained<=40):
        print("Result: Fail")
    
    

