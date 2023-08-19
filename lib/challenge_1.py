
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
convert_to_24hr_sys(1, 30, 'am')
convert_to_24hr_sys(1, 30, 'pm')
convert_to_24hr_sys(4, 30, 'am')
convert_to_24hr_sys(9, 30, 'pm')

