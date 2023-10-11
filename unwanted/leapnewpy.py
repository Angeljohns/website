
y1= int(input("Enter the starting year:"))
y2= int(input("Enter the ending year:"))
if y1>y2:
    print("final year must be greater than or equal to current year:")
else:
    print(f"leap years from {y1} to {y2}")
    for year in range(y1,y2+1):
       if(year%4==0 and year%100!=0)or(year%400==0):
          print (year)

        
