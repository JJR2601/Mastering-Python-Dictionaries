movie_directors = {
    "Titanic": "James Cameron",
    "The Matrix": "The Wachowskis",
    "Joker": "Todd Phillips",
    "Black Panther": "Ryan Coogler",
    "Moonlight": "Barry Jenkins",
    "Knives out": "Rian Johnson",
    "Jurassic Park": "David Koepp",
    "Inside out 2": "Kelsey Mann",
    "Deadpool & Wolverine": "Shawn Levy",
    "Twisters": "Lee Isaac Chung"
}

print(movie_directors)

print(movie_directors.get("Moonlight"))

movie_directors["Deadpool & Wolverine"] = "Marvel Studios"

movie_directors.pop("Jurassic Park")

print("Twisters", movie_directors["Twisters"])