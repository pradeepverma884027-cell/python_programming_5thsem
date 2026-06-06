#program to store employ records
''' company stores employee details in a tuple. Each employee record contains: 
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 
Where: 
• First value = Employee ID  
• Second value = Employee Name  
• Third value = Performance Score  
Tasks 
Write a Python program to: 
1. Display details of employees scoring 80 or above.  
2. Count the number of employees who need improvement (score below 60).  
3. Find the employee with the highest score.  
4. Create a list containing the names of all employees scoring above 75.'''

#creating employee data
employees=(
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
)

#--------------------------------------------------------

#Task-1 : To display details of employees scoring 80 or above. 
print("Dispalying details of employees scoring above 80")
for records in employees:
    if (records[2]>= 80):

        print(records[0],records[1],records[2])

#Task-2 To Count the number of employees who need improvement (score below 60).    
count=0
for record in employees:
    if record[2]<60:
        count+=1
print("Employees needing improvement : ",count)
print("---------------------------------")

#Task-3 To Find the employee with the highest score.  

max_score = 0
for record in employees:
    if record[2]>max_score:
        max_score=record[2]
        emp_id=record[0]
        emp_name=record[1]
print("Highest Performer : ")
print(emp_id,emp_name,max_score)
print("------------------------------------")

#Task-4 To Create a list containing the names of all employees scoring above 75.
score_above_75=[]
for record in employees:
    if(record[2]>75):
        score_above_75.append(record[1])
print("High Performers : ")
print(score_above_75)
print("---------------------------------") 


#Task 5: To display the performance category for each employee:
print("Performance Categories : ")
for record in employees:
    if record[2]>=90:
        print(record[1],"-> Excellent")
    elif record[2]>=75 and record[2]<90:
        print(record[1],"-> Good")
    elif record[2]>=60 and record[2]<75:
        print(record[1],"-> Average")
    else:
        print(record[1],"-> Needs Improvement")
print("---------------------------------")
