#parameters=>hour,min,period
#if pm add 12 except 12 itself
#if midnight i.e 12 am eka hour = 0
#join them after convertion CORRECTLY

def convert_to_24hr_sys(hour,minutes, period):
    if period=='am' and hour == 12:
        hour=0
    elif period=='pm' and hour!=12:
        hour +=12 

    hour_str=str(hour).zfill(2) 
    min_str=str(minutes).zfill(2)   

    print(hour_str + min_str)
    pass   

convert_to_24hr_sys(12, 00, 'pm')
convert_to_24hr_sys(12, 00, 'am')
convert_to_24hr_sys(1, 30, 'pm')
convert_to_24hr_sys(1, 30, 'pm')
convert_to_24hr_sys(4, 30, 'am')
convert_to_24hr_sys(9, 30, 'pm')

