city_population = {
    "Caloocan": "1,500,000",
    "Quezon": "2,760,000",
    "Pasig": "615,000",
    "Manila": "1,600,000",
    "Makati": "510,000",
    "Pasay": "416,000",
    "Mandaluyong": "305,000",
    "San Juan": "121,000",
    "Las Pinas": "590,000",
    "Davao": "1,121,000"
}

print(city_population)

print(city_population.get("Pasay"))

city_population["Pasig"] = "617,000"

city_population.pop("Las Pinas")

print("Davao:", city_population["Davao"])
