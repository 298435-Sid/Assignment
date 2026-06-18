#Perform basic dictionary operations 
student = {
    "name": "Sidhardh",
    "age": 26,
}
print(student)

#Access a Value
print(student["name"])
print(student.get("age"))

#Add a New Item
student["city"] = "Bangalore"
print(student)

#Update an Item
student["age"] = 22
print(student)

#Delete an Item
del student["city"]
print(student)

#Dictionary from Lists
keys = ["name", "age", "city"]
values = ["Sidhardh", 26, "Bangalore"]
result = dict(zip(keys, values))
print(result)

#Clear Dictionary 
student = {
    "name": "Sidhardh",
    "age": 26,
    "city": "Bangalore"
}
student.clear()
print(student)

#Merge two Python dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
result = dict1 | dict2
print(result)

#Count Character Frequencies
text = "hello"
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

#Access Nested Dictionary
student = {
    "name": "Sidhardh",
    "details": {
        "age": 26,
        "city": "Bangalore"
    }
}
print(student["details"]["age"])

#Print the value of key ‘history’ from nested dict
student = {
    "class": {
        "student1": {
            "name": "Sidhardh",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
} 
print(student["class"]["student1"]["marks"]["history"])

# Modify Nested Dictionary 
student["class"]["student1"]["marks"]["history"] = 90
print(student)

#Initialize dictionary with default values
employees = ["arun", "varun", "arjun"]
defaults = dict.fromkeys(employees, 0)
print(defaults)

#Create a dictionary by extracting the keys from a given dictionary
Employee = {
    "name": "Sidhardh",
    "age": 25,
    "salary": 50000,
    "city": "Bangalore"
}
keys = ["name", "salary"]
new_dict = {k: Employee[k] for k in keys}
print(new_dict)

# Delete a list of keys from a dictionary
Employee = {
   "name": "Sidhardh",
    "age": 25,
    "salary": 50000,
    "city": "Bangalore"
}
keys_to_remove = ["age", "city"]
for key in keys_to_remove:
    Employee.pop(key, None)
print(Employee)

#Check if a value exists in a dictionary
Employee = {
   "name": "Sidhardh",
    "age": 25,
    "city": "Bangalore"
}
if "Sidhardh" in Employee.values():
    print("Value exists")
else:
    print("Value does not exist")

# Rename key of a dictionary
Employee["full_name"] = Employee.pop("name")
print(Employee)

#Get the key of a minimum value
dict1 = {
    "a": 50,
    "b": 20,
    "c": 10,
    "d": 40
}
min_key = min(dict1, key=dict1.get)
print(min_key)

#Change value of a key in a nested dictionary
dict1 = {
    "employee": {
        "name": "Sidhu",
        "salary": 50000
    }
}
dict1["employee"]["salary"] = 60000
print(dict1) 

#Invert Dictionary
dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}
inverted_dict = {value: key for key, value in dict1.items()}
print(inverted_dict)

#Sort Dictionary by Keys
dict1 = {
    "c": 300,
    "a": 100,
    "b": 200
}
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)

#Sort Dictionary by Values
dict1 = {
    "a": 300,
    "b": 100,
    "c": 200
}
sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(sorted_dict)

#Check if All Values are Unique
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}
if len(dict1.values()) == len(set(dict1.values())):
    print("All values are unique")
else:
    print("Duplicate values found")