'''The marks obtained by students in the final examination are stored as follows: 
Sample Data 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
6. Create a list of scholarship students (marks ≥ 90).  
Sample Output 
Students Scoring Above 85: 
Anuj 
Priya 
Sneha 
Anjali 
 
Topper: 
Sneha (95) 
 
Lowest Scorer: 
Rohit (47) 
 
Average Marks: 76.4 
 
Scholarship Students: 
['Anuj', 'Sneha', 'Anjali']'''

#creating dictionary for marks
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 


#Display students scoring above 85 marks. 

for student ,mark in marks.items():
    if mark>85:
        print(student)

# Find the topper. 

topper = list(marks.keys())[0]
highest_marks = marks[topper]

for student, mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        topper = student

print("Topper:")
print(topper, "(", highest_marks, ")")

#to find student with lowest marks
lowest = list(marks.keys())[0]
lowest_marks = marks[lowest]

for student, mark in marks.items():
    if mark < lowest_marks:
        lowest_marks = mark
        lowest = student

print("Lowest Scorer:")
print(lowest, "(", lowest_marks, ")")

#Calculate class average marks.

total= sum(marks.values())

print("Average Marks: ",total/len(marks))

#Create a list of scholarship students (marks ≥ 90).  

scholar=[]

for student, mark in marks.items():
    if mark>=90:
        scholar.append(student)

print("schloarship Students:") 
print(scholar)


