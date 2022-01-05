#Calculating net amount of a product after discount
Marked_price = float(input("What is the marked price..??..."))
if Marked_price>10000 :
    Net_amount = Marked_price-(Marked_price*0.20)
    print("You are getting 20% of discount\nNet amount to pay after discount is ",Net_amount)
elif Marked_price>7000 and Marked_price<=10000 :
    Net_amount = Marked_price-(Marked_price*0.15)
    print("You are getting 15% of discount\nNet amount to pay after discount is ",Net_amount)
else :
    Net_amount = Marked_price-(Marked_price*0.10)
    print("You are getting 10% of discount\nNet amount to pay after discount is ",Net_amount)
