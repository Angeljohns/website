year=int(input("Enter a year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print(" it is leap year")
else:
    print("it is not a leap year")
   
