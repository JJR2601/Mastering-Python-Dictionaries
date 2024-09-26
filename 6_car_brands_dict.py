car_brands = {
    "BMW": "Germany",
    "Bugatti": "France",
    "Ferrari": "Italy",
    "Ford": "United states",
    "Honda": "Japan",
    "Hyundai": "South korea",
    "McLaren": "England",
    "Chery": "China",
    "Aston Martin": "United Kingdom",
    "Saab": "Sweden"
}

print(car_brands)

print(car_brands.get("Ferrari"))

car_brands["McLaren"] = "United Kingdom"

car_brands.pop("Chery")

print("Saab:", car_brands["Saab"])
