number_of_items=int(input("Number of Items: "))
pricelist=[]
for number_of_items in range(0,number_of_items):
    items_price=float(input("Price of items: "))
    pricelist.append(items_price)
totalprice=sum(pricelist)
if totalprice>100:
    discount=totalprice*0.10
    discount_price=totalprice-discount
print("Total price for",number_of_items+1,"items is",discount_price)

