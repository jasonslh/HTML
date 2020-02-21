def press_grind_beans():
    print('grinding for 20 seconds')
#def = define function
press_grind_beans()

coffee_is_grinding = False

def press_grind_beans():
    if coffee_is_grinding:
        print('The coffee is grinding')
    else:
        print ('The coffee is not grinding')
press_grind_beans()

def cash_withdrawal(amount,accnum):
    print('Withdrawing {} from account {}'. format(amount,accnum))

cash_withdrawal(300, 50449921)
cash_withdrawal(30, 50449921)
cash_withdrawal(200, 50449921)

def coffee_order(size, type_of_drink):
    print('The order is a {} {}'. format(size, type_of_drink))

coffee_order("Large", "Latte")

def add_up(num1, num2):
    return num1 + num2
add_up(7,3)
print(add_up(2,5))

def multiply_by_nine_fiths(celsius):
    return celsius * (9/5)
def get_farenheit(celsius):
    return multiply_by_nine_fiths(celsius) + 32
print ("The temperature is {} degrees".format(get_fahrenheit(15)))

