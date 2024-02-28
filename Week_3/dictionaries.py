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
for key,value in laptop.items():
 print(key)
print("\n")
print(value)

bro_laptop=laptop.copy()
print(bro_laptop)

#describe your favourite car









#print individual keys,value
#copy dictionary in another dictionary
