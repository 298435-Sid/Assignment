#Perform Basic Set Operations 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#Union of Sets 
print("Union:", A | B)

#Intersection of Sets 
print("Intersection:", A & B)

#Difference of Sets 
print("A - B:", A - B)
print("B - A:", B - A)

#Symmetric Difference of Sets 
print("Symmetric Difference:", A ^ B)

#Add a list of Elements to a Set
A = {1, 2, 3}
B = [3, 4, 5, 6]
A.update(B)
print(A)

#Set Difference Update
#Remove Items From Set Simultaneously
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
A.difference_update(B)
print(A)

#Check Subset 
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

#Check Superset 
print(A.issuperset(B))

#Set Intersection Check
A = {1, 2, 3, 4}
B = {4, 5, 6}
if A & B:
    print("Sets intersect")
else:
    print("Sets do not intersect")

#Set Symmetric Difference Update
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.symmetric_difference_update(B)
print(A)

#Set Intersection Update
A.intersection_update(B)
print(A)

#Find Common Elements in Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)

#Frozen Set
fruits = frozenset(["apple", "banana", "orange"])
print(fruits)

#Count Unique Words
text = "Hi UST Hi Microsoft"
words = text.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Count:", len(unique_words))