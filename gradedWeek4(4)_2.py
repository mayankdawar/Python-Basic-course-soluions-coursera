#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). 
#Save these past tense words to a list called past_wrds.

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
lst = []
for i in wrds:
    i = i + "ed"
    lst.append(i)
past_wrds = lst
