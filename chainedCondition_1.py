#Create one conditional to find whether “false” is in string str1.
#If so, assign variable output the string “False. You aren’t you?”. 
#Check to see if “true” is in string str1 and if it is then assign “True! You are you!” to the variable output.
#If neither are in str1, assign “Neither true nor false!” to output.

str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
if 'false' in str1:
    output = "False. You aren't you?"
elif "true" in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false"
