music = "Sam's music"

if music == "Sam's music"
    print("Oh no it's 00s indie again")
elif music == "No music":
    print("Peace and quiet")
else:
    print("What music is playing?")

age = 22
country = "UK"

if age > 17 and country == "UK":
    print("Yes, what can I get you?")

else:
    print("Sorry, you're underage.")


day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
else:
    print("When is the weekend?")

#Challenge 1

password = ("Manchester")
password_len =len(password)

if password_len >8:
    print("password is good")
else:
    print("password is too short")

#Challenge 2

num = 1
div_num_3 = num / 3
div_num_5 = num / 5
if (div_num_3).is_integer() or (div_num_5).is_integer():
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")

#Challenge 3

num = 15
if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print("This number is not divisible by 3 or 5")

#Challenge 4

#challeng4
num_int = 148221
num = str(num_int)
if num == num[::-1]:
    print("This is a palindrome.")
else:
    print("This is not a palindrome")
