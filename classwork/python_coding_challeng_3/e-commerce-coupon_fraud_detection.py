'''E-Commerce Coupon Fraud Detection 
Problem Statement 
A file named coupons.txt contains coupon usage records. 
SAVE50 
WELCOME20 
SAVE50 
FESTIVE10 
SAVE50 
WELCOME20 
NEWUSER 
FESTIVE10 
SAVE50 
NEWUSER 
Tasks 
1. Count the usage frequency of each coupon.  
2. Identify coupons used more than 3 times.  
3. Create a set of unique coupons.  
4. Display the most frequently used coupon.  
5. Save suspicious coupon records into fraud_report.txt.  
Sample Output 
Coupon Usage Frequency: 
SAVE50 : 4 
WELCOME20 : 2 
FESTIVE10 : 2 
NEWUSER : 2 
Suspicious Coupons: 
SAVE50 
Unique Coupons: 
{'SAVE50', 'WELCOME20', 'FESTIVE10', 'NEWUSER'} 
Most Frequently Used Coupon: 
SAVE50 '''

# E-Commerce Coupon Fraud Detection

# Function to analyze coupon usage
def coupon_fraud_detection():

    try:
        # Open and read coupon records
        file = open("coupons.txt", "r")
        coupons = file.readlines()
        file.close()

        # Dictionary to store coupon frequencies
        coupon_freq = {}

        # Set to store unique coupons
        unique_coupons = set()

        # Count frequency of each coupon
        for coupon in coupons:

            coupon = coupon.strip()

            # Ignore empty lines
            if coupon == "":
                continue

            unique_coupons.add(coupon)

            if coupon in coupon_freq:
                coupon_freq[coupon] += 1
            else:
                coupon_freq[coupon] = 1

        # Display coupon frequencies
        print("Coupon Usage Frequency:")

        for coupon in coupon_freq:
            print(coupon, ":", coupon_freq[coupon])

        # Find suspicious coupons (used more than 3 times)
        suspicious = []

        print("\nSuspicious Coupons:")

        for coupon in coupon_freq:

            if coupon_freq[coupon] > 3:
                suspicious.append(coupon)
                print(coupon)

        if len(suspicious) == 0:
            print("None")

        # Display unique coupons
        print("\nUnique Coupons:")
        print(unique_coupons)

        # Find most frequently used coupon
        most_used = ""
        highest_count = 0

        for coupon in coupon_freq:

            if coupon_freq[coupon] > highest_count:
                highest_count = coupon_freq[coupon]
                most_used = coupon

        print("\nMost Frequently Used Coupon:")
        print(most_used)

        # Save suspicious coupons into fraud_report.txt
        try:
            report = open("fraud_report.txt", "w")

            report.write("Suspicious Coupons Report\n")
            report.write("-------------------------\n")

            for coupon in suspicious:
                report.write(coupon + "\n")

            report.close()

            print("\nFraud Report Generated Successfully")

        except Exception as e:
            print("Error while creating fraud report:", e)

    except FileNotFoundError:
        print("Error: coupons.txt file not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except Exception as e:
        print("Unexpected Error:", e)


# Function Call
coupon_fraud_detection()
