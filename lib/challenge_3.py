
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

    def get_value(cs):
        string_value = 0
        for ch in cs:
            string_value += ord(ch)-ord("a")+1
        return string_value 


    max_value=0

    for substr in consonant_substr:
         value= get_value(substr)
         if value> max_value:
              max_value=value
    print(max_value)


    pass           


consonant_substr_value("zodiacs")
consonant_substr_value("strength")

