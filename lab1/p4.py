cdate=int(input('Enter current date'))
cmonth=int(input('Enter current month '))
cyear=int(input('Enter current year'))
bdate=int(input('Enter birth date'))
bmonth=int(input('Enter birth month'))
byear=int(input('Enter birth year'))

month=[31,28,31,30,31,30,31,31,30,31,30,31]
if bdate>cdate:
    cdate = cdate+cdate[month[bdate]-1]
    cmonth-=1
if bmonth>cmonth:
    cyear-=1
    cmonth+=12
print("Total no of days:",cdate-bdate)
print("Total no of months",cmonth-bmonth)
print("Total no of years",cyear-byear)        