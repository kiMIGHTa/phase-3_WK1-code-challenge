
def consonant_substr_value(string):
    #defie the necessary variables
    #vowels
    vowels = "aeiou"
    #array variable to hold each substring
    consonant_substr=[]
    #string that is the substring to be pushed to consonant_substr array
    current_substr=""
    
    #iterate through every character in the string
    for char in string:
        #checks the condition if the current character is a vowel
        if char in vowels:
            #if the condition is met push the substring into the array container
            if current_substr:
                consonant_substr.append(current_substr)
                current_substr=""
        else:
            #if character is not a vowel add the consonant to the current_susbtr
            current_substr += char
    #this pushes the final substring into the array container i.e cleans up the loop
    if current_substr:
            consonant_substr.append(current_substr)

    print(consonant_substr)
    
    #defines a function that calculates the value of the substring
    def get_value(cs):
        string_value = 0
        #iterates through each character in the substring and calculates its value using ACII values
        for ch in cs:
            string_value += ord(ch)-ord("a")+1
        return string_value 


    max_value=0
    
    # iterate through each substring and calculate the value of the consonants
    for substr in consonant_substr:
         value= get_value(substr)
         #assign highest value to max_value
         if value> max_value:
              max_value=value
    print(max_value)


    return max_value           


consonant_substr_value("zodiacs")
consonant_substr_value("strength")

