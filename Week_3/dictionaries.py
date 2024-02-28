laptop={"make":"HP",
           "color":"grey",
           "weight":"2.1kg",
           "year":"2021"}
print(laptop["make"])
print(laptop["color"])
print(laptop["year"])
print(laptop["weight"])

#changing key and value or adding to original list
"""
laptop["color"]="red"
laptop["year"]="2023"
print(laptop)
"""
laptop["color"]="red"
laptop["year"]="2023"
laptop["size"]="1200mm * 600mm"
print(laptop)

del laptop["color"]
print(laptop)


#key is before: value is after:.....hence..
for key,values in laptop.items():
 print(key)
print("\n")
print(values)

bro_laptop=laptop.copy()
print(bro_laptop)

#describe your favourite car
car={"brand":"BMW","make":"m4","type":"sport","horse power":"503hp","0-60":"3.2s","color":"black"}
print(car["brand"])
print(car["make"])
print(car["type"])
print(car["horse power"])
print(car["0-60"])
print(car["horse power"])


#print individual keys,value
for key,values in car.items():
 print(key)
 print("\n")
print(values)


#copy dictionary in another dictionary
bro_car=car.copy()
print(bro_car)
