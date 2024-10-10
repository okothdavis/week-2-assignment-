# question 1 
#garbage collection is an automatic memory management that frees up memory by removing objects that are not in use 
#which helps to prevent memeory leak and also helps the programms run smoothly without running out of memory
#python uses reference counting to check on references made to an object and when the checks reach zero it is freed up.

# question 2 
#python list are flexible and can hold a variety of different data types eventhough they do not support vectorized operations while Numpy arrays also store data sets of the same type in contigous blocks allowing for more efficient and faster storage hence support for vectorized operations 
#Advantages of Numpy include: faster numerical operations through vectorization and also contributes to memory efficiency due to homgenous data types 

# question 3
#lists provide a concise way to create lists based on existing lists which allows for loops and expresssions to be condensed in a single line e.g
# squared values
squared_values = [x**2 for x in range(1, 6)]
print(squared_values)  # Output: [1, 4, 9, 16, 25]

# filtering list 
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

#question 4 
# shallow copy is used to copy objects but with reference to the original object contained in the original structure. used only for immutable data types e.g
import copy
original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original)
shallow_copy[0][0] = 99
print(original)  # Output: [[99, 2, 3], [4, 5, 6]]

# deep copy is used to create a new object which copies all objects from the original structure ensuring changes in copy dont affect the original .e.g
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 999
print(original)  # Output: [[1, 2, 3], [4, 5, 6]]

#question 5 
# lists are mutable 
my_list = [1, 2, 3]
my_list.append(4)  # Adds an element
print(my_list)  # Output: [1, 2, 3, 4]


# tuples are immutable 
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise an error
print(my_tuple)  # Output: (1, 2, 3)
