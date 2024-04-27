
date = input("Enter the date in the format of 21/04/2010 : ")
#  using built in function split

day,month,year = date.split('/')
print(f"the day is {day} and the month is {month} and the year is {year}")

# without built in function


day=''
month=''
year=''

i=0
while date[i]!='/':
    day+=date[i]
    i=i+1
    
i+=1

while date[i]!='/':
    month+=date[i]
    i+=1
    
i+=1

while i<len(date):
    year+=date[i]
    i+=1
    
print(f"the day is {day} and the month is {month} and the year is {year}")
