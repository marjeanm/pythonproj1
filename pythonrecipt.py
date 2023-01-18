

#recipt descriptions 
lovely_loveseat_description = """
 Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
                              """

style_sette_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.

                          """

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.

                              """
# recipt sales prices
lovely_loveseat_price = 254.00

stylish_settee_price = 180.50

luxurious_lamp_price = 52.15
# recipt sales tax
sales_tax = .088

#customer starting total 
customer_one_total = 0

# keep a list of things purchased
customer_one_itemization = ""
# adding all the customers items together
customer_one_total += lovely_loveseat_price + luxurious_lamp_price
# adding together the description.
customer_one_itemization += lovely_loveseat_description + luxurious_lamp_description
#calucation of the recipt
customer_one_tax = customer_one_total * sales_tax
# calculation of the total plus tax.
total = customer_one_total + customer_one_tax
# print details.
print("Customer One Items: ", customer_one_itemization,"Customer One Total: ", total)