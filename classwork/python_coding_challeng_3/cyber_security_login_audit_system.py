'''Cyber Security Login Audit System 
Problem Statement 
A file named login_logs.txt contains user login attempts in the following format: 
username,status 
anuj,Success 
rahul,Failed 
anuj,Failed 
priya,Failed 
rahul,Failed 
neha,Success 
anuj,Failed 
karan,Failed 
rahul,Success 
priya,Failed 
Tasks 
1. Count successful and failed login attempts.  
2. Identify users with more than 2 failed attempts.  
3. Create a dictionary storing the number of failures per user.  
4. Create a set of users who logged in successfully.  
5. Display users whose accounts should be reviewed.  
Sample Output 
Successful Login Attempts: 3 
Failed Login Attempts: 7 
 
Failure Count per User: 
anuj : 2 
rahul : 2 
priya : 2 
karan : 1 
 
Users with Successful Logins: 
{'anuj', 'neha', 'rahul'} 
 
Accounts Requiring Review: 
None '''

# Cyber Security Login Audit System

# Function to analyze login logs
def analyze_login_logs():

    try:
        # Open file in read mode
        file = open("login_logs.txt", "r")

        # Read all lines
        records = file.readlines()

        # Close the file
        file.close()

        # Counters for login attempts
        success_count = 0
        failed_count = 0

        # Dictionary to store failure count per user
        failure_dict = {}

        # Set to store users with successful logins
        successful_users = set()

        # Process each record
        for line in records:

            # Remove extra spaces/newlines
            line = line.strip()

            try:
                # Split username and status
                username, status = line.split(",")

                # Check login status
                if status == "Success":
                    success_count += 1
                    successful_users.add(username)

                elif status == "Failed":
                    failed_count += 1

                    # Update failure count
                    if username in failure_dict:
                        failure_dict[username] += 1
                    else:
                        failure_dict[username] = 1

                else:
                    print("Invalid status found in file:", line)

            except ValueError:
                print("Invalid record format:", line)

        # List to store users requiring review
        review_accounts = []

        # Check users with more than 2 failed attempts
        for user in failure_dict:

            if failure_dict[user] > 2:
                review_accounts.append(user)

        # Display results
        print("Successful Login Attempts:", success_count)
        print("Failed Login Attempts:", failed_count)

        print("\nFailure Count per User:")

        for user in failure_dict:
            print(user, ":", failure_dict[user])

        print("\nUsers with Successful Logins:")
        print(successful_users)

        print("\nAccounts Requiring Review:")

        if len(review_accounts) > 0:
            for user in review_accounts:
                print(user)
        else:
            print("None")

    except FileNotFoundError:
        print("Error: login_logs.txt file not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except Exception as e:
        print("Unexpected Error:", e)


# Function call
analyze_login_logs()

