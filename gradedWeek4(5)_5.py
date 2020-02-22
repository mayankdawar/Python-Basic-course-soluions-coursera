#Provided is a list of data about a store’s inventory where each item in the list represents the name of an item,
#how much is in stock, and how much it costs. Print out each item in the list with the same formatting, 
#using the .format method (not string concatenation).
#For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for temp in inventory:
    temp = temp.split(',')
    str1="The store has{} {}, each for{} USD."
    str1=str1.format(temp[1],temp[0],temp[2])
    print(str1)
    
    
    
# 2nd way of string formatting    
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for temp in inventory:
    temp = temp.split(',')
    item = temp[0]
    quantity = temp[1]
    amount = temp[2]
    str1="The store has{} {}, each for{} USD."
    str1=str1.format(quantity,item,amount)
    print(str1)
