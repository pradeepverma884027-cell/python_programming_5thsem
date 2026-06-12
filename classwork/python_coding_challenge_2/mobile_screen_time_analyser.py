'''Mobile Screen Time Analyzer 
Problem Statement 
Daily mobile screen time (in minutes) of a student is recorded for 10 days. 
Sample Data 
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
Tasks 
1. Calculate average screen time.  
2. Find the highest and lowest screen time.  
3. Count days exceeding 200 minutes.  
4. Display days with healthy usage (<180 minutes).  
5. Categorize usage:  
o Healthy (<180)  
o Moderate (180–240)  
o Excessive (>240)  
Sample Output 
Average Screen Time: 205.5 minutes 
 
Highest Screen Time: 300 minutes 
 
Lowest Screen Time: 120 minutes 
 
Days Exceeding 200 Minutes: 5 
 
Healthy Usage Days: 
Day 3 
Day 5 
Day 9 
 
Healthy: 3 
Moderate: 4 
Excessive: 3'''


#creating list for screen time
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 

#Calculate average screen time. 

total=sum(screen_time)
print("Average Screen Time:",total/len(screen_time))


#Find the highest and lowest screen time.

high=screen_time[0]
low=screen_time[0]

for time in screen_time:
    if time>high:
        high=time
    if time<low:
        low=time

print("Highest Screen Time:")
print(high)

print("Lowest Screen Time: ")
print(low)

# Display days with healthy usage (<180 minutes).  
for i in range(len(screen_time)):
    if i<180:
        print(i)


'''5. Categorize usage:  
o Healthy (<180)  
o Moderate (180–240)  
o Excessive (>240)  '''

high=0
mod=0
exc=0

for i in screen_time:
    if i <180:
        high+=1
    if i >180 and i<240:
        mod+=1
    if i>240:
        exc+=1

print("Healthy: ",high)
print("Moderate:",mod) 
print("Excessive: ",exc)

