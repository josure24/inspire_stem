laptop = {"make":"hp","colour":"grey","weight":"1.2","year":"2021"}


print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

laptop["colour"] = "red"
laptop["year"] = "2021"

for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)

    laptop["size"] = "1200mm x 600mm"

    print(laptop)

  

