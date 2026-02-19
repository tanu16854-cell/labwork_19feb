second = int(input("Enter time in seconds: "))
minutes = 0
hours= 0
if(second >= 3600):
    hours=second//3600
    second= second%3600
if(second>=60):
    minutes = second//3600
    second = second%3600
printf("Time in hours:",hours)
printf("Time in minutes: ",minutes)
printf("Time in seconds: ",second)
    
