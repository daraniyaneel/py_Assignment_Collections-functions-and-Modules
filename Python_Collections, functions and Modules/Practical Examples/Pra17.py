#Write a Python program to convert two lists into one 
#dictionary using a for loop.

keys = ['aa','bb','cc','dd'] 
values = [55,66,44,77]

dict = {}

for i in range(len(keys)): 
    dict[keys[i]] = values[i]
    
print('dict = ',dict)

