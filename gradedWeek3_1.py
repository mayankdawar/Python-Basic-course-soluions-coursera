#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan 
#for every month (in inches) with every month separated by a comma. 
#Write code to compute the number of months that have more than 3 inches of rainfall.
#Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.
#Hard-coded answers will receive no credit.

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
months = rainfall_mi.split(",")
count = 0
for i in months:
    if float(i) > 3.0:
        count += 1
    
num_rainy_months = count
