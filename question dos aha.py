#question two
Hours = [12,7,9,9,6,8,2]
total_litres = sum(Hours)
cost_per_litre = 1.35
total_litres = total_litres*0.5
print("The total amount of milk during the week was",total_litres)
pricetotal = total_litres * cost_per_litre
pricetotal = round(pricetotal,2)
print("Price for milk this week..","€",pricetotal)
