name = "Jason"
print (name)
my_age = "22"
print (my_age)
drink = "Vimto"
print (drink)
breakfast = "Cereal"
print (breakfast)
my_age = "22"
#These functions are called variables, by typing in name and printing it, it'll print Jason as name = Jason
print ("My age is " + my_age)
#Typing in the string "My age is" then adding in + then the variable, it creates a string that 
print ("My age is {}".format(my_age)) 
print ("My favourite drink is {} and my name is {}.".format(drink,name))
#This is an alternative method to combining a string and a variable using "{}" then adding ".format(drink,name))"
i= 10
print (i)
#setting the value being "i" to "10"
i+= 2
print (i)
# += adds 2 to the original variable
i*= 2
print (i)
# *= multiplies the variable by 2
i/= 2
print (i)
# /= divides the variable by 2
i-= 2
print (i)
# -= subracts 2 from the variable
import datetime
todays_date = datetime.date.today()
my_birthday = datetime.date(2020,3,4)
days_until_birthday = my_birthday - todays_date
print(days_until_birthday)

space_top_left = "x"
space_top_centre = "o"
space_top_right = " "
space_middle_left = "x"
space_middle_centre = "x"
space_middle_right = " "
space_bottom_left = "o"
space_bottom_centre = " "
space_bottom_right = " "

print("     |     |      ")
print("  {}  |  {}  |    ".format(space_top_left, space_top_centre))
print("     |     |      ")
print("------------------")
print("     |     |      ")
print("  {}  |  {}  |    ".format(space_middle_left, space_middle_centre))
print("     |     |      ")
print("------------------")
print("     |     |      ")
print("  {}  |     |     ".format(space_bottom_left))
print("     |     |      ")