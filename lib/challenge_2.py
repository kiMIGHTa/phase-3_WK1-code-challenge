
def two_numbers_are_positive(a,b,c):
    #checks the connsition that only two integers are positive and one is negative
    if a>0 and b>0 and c<0 or a>0 and b<0 and c>0 or a<0 and b>0 and c>0:
        #return true if condition is met
        print ("True")
        return True
    else :
        #returns false if condition is not met
        print ("False")
        return False

#tests
two_numbers_are_positive(2, 4, -3)
two_numbers_are_positive(-4, 6, 8)
two_numbers_are_positive(4, -6, 9)
two_numbers_are_positive(-4, 6, 0)
two_numbers_are_positive(4, 6, 10) 
two_numbers_are_positive(-14, -3, -4)