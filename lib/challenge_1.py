
def convert_to_24hr_sys(hour,minutes, period):
    # condition checks for duration whether in the am or pm
    if period=='am' and hour == 12:
        hour=0
    elif period=='pm' and hour!=12:
        hour +=12 
    #convert the hour and minute variables to two digit strings
    hour_str=str(hour).zfill(2) 
    min_str=str(minutes).zfill(2)   
    
    #print out the time to test functionality
    print(hour_str + min_str)
    return hour_str + min_str   


#tests
convert_to_24hr_sys(89, 900, 'pm')
convert_to_24hr_sys(12, 00, 'am')
convert_to_24hr_sys(1, 30, 'am')
convert_to_24hr_sys(1, 30, 'pm')
convert_to_24hr_sys(4, 30, 'am')
convert_to_24hr_sys(9, 30, 'pm')

