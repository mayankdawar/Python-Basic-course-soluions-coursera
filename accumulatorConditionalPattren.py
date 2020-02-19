#For each string in the list words, find the number of characters in the string. 
#If the number of characters in the string is greater than 3, 
#add 1 to the variable num_words so that num_words should end up with the total number of words with more than 3 characters.

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for i in words:
    if len(i) > 3:
        num_words += 1
