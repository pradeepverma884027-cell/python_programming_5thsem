'''Hospital Patient Monitoring System 
Problem Statement 
Patient heart rates are recorded below. 
Sample Data 
heart_rate = { 
    "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
} 
Tasks 
1. Display critical patients (heart rate >100).  
2. Find highest and lowest heart rate.  
3. Calculate average heart rate.  
4. Count stable patients (60–100 bpm).  
Sample Output 
Critical Patients: 
P102 
P104 
P107 
P110 
 
Highest Heart Rate: 
P110 (130 bpm) 
 
Lowest Heart Rate: 
P105 (65 bpm) 
 
Average Heart Rate: 94.3 bpm 
 
Stable Patients: 6'''

# Hospital Patient Monitoring System

# Dictionary storing patient IDs and their heart rates
heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# --------------------------------------------------
# Task 1: Display critical patients
# (Heart rate greater than 100 bpm)
# --------------------------------------------------

print("Critical Patients:")

# Traverse the dictionary and identify critical patients
for patient, rate in heart_rate.items():
    if rate > 100:
        print(patient)

# --------------------------------------------------
# Task 2: Find highest and lowest heart rate
# --------------------------------------------------

# Assume first patient has highest and lowest heart rate
highest_patient = list(heart_rate.keys())[0]
lowest_patient = list(heart_rate.keys())[0]

highest_rate = heart_rate[highest_patient]
lowest_rate = heart_rate[lowest_patient]

# Compare heart rates of all patients
for patient, rate in heart_rate.items():

    # Update highest heart rate
    if rate > highest_rate:
        highest_rate = rate
        highest_patient = patient

    # Update lowest heart rate
    if rate < lowest_rate:
        lowest_rate = rate
        lowest_patient = patient

print("\nHighest Heart Rate:")
print(highest_patient, f"({highest_rate} bpm)")

print("\nLowest Heart Rate:")
print(lowest_patient, f"({lowest_rate} bpm)")

# --------------------------------------------------
# Task 3: Calculate average heart rate
# --------------------------------------------------

total_rate = 0

# Add heart rates of all patients
for rate in heart_rate.values():
    total_rate += rate

# Calculate average heart rate
average_rate = total_rate / len(heart_rate)

print("\nAverage Heart Rate:", round(average_rate, 1), "bpm")

# --------------------------------------------------
# Task 4: Count stable patients
# (Heart rate between 60 and 100 bpm inclusive)
# --------------------------------------------------

stable_count = 0

# Count stable patients
for rate in heart_rate.values():
    if 60 <= rate <= 100:
        stable_count += 1

print("\nStable Patients:", stable_count)
