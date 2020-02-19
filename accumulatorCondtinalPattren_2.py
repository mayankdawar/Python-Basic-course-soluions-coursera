#Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. 
#Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for i in words:
    if(i[len(i)-1] == 'e'):
        i += 'd'
    else:
        i += 'ed'
    past_tense.append(i)
