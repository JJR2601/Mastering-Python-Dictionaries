athletes_achievements = {
    "usain bolt": "world record holder in 100m and 200m sprints",
    "michael ohelps": "most Olympic gold medals won (23)",
    "serena williams": "winning 23 grand slam singles titles",
    "lionel messi": "7 ballon d'or awards",
    "tom brady": "7 super bowl wins",
    "babe ruth": "one of the greatest baseball players, with 714 home runs",
    "michael jordan": "6-time NBA champion and 5-time MVP",
    "simone biles": "most decorated gymnast in world championship history"
}

print(athletes_achievements)

print(athletes_achievements.get("tom brady"))

athletes_achievements["serena williams"] = "won 14 grand slam doubles titles"

athletes_achievements.pop("michael jordan")

print("simone biles:", athletes_achievements["simone biles"])



