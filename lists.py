coffee_order = ['sam - hot choco', 'andrew - flat white', 'ezra - champagne']

print(coffee_order[2])
#Square brackets, access the individual string in the list, Python begins to count from 0, so the 3rd item in the list is actually the 2nd
coffee_order[2]="Ezra-Latte"
#The square brackets here, allows me to change the item in the list that corresponds with the number.
print(coffee_order)

print(len(coffee_order))
#"print(len), prints the number of items in the list rather than each character"
coffee_order.append('Stuart - Cortado')
#append, allows me to add an item to the list
print(coffee_order)

coffee_order.pop()
#.pop removes the last item on the list
print(coffee_order)

import random

for i in range(6):
    print(random.randint(1,50))
#this code is a random number generator, the "range" is how many numbers I want to print and "randint" is the range of numbers

import random

for i in range(9,-1, -1):
    print(i)
#first value is where to start, second value is where to end. Using index, 0 is the starting number, so to get the number we want, we need to change it to -1. The third number is the direction we want to count.

favourite_films = ["Anchorman", "The Dark Knight", "Tarzan", "Spiderman 2", "Saving Private Ryan"]

favourite_films.append ("The Babadook")
favourite_films.insert (6,"Avengers")
favourite_films.insert (0, "Tropic Thunder")
favourite_films.insert (2, "Alien")
print(favourite_films)
#.insert followed by a number in the brackets, inserts a string into the list in the position that correlates with the number.

films = ["Twin Towers", "Enemy at the gates", "Ghostbusters", "Alien"]

if films [2] == "Ghostbusters":
    print('yes its Ghostbusters')
else:
    print("boo, we want Ghostbusters")

#This is a code for finding the 3rd item in the list, this function checs if the 3rd film is "Ghostbusters"
