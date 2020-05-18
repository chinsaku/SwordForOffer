t =20200101
times = 0
week = 0
alldays = 0
month1 = [31,29,31,30,31,30,31,31,30,31,30,31]
month2 = [31,28,31,30,31,30,31,31,30,31,30,31]
for  i  in (1,10000000):
    if i % 4 == 0:
        month = month1
    else:
        month = month2
    for days in month:
        alldays += days 
        week = alldays % 7
        if week ==0:
            times += 1
    if times ==666:
        print(alldays)
        break
    
