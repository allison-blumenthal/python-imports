from appliances import Dishwasher, Dryer, Washer, Refrigerator, CoffeeMaker, CanOpener

whirlpool_dishwasher = Dishwasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

handheld_opener = CanOpener("black")
handheld_opener.open_can()
