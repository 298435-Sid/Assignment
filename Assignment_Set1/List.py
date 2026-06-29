#Create a list
numbers = [10, 20, 30, 40]
print(numbers)

#Access elements
print(numbers[0])      
print(numbers[-1])    

#Add elements
numbers.append(50)     
numbers.insert(1, 15)  

#Remove elements
numbers.remove(30)    
numbers.pop()          

#Update element
numbers[0] = 100

#List length
print(len(numbers))

# sum and average of all numbers in a list

total = sum(numbers)
average = total / len(numbers)

print("Sum =", total)
print("Average =", average)

# Reverse list
numbers.reverse()

#every element in a list to its square
squares = [num ** 2 for num in numbers]
print(squares)

#Maximum and Minimum
maximum = max(numbers)
minimum = min(numbers)
print("Maximum is", maximum)
print("Minimum is", minimum)

#Count Occurrence
print("Occurrence of 40:", numbers.count(40))
print("Occurrence of 20:", numbers.count(20))

# Sort list
numbers.sort()

#copy list
copy_list = numbers.copy()
print("Copied List:", copy_list)

#combine 2 list
numbers2 = [60, 70, 50, 40]
combined = numbers + numbers2
print(combined)

#Remove Empty Strings from a List
words = ["apple", "", "banana", "", "mango"]
result = [word for word in words if word != ""]
print(result)

#Remove Duplicates from a List in Python
numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = list(set(numbers))
print(unique_numbers)

#Remove All Occurrences of a Specific Item from a List
#List Comprehension for numbers
numbers = [10, 20, 10, 30, 10, 40, 20]
item_remove = 10
result = [num for num in numbers if num != item_remove]
print(result)

#Access Nested List
nested_list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(nested_list[0])

#flattened Nested List
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

#Concatenate Two Lists Index-Wise
list1 = ["Hello", "Good"]
list2 = ["UST", "Morning"]
result = [a + b for a, b in zip(list1, list2)]
print(result)

#Concatenate Two Lists in the Following Order
result = [a + b for a in list1 for b in list2]
print(result)

#iterate both lists simultaneously
list1 = ["A", "B", "C"]
list2 = [1, 2, 3]
for a, b in zip(list1, list2):
    print(a, b)

#add a new item to a list after a specific item
fruits = ["apple", "banana", "orange"]
index = fruits.index("banana")
fruits.insert(index + 1, "mango")
print(fruits)

#extended nested list by adding sublist
nested_list = [[1, 2], [3, 4]]
nested_list.append([5, 6])
print(nested_list)

#replace list's item with new value if found
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    index = fruits.index("banana")
    fruits[index] = "mango"
print(fruits)