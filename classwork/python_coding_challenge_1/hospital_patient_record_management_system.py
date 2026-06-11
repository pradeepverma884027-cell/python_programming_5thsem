# Hospital Patient Record Management System

# --------------------------------------------------
# Task 1: Display all patient records
# --------------------------------------------------

# Open file in read mode
file = open("patients.txt", "r")

print("Patient Records:\n")

# Read and display all records
for record in file:
    print(record.strip())

# Close the file
file.close()

# --------------------------------------------------
# Task 2: Display critical patients
# --------------------------------------------------

# Open file again in read mode
file = open("patients.txt", "r")

print("\nCritical Patients:")

# Traverse all records
for record in file:

    # Remove newline character
    record = record.strip()

    # Split record into fields
    pid, name, status = record.split(",")

    # Display patient name if status is Critical
    if status == "Critical":
        print(name)

# Close file
file.close()

# --------------------------------------------------
# Task 3: Count patients under each status
# --------------------------------------------------

normal_count = 0
stable_count = 0
critical_count = 0

# Open file
file = open("patients.txt", "r")

# Traverse records
for record in file:

    record = record.strip()

    pid, name, status = record.split(",")

    # Count based on status
    if status == "Normal":
        normal_count += 1

    elif status == "Stable":
        stable_count += 1

    elif status == "Critical":
        critical_count += 1

# Close file
file.close()

# Display counts
print("\nPatient Count:")
print("Normal :", normal_count)
print("Stable :", stable_count)
print("Critical :", critical_count)

# --------------------------------------------------
# Task 4: Search patient details using Patient ID
# --------------------------------------------------

search_id = input("\nEnter Patient ID to Search: ")

found = False

# Open file
file = open("patients.txt", "r")

# Traverse records
for record in file:

    record = record.strip()

    pid, name, status = record.split(",")

    # Check Patient ID
    if pid == search_id:
        print("\nPatient Found:")
        print(record)
        found = True
        break

# Close file
file.close()

# If patient not found
if found == False:
    print("Patient Not Found.")

# --------------------------------------------------
# Task 5: Save critical patient records to file
# --------------------------------------------------

# Open source file
file = open("patients.txt", "r")

# Open destination file
critical_file = open("critical_patients.txt", "w")

# Traverse records
for record in file:

    record = record.strip()

    pid, name, status = record.split(",")

    # Save only critical patient records
    if status == "Critical":
        critical_file.write(record + "\n")

# Close files
file.close()
critical_file.close()

print("\nCritical Patient Report Generated Successfully.")
