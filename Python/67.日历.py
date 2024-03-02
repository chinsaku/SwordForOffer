year = 2020
month31 = [1,3,5,7,8,10,12]
month30 = [4,6,9,11]
weekday = 2 
month = 1 
monthday = 1
count = 0
while True:
#     print(monthday,month,year,weekday)
    if monthday == 13 and weekday ==5:
        count += 1
#         print(count)
    if count == 666:
        break
    #weekday进位
    if weekday == 7:
        weekday = 1
    else:
        weekday+= 1
    #月份进位
    if (month in month31 and monthday == 31) or (month in month30 and monthday == 30) or \
    (month == 2 and year % 4==0 and monthday ==29) or (month == 2 and year % 4 !=0 and monthday == 28):
        if month != 12:
            month += 1
            monthday = 1
            continue
        else:
            month = 1
            year += 1
            monthday = 1
            continue
    monthday += 1

    
print(year,month,monthday)