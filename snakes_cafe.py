def order():
    
    while True:
        order = input('> ').capitalize()
        if order.lower() == 'quit':
            
            print('Thank you for your order!')
            break
        if order in orders:
            orders[order] += 1
            if orders[order] == 1:
                print(f'** {orders[order]} order of {order} has been added to your meal **')
            else:
                print(f'** {orders[order]} orders of {order} have been added to your meal **')
        else:
            print(f'** Sorry,{order} is not in our Menu **')

    print("Your full order is: ")
    for i in orders:
                if orders[i] > 0:
                    
                    print(f'* {orders[i]} orders of {i} *')
        

print('*' * 38)
print('**  ', 'Welcome to the Snakes Cafe!', '   **')
print('**  ', 'Please see our menu below.', '    **')
print('**'," "*32,"**")
print('**', 'To quit at any time, type "quit"', '**')
print('*' * 38)
print('''
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Beverages
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************''')
orders = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
    }

order()

    
        
