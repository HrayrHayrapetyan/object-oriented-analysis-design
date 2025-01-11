class Product:
        def __init__(self,product_id,product_name,price,inventory_count):
                self.product_id=product_id
                self.product_name=product_name
                self.price=price
                self.inventory_count=inventory_count


        def apply_discount(self,discount_percentage):
                discount_ammount=self.price*discount_percentage/100
                self.price-=discount_ammount
                print(f'The new price is {self.price}')

        def sell(self,quantity):
                self.inventory_count-=quantity
                print(f'The current inventory count is {self.inventory_count}')


class DynamicPricing:
        def adjust_price(self,product:Product,demand:str):
                if demand =='high':
                        product.price+=1000
                        print(f'The price has increase because of a high demand, now it is {product.price}')
                elif demand=='low' and  product.inventory_count<20:
                        product.price-=1000
                        print(f'The price has decreased because of a low demand and low inventory count, now it is {product.price}')


product =Product('123131','Iphone',4000,30)
product.apply_discount(20)
product.sell(20)

product2=Product('adwdw','macbook',8000,24)
product2.apply_discount(10)
product2.sell(3)

dynamicpricing=DynamicPricing()
dynamicpricing.adjust_price(product,'low')

dynamicpricing.adjust_price(product2,'high')

#1. We have full access to the price we initialize the product  with.This can cause wrong inputs from user 
#2. The reliability lacks in places such as passing negative values to both changing the quantity and applying a wrong number as a discount
#3.The inventory count can decrease until it reaches zero and even further so thats one problem. The price can change significantly and become unacceptable (become  a negative or get too high )




