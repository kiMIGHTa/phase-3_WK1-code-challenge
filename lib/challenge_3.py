#breakdown strings to substring on condition of it is not a vowel
# calculate value of substring according to a range of the alphabet(1-26)
# params=>string
#variables=>substring array and vowels for condition 

def consonant_substr_value(string):
    vowels = "aeiou"
    consonant_substr=[]
    current_substr=""

    for char in string:
        if char in vowels:
            if current_substr:
                consonant_substr.append(current_substr)
                current_substr=""
        else:
            current_substr += char
            
    if current_substr:
            consonant_substr.append(current_substr)

    print(consonant_substr)
    pass

consonant_substr_value("strength")

