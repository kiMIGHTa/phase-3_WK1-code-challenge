# phase-3_WK1-code-challenge
## Author
- 

# Challenge 1: Converting 12-hour time to 24-hour time

- This function takes in three parameters i.e hour, minute and period
- The function works by operating on the hour and minute integers according to condition determined by the period string
- The function then converts those integers into strings using the str() method and .zfill() which converts it to a two digit string. Note that it adds a zero before the string if it is a single digit integer. i.e 5 will become '05'.
- The result string are then concantenated.

## Operation
- Run python lib/challenge_1.py in your terminal while in the phase-3_WK1-code-challenge dir.

# Challenge 2: Two numbers are positive
- The function takes in three integers, checks the condition of whether only two of the numbers are positive i.e only two of the numbers are greater than zero and outputs true if the  condition is met.
## Operation
- Run python lib/challenge_2.py in your terminal while in the phase-3_WK1-code-challenge dir.

# Challenge 3: Consonant value
- Initialize a list called consonant_substr to store individual consonant substrings found within the input string.

- Iterate through each character in the input string:

- - If the character is a vowel ('aeiou'), the current substring (if any) is added to the consonant_substr list, and the current_substr is reset.
- - If the character is a consonant, it is added to the current_substr.
- After the loop, if there is an unfinished current_substr, it is added to the consonant_substr list.

- Define a function get_value(cs) that calculates the value of a given consonant substring by summing up the ASCII values of its characters.

- Iterate through the consonant_substr list and calculate the value of each substring using the get_value function. Keep track of the maximum value encountered.

- Finally, print the list of consonant substrings found and the maximum value among them.

