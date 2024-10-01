# Q1. Write a Python program to find the second largest number in a list.
print('--Q1: ')
li = [10, 20, 4, 45, 99]
max = 0
for i in li:
    if i> max:
        max = i
li.remove(max)

max = 0
for i in li:
    if i> max:
        max = i

# Alternate approach
li = [10, 20, 4, 45, 99]
max_num = max(li)
li.remove(max_num)  # Remove the largest element
second_max = max(li)
print(second_max)


print(max)
print(li)

# Q2. Write a Python program to convert a list of tuples into a dictionary.
print('--Q2: ')
lis = [('apple', 1), ('banana', 2), ('cherry', 3)]
d1 = {}
for tup in lis:
    d1[tup[0]] = tup[1]

print(d1)
# Alternate approach
d1 = {tup[0]: tup[1] for tup in lis}


# Q3. Write a Python program to check if a key exists in a dictionary. {'a': 1, 'b': 2, 'c': 3}, key = 'b'
print('--Q3: ')
d2 = {'a': 1, 'b': 2, 'c': 3}
d2k = 'b' in d2.keys()
print(d2k) 

# Q4. Write a Python program to return a set that contains only the common elements between two sets.
print('--Q4: ')
set1 = {1, 2, 3} 
set2 = {3, 4, 5}
print(f"Common elements: ", set1.intersection(set2))

# Q5. Write a Python program that prints the multiplication table of a given number up to 10.
print('--Q5: ')
# num = int(input("Enter number: "))
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

