print("Hi.")
#"Hi" is a string.
print(len("hi."))
#print(len("hi.")) counts how many characters are in the string, the count is 3 because of the "." included.
print("hello".upper())
#This functions capitalizes all the characters in "hello"
print("hello".capitalize())
#the capitalize method ensures that the first letter in the string is upper case and the rest lower.

print("hellothere".count("h"))
#the count method counts the number of instances of the letter that's in the string: example "h".

print("hello".find("e"))
#the find method finds the index position of the given string. Index positions start from 0, E being the 2nd character is the 1st index

print("hello people".replace("hello", "cya"))
#replace takes two strings, the first string is what we want to replace, the second(indicated with a comma) is the string we want to replace

import random
print( random.randint(1,123))
#import random, imports a random number generator,(randint takes two parameters an upper and lower bound) "print(random.randint(1,123)) gives me a random number between 1 and 123"

print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
#This is my attempt at printing out a "O's" and "X's" board
print("All Around the World"[7].upper())
#This functions prints the 7th character in the string in upper case.