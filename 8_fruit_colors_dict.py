fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "dragon fruit": "pink",
    "grapes": "purple",
    "pear": "green",
    "coconut": "brown",
    "blueberry": "blue"
}

print(fruit_colors)

print(fruit_colors.get("pear"))

fruit_colors["dragon fruit"] = "white"

fruit_colors.pop("coconut")

print("blueberry:", fruit_colors["blueberry"])