def dayOfProgrammer(year):
    if ((year < 1918 and year % 4 == 0) or (year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
        dop="12.09."+str(year)
    elif year==1918:
        dop="26.09.1918"
    else:
        dop="13.09."+str(year)
    return dop

print(dayOfProgrammer(1918))