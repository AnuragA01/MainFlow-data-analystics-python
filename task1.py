# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16fTupZ6xd6roMpg_UunwHqAO_Ac6SWST
"""

list = [0, 1, 2, 3, 4]
print("list:", list)

list.append(6)
print("adding an element:", list)

list.remove(0)
print("removing an element:", list)

list.insert(2, 10)
print("inserting an element:", list)

list.extend([7, 8, 9])
print("extending with another list:", list)

list[2] = 15
print("modifying an element:", list)

print("Popped element:", list.pop())
print("List after popping an element:", list)

list.clear()
print("clearing all elements:", list)

dict = {'id': 123, 'name':'Anurag', 'gender':'male'}
print("dictionary:",dict)

dict['age'] = 21
print("adding an element:", dict)

del dict['gender']
print("removing an element:", dict)

dict.update({'Batch': 'A', 'email': 'xyz@gmail.com'})
print("updating with another dictionary:", dict)

print("Removed value using pop:", dict.pop('email'))
print("Dictionary after popping an element:", dict)

dict.clear()
print("clearing all elements:", dict)

set = {1, 2, 3, 4, 5}
print("set:", set)

set.add(11)
print("adding an element:", set)

set.remove(4)
print("removing an element:", set)

print("Popped element from set:", set.pop())
print("Set after popping an element:", set)

another_set = {5, 6, 7, 8}
union_set = set.union(another_set)
print("Union of sets:", union_set)

print("Intersection of sets:", set.intersection(another_set))

print("Difference of sets:", set.difference(another_set))

set.clear()
print("Set after clearing all elements:", set)