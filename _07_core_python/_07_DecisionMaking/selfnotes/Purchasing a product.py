#Purchasing a product
print("\tList of products")
print("---------------------------------")
print("\ts.no\tproduct")
print("---------------------------------")
print("\t 1 \tGadgets\n\t 2 \tHome Appliances\n\t 3 \tClothing\n\t 4 \tHome Decors")
print("---------------------------------")
product=input("Which product do you want from the above list..??..")
if product=="Gadgets" :
    print("We are available on selling below products\n")
    print("\ts.no\tGadgets")
    print("---------------------------------")
    print("\t 1 \tMobiles\n\t 2 \tLaptops\n\t 3 \tTablets\n\t 4 \tPCs")
    print("---------------------------------")
    gadget=input("Which gadget you want to buy from above..??..")
    if gadget=="Moblies" :
        print("Yes we have Mobiles you can buy from our website\n")
    elif gadget=="Laptops" :
        print("Yes we have Laptops you can buy from our website\n")
    elif gadget=="Tablets" :
        print("Yes we have Tablets you can buy from our website\n")
    elif gadget=="PCs" :
        print("Yes we have PCs you can buy from our website\n")
    else :
        print("Sorry!!!\nWe are not giving  service for your gadget\n")
elif product=="Home Appliances" :
    print("We are available on selling below products\n")
    print("\ts.no\tHome Appliances")
    print("---------------------------------")
    print("\t 1 \tKitchen Sets\n\t 2 \tAir Conditiors\n\t 3 \tWashing Machines\n\t 4 \tRefrigerators")
    print("---------------------------------")
    Appliance=input("Which Home Appliance you want from the above...??..")
    if Appliance=="Kitchen Sets" :
        print("Yes we have Kitchen Sets you can buy from our website\n")
    elif Appliance=="Air Conditiors" :
        print("Yes we have Air Conditiors you can buy from our website\n")
    elif Appliance=="Washing Machines" :
        print("Yes we have Washing Machines you can buy from our website\n")
    elif Appliance=="Refrigerators" :
        print("Yes we have Refrigerators you can buy from our website\n")
    else :
        print("Sorry!!!\nWe are not giving  service for your Appliance\n")
elif product=="Clothing" :
    print("We are available on selling below products\n")
    print("\ts.no\tClothing")
    print("---------------------------------")
    print("\t 1 \tMen's Wear\n\t 2 \tWomen's Wear\n\t 3 \tKids Wear")
    print("---------------------------------")
    category=input("Which category you want from above...??...")
    if category=="Men's Wear" :
        print("Yes we have....you can buy from our website\n")
    elif category=="Women's Wear" :
        print("Yes we have....you can buy from our website\n")
    elif category=="Kids Wear" :
        print("Yes we have....you can buy from our website\n")
    else :
        print("Sorry!!!\nWe are not giving  service for your category\n")
elif product=="Home Decors" :
    print("We are available on selling below products\n")
    print("\ts.no\tHome Decors")
    print("---------------------------------")
    print("\t 1 \tCurtains\n\t 2 \tPhoto Frames\n\t 3 \tShow Pieces\n\t 4 \tWall Hangers")
    print("---------------------------------")
    decor_item=input("Which item you want from above...??...")
    if decor_item=="Curtains" :
        print("Yes we have Curtains you can buy from our website\n")
    elif decor_item=="Photo Frames" :
        print("Yes we have Photo Frames you can buy from our website\n")
    elif decor_item=="Show Pieces" :
        print("Yes we have Show Pieces you can buy from our website\n")
    elif decor_item=="Wall Hangers" :
        print("Yes we have Wall Hangers you can buy from our website\n")
    else :
        print("Sorry!!!\nWe are not giving  service for your decor_item\n")
else :
    print("Sorry!!!\nWe are not giving  service for your product\n")

