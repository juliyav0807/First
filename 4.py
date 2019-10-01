price=700
discount=20
price_with_discount = price-price*discount/100
print (price_with_discount)

def discounted (price, discount):
    price=abs(float (price))
    discount=abs (float (discount))
    if discount >=100:
        price_with_discount = price
    else:             
        price_with_discount = price-price*discount/100
    return (price_with_discount)

p=discounted (700, 120)
print (p)
discounted (1000, 50)
discounted (600, -30)

hilos ={'name': 'Ариадна', 'price': 700, 'stock':50, 'discount':30}
hilos ['with_discount']= discounted (hilos ['price'], hilos ['discount'])
print (hilos)

def discounted (price, discount, max_discount=50):
    price=abs(float (price))
    discount=abs (float (discount))
    if discount >=max_discount:
        price_with_discount = price
    else:             
        price_with_discount = price-price*discount/100
    print (price_with_discount)

    discounted (1000, 50)