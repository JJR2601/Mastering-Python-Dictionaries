country_capital = {
    "Indonesia": "Jakarta",
    "India": "New Delhi",
    "Israel": "Jerusalem",
    "Canada": "Ottawa",
    "United states": "Washington, D.C.",
    "Australia": "Canberra",
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
    "Singapore": "Singapore",
    "South Korea": "Seoul",
    "Thailand": "Bangkok",
    "Vietnam": "Hanoi"
}

print(country_capital)

print(country_capital.get("United states"))

country_capital["Philippines"] = "Quezon"

country_capital.pop("Thailand")

print("Vietnam:" ,country_capital["Vietnam"])