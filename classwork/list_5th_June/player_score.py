##program to show score of 11 players after take input of each one's

player_score=[]  #making of a list 
for i in range(11):   #using for loop to take input of score of players
    s=int(input("Enter Score: "))   
    player_score.append(s)    #list method to send data in end of list index
print(player_score)

max=player_score[0]    #declaring index 0 of list to maximum
for i in range(len(player_score)):    #loop
    if (player_score[i]>max):   #checking value of index 0 to 1 and then 1 to 2 ...
        max=player_score[i]      #if another index has greater value then change value of max
print("Maximum value of score is: ",max)        #printing value of max
