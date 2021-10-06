#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# List in Data science and analysis
'''List
Lists are used to store multiple items in a single variable.
"
Lists are created using square brackets:'''

list_of_movies = ['Free Guy', 'Shang-Chi', 'Black Widow', 'Snyder\'s Justice league', 'Venom 2']

'''List Items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1]. the third, index [2] etc.

Ordered
When lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

*NB:  List can be changeable and it allows duplicates. List can be of any data types also and even have different data types within the same list'''

# To count the number of items in a list the len() function is used.
print(len(list_of_movies))


# Using the type() function we can find out if list_of_movies is truly a list or there's a mistake.
print(type(list_of_movies))


# Because lists are changeable and allow duplicates, we can access the items of a list using the index positions of the items. Note index position in list starts from zero(0)
print(list_of_movies[3])
print(list_of_movies[:5])


# We can also check if an item is in a list
if "Flash" in list_of_movies:
    print("Yes, Flash is in the list of movies")
else:
    print("No, The Flash is not in the list of movies")
    
    
# What if the list of movies does not have enough of the movies produced this year. We can add some of the movies to the list. Let's add one more movie
#This can be done using the append method
list_of_movies.append("Suicide Squad")
print(list_of_movies)
#Then if we have a lot of or few items to add, we can create a list for those items and extend them using the extend() function
additional_movies = ["The Flash", "Spider-man:No Way Home", "Justice League:Injustice"]
list_of_movies.extend(additional_movies)
print(list_of_movies)


# What if we realise that The Flash is not a movie but a series. Then we'll have to remove it so we report an accurate data
#the remove function remove(), helps us with that
list_of_movies.remove("The Flash")
print(list_of_movies)


# Now, probably you'll need a specific list of data many times before you move forward. With that in mind python helps us so we are able to loop a number of times with a list
#using the while loop
i = 0
while i < len(list_of_movies):
    print(list_of_movies)
    i = i + 1
#using the for loop. This allows you to loop through the index
for t in range(len(list_of_movies)):
    print(list_of_movies[t])
    
    
# Well, you are done with creating a list, you find out its not ordered and you'll like to arrange the list. Python has got you covered. Using the sort() function, you can sort the items in the list either in ascending order or cive versa
list_of_movies.sort()
print(list_of_movies)
list_of_movies.sort(reverse=True)
print(list_of_movies)
'''NB: the sort() fuction is case sensitive, thus it will arrange base on the upper case first before moving to the lower case'''

# What if you have to use list_of_movies again but don't want to make any changes to that list and use a prototype of list_of_movies. The copy() fuction helps us with that, thus you can use list_of_movies as copy in a different variable and work with it without changing the original copy
list_of_movies2 = list_of_movies.copy()
print(list_of_movies2)


# Not done with list quite yet. Don't worry, this is our last concept. Well, what if we have another list, and we want to join it with our list of movies. Let's say we have a list of cartoons
list_of_cartoons = ["Tom and Jerry", "Demon Slayer", "The Seven Deadly Sins", "Black Clover", "Naruto"]
list_of_theatre_entertainment = list_of_movies + list_of_cartoons
print(list_of_theatre_entertainment)
#this list then prints out both movies and cartoons produced this year
'''It has been fun learning with you. Hope this tutorial on how list can be used in data science and analysis proves useful.'''

