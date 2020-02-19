#The variable sentence stores a string. 
#Write code to determine how many words in sentence start and end with the same letter, 
#including one-letter words. Store the result in the variable same_letter_count.
#Hard-coded answers will receive no credit.

sentence = """students flock to the arb for a variety of outdoor
                activities such as jogging and picnicking"""
sen = sentence.split()
count = 0
# Write your code here.
for i in sen:
    if i[0] == i[len(i)-1]:
        count += 1
same_letter_count = count
