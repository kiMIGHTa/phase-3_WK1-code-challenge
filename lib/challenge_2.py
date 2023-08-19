# true if a>0,b>0 and c<0 or a>0,b<0 and c>0 or a<0,b>0 and c>0
# else false


def two_numbers_are_positive(a,b,c):
    if a>0 and b>0 and c<0 or a>0 and b<0 and c>0 or a<0 and b>0 and c>0:
        print ("True")
        return True
    else :
        print ("False")
        return False

two_numbers_are_positive(2, 4, -3)
two_numbers_are_positive(-4, 6, 8)
two_numbers_are_positive(4, -6, 9)
two_numbers_are_positive(-4, 6, 0)
two_numbers_are_positive(4, 6, 10) 
two_numbers_are_positive(-14, -3, -4)