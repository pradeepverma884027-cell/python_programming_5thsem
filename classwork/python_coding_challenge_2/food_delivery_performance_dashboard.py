'''Food Delivery Performance Dashboard 
Problem Statement 
Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  
Sample Output 
Fastest Delivery: 18 minutes 
 
Slowest Delivery: 80 minutes 
 
Average Delivery Time: 40.8 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Fast Deliveries: 4 
Normal Deliveries: 3 
Delayed Deliveries: 3 '''

#making list of delivery times

delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 

#Find the fastest delivery time.  

fastest=delivery_times[0]

for i in delivery_times:
    if i<fastest:
        fastest=i

print("Fastest Delivery:",fastest)

# slowest delivery time

slowest=delivery_times[0]

for i in delivery_times:
    if i<slowest:
        slowest=i

print("slowest Delivery:",slowest)


#Calculate the average delivery time.

total_time= sum(delivery_times)

print(" Average Delivery Time: ",total_time/len(delivery_times))


#Display delayed orders (>45 minutes). 
print("Delayed Orders: ")
[60, 80, 55] 
for i in delivery_times:
    if i >45:
        print(i)


'''5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  '''
count_fast=0
count_normal=0
count_delayed=0
for i in delivery_times:
    if i<=30:
        count_fast+=1
    if i>31 and i<45:
        count_normal+=1
    if i>45:
        count_delayed+=1

print("Fast Deliveries:",count_fast ) 
print("Normal Deliveries", count_normal) 
print("Delayed Deliveries ", count_delayed)

