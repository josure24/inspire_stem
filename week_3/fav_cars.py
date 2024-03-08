# this is a class that describe cars
# date : 28/02/2024
# name : Joshua wairegi 

fav_car={"brand":"toyota","colour":"black","model":"prado","speed":"200km/h"}
print(fav_car)

print(fav_car["colour"])
print(fav_car["model"])
print(fav_car["speed"])

# to change the car value
fav_car["colour"] = "black"
fav_car["speed"] = "200km/h"
fav_car["model"] = "prado"
print(fav_car)

fav_car["size"] = "4783mm x 1852mm x 1442mm"
print(fav_car)

del fav_car["model"]
print(fav_car)


for key,value in fav_car.items():
    print(key)
    print("\n")
    print(value)                
