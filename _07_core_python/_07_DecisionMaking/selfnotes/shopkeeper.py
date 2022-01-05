#price after different discount
Amount=float(input("How much a customer purchased...??..."))
if Amount<=0 :
    print("Insufficient purchase")
elif Amount>0 and Amount<=100 :
    print("You are eligible for below discounts")
    print("Discount on each item")
    print("-----------------------------------")
    print("\t Sh---Short--- 0%")
    print("\t P---Pants--- 3%")
    print("\t Shirt/T-Shirt--- 5%")
    product = input("Enter the item customer purchased....")
    if product== "Sh" :
        print("Discount is 0%")
        print("Your have purchased for Rs/-",Amount)
    elif product == 'P' :
        print("Discount is 3%")
        print("Your have purchased for Rs/-",Amount*0.97)
    elif product == 'Sht' :
        print("Discount is 5%")
        print("Your have purchased for Rs/-",Amount*0.95)
    else :
        print("You have not purchased any discounted product")
elif Amount>101 and Amount<=200 :
    print("You are eligible for below discounts")
    print("Discount on each item")
    print("-----------------------------------")
    print("\t Sh---Short--- 5%")
    print("\t P---Pants--- 8%")
    print("\t Sht---Shirt/T-Shirt--- 10%")
    product = input("Enter the item customer purchased....")
    if product== "Sh" :
        print("Discount is 5%")
        print("Your have purchased for Rs/-",Amount*0.95)
    elif product == 'P' :
        print("Discount is 8%")
        print("Your have purchased for Rs/-",Amount*0.92)
    elif product == 'Sht' :
        print("Discount is 10%")
        print("Your have purchased for Rs/-",Amount*0.90)
    else :
        print("You have not purchased any discounted product")
elif Amount>201 and Amount<=300 :
    print("You are eligible for below discounts")
    print("Discount on each item")
    print("-----------------------------------")
    print("\t Sh---Short--- 10%")
    print("\t P---Pants--- 12%")
    print("\t Sht---Shirt/T-Shirt--- 15%")
    product = input("Enter the item customer purchased....")
    if product== "Sh" :
        print("Discount is 10%")
        print("Your have purchased for Rs/-",Amount*0.90)
    elif product == 'P' :
        print("Discount is 12%")
        print("Your have purchased for Rs/-",Amount*0.88)
    elif product == 'Sht' :
        print("Discount is 15%")
        print("Your have purchased for Rs/-",Amount*0.85)
    else :
        print("You have not purchased any discounted product")
else :
    print("You are eligible for below discounts")
    print("Discount on each item")
    print("-----------------------------------")
    print("\t Sh--Sh0rt--- 18%")
    print("\t P--Pants--- 20%")
    print("\t Sht--Shirt/T-Shirt--- 22%")
    product = input("Enter the item customer purchased....")
    if product== "Sh" :
        print("Discount is 18%")
        print("Your have purchased for Rs/-",Amount*0.82)
    elif product == 'P' :
        print("Discount is 20%")
        print("Your have purchased for Rs/-",Amount*0.80)
    elif product == 'Sht' :
        print("Discount is 22%")
        print("Your have purchased for Rs/-",Amount*0.78)
    else :
        print("You have not purchased any discounted product")
