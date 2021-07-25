menu=['wings','cookies','spring rolls','salmon','steak','meat tornado','a literal garden','ice cream','cake','pie','coffee','tea','unicorn tears']


print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")

print("""Appetizers
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

Drinks
------
Coffee
Tea
Unicorn Tears""")

order=[]
count =0 
count1=0
print("""***********************************
** What would you like to order? **
***********************************""")


    

while(-1 <0):
  
 order_item = input(">")
 order_item=order_item.lower()
 if order_item in menu:
  order.append(order_item)
  count = order.count(order_item)
  count1 +=1
  print(f" ** {count} order of {order_item} have been added to your meal **")
  
 
 elif order_item == "quit":
     break 
     
 else:
  print("not aviable , chooes something else !")
 

print("This is your order : " )
for j in order:
    print(j.upper())
    


