# iterating through the dictionary and printing my_dict  = {'A':1,"B":2,"C":3} and printing each key 
# value pair in the format key:value 
'''my_dict  = {'A':1,"B":2,"C":3}
for key in my_dict:
    #print(key)
    #print(my_dict[key])
    #printing them in key to value  format
    print(f"{key}:{my_dict[key]}") '''

# Getting user input for the dictionary
my_dict = {}
n = int(input("Enter the number of key-value pairs: "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

# Iterating through the dictionary and printing key-value pairs
for key in my_dict:
    print(f"{key}:{my_dict[key]}")
