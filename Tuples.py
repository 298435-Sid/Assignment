# Creating a tuple
t = (10, 20, 30, 40, 50)

# Accessing elements
print(t[0])      
print(t[-1])    

# Tuple repetition
print(t * 2)

# Slicing Tuple
print(t[1:4])    

#Reverse the tuple
reversed_t = t[::-1]
print(reversed_t)

#Access Nested Tuples 
t = (10, 20, (30, 40, 50), 60)
print(t[2])
print(t[2][0])  
print(t[2][1]) 
print(t[2][2]) 

#Create a tuple with single item 50
t = (50,)
print(t)
print(type(t))

# Unpack the tuple into 4 variables 
t = (10, 20, 30, 40)
a, b, c, d = t
print(a)
print(b)
print(c)
print(d)

#Swap two tuples in Python
t1 = (10, 20, 30)
t2 = (40, 50, 60)
t1, t2 = t2, t1
print("t1 =", t1)
print("t2 =", t2)

#Copy Specific Elements From Tuple
t = (10, 20, 30, 40, 50)
new_t = (t[0], t[2], t[4])
print(new_t)

#List to Tuple 
my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

#Function Returning Tuple 
def get_values():
    return (10, 20, 30)
result = get_values()
print(result)
print(type(result))

#Comparing Tuples 
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)
print(t1 == t2)  # True
print(t1 != t3)  # True
print(t1 < t3)   # True
print(t3 > t1)   # True

#Removing Duplicates from Tuple
t = (10, 20, 30, 20, 40, 10, 50)
unique_t = tuple(set(t))
print(unique_t)

#Filter Even Numbers(Filter Tuple)
t = (10, 15, 20, 25, 30, 35)
filtered_t = tuple(x for x in t if x % 2 == 0)
print(filtered_t)

#Multiply Each Element by 10 (Map Tuples)
t = (10, 20, 30)
mapped_t = tuple(map(lambda x: x * 10, t))
print(mapped_t)

#Modify Tuple
t = (10, 20, 30, 40)
temp = list(t)
temp[1] = 25
t = tuple(temp)
print(t)

# Sort a tuple of tuples by 2nd item
t = ((1, 5), (2, 3), (3, 8), (4, 1))
sorted_t = tuple(sorted(t, key=lambda x: x[1]))
print(sorted_t)

# Counting elements
t = (1, 2, 2, 3, 2)
print(t.count(2))

# Length of tuple
print(len(t))

#Check if all items in the tuple are the same
t = (5, 5, 3, 5)
if t.count(t[0]) == len(t):
    print("All items are the same")
else:
    print("Items are different")