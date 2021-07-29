import random
import datetime
def randomBirthday():
    year = random.randint(1900,2021)        #random year
    yearLeap=False
    if (year%4==0 and year%100!=0 or year%400==0):      #check leap year
        yearLeap=True
    
    month = random.randint(1, 12)           #random month
    day_limit=0
    if (month ==2):                     #check if february
        if(yearLeap==True):             #check if leap year
            day_limit=29    
        else:
            day_limit=28
    else:
        if(month%2==0 and month<7 or month%2!=0 and month >7):
            day_limit=30        #condition for 30 days
        else:
            day_limit=31
    day = random.randint(1, day_limit)      #generate a random date
    dob =datetime.date(year, month, day)    #format our date   
    day_of_year = dob.timetuple().tm_yday   #day out of 365/366
    return day_of_year
   
    
    
birthday=[]
for i in range(50):
    day_of_year=randomBirthday()
    birthday.append(day_of_year)
birthday.sort()




print(birthday)