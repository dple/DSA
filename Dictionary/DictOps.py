"""
Common Dict Operations used in Python
"""

dict = {"Geeks": 3, "for": 2, "geeks": 1, "I": 4, "love": 5}
# Get value of a corresponding key
print(dict["geeks"])
# This is equivalent to use the method get()
print(dict.get("Geeks"))
print(dict["for"])

# Get all keys of the dictionary
print(dict.keys())

# Get all value of the dictionary 
print(dict.values())

# Scan the dictionary 
# 1. Using 'in' operator
for key in dict:
    print(key, dict[key])

# 2. Using items() method
for key, value in dict.items():
    print(key, value)


# Sort the dictionary 
sorted_dict = sorted(dict)
print("Sorted by keys", sorted_dict) 

# Sort by the values
sorted_by_values = sorted(dict.items(), key = lambda kv: (kv[1], kv[0]))
print("Sorted by values", sorted_by_values)