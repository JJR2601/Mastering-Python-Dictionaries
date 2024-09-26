animal_sounds = {
    "cat": "meow",
    "dog": "woof",
    "sheep": "baa",
    "pig": "oink",
    "snake": "hiss",
    "duck": "quack",
    "frog": "croak",
    "horse": "neigh"
}
print(animal_sounds)

print(animal_sounds.get("pig"))

animal_sounds["frog"] = "ribbit"

animal_sounds.pop("snake")

print("horse:", animal_sounds["horse"])
