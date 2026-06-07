'''Sample Data 
quiz_scores = { 
    "S001": 18, 
    "S002": 12, 
    "S003": 9, 
    "S004": 20, 
    "S005": 14, 
    "S006": 7, 
    "S007": 16, 
    "S008": 10, 
    "S009": 19, 
    "S010": 13 
} 
(Quiz is out of 20 marks.) 
Tasks 
• Display students scoring 15 or above.  
• Count students scoring below 10.  
• Find the top performer.  
• Create a list of students who passed (≥ 10 marks).  
• Calculate the class average.  '''

'''
Quiz Score Analysis
(Quiz is out of 20 marks)
'''

# Dictionary containing student IDs and quiz scores
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# --------------------------------------------------
# Task 1: Display students scoring 15 or above
# --------------------------------------------------

print("Students scoring 15 or above:")

# Traverse dictionary
for student, score in quiz_scores.items():

    # Check if score is 15 or above
    if score >= 15:
        print(student)

print("-----------------------------------")

# --------------------------------------------------
# Task 2: Count students scoring below 10
# --------------------------------------------------

count = 0

# Traverse score values
for score in quiz_scores.values():

    # Check if score is below 10
    if score < 10:
        count += 1

print("Students scoring below 10:", count)

print("-----------------------------------")

# --------------------------------------------------
# Task 3: Find the top performer
# --------------------------------------------------

# Assume first student is top performer
top_student = list(quiz_scores.keys())[0]

# Store first student's score
highest_score = quiz_scores[top_student]

# Traverse dictionary
for student, score in quiz_scores.items():

    # Update top performer if higher score found
    if score > highest_score:
        highest_score = score
        top_student = student

print("Top Performer:", top_student)
print("Score:", highest_score)

print("-----------------------------------")

# --------------------------------------------------
# Task 4: Create a list of students
# who passed (score >= 10)
# --------------------------------------------------

passed_students = []

# Traverse dictionary
for student, score in quiz_scores.items():

    # Check pass condition
    if score >= 10:
        passed_students.append(student)

print("Students Who Passed:")
print(passed_students)

print("-----------------------------------")

# --------------------------------------------------
# Task 5: Calculate class average
# --------------------------------------------------

total_score = 0

# Calculate total score
for score in quiz_scores.values():
    total_score += score

# Calculate average
average_score = total_score / len(quiz_scores)

print("Class Average:", average_score)
