sports_players = {
    "Boxing": "Manny Pacquiao",
    "Soccer": "Diego Maradona",
    "Basketball": "Michael Jordan",
    "Tennis": "Roger Federer",
    "Baseball": "Hank Aaron",
    "Badminton": "Taufik Hidaya",
    "Gymnastics": "Carlos Yulo",
    "MMA": "Conor McGregor",
    "Cycling": "Lance Armstrong",
    "Volleyball": "Karch Kiraly"
}

print(sports_players)

print(sports_players.get("Tennis"))

sports_players["Badminton"] = "Carolina Marin"

sports_players.pop("Volleyball")

print("Volleyball:", sports_players["Volleyball"])