prog_languages = {
    "Python": "Guido van Rossum",
    "Java script": "Brendan Eich",
    "PHP": "Rasmus Lerdorf",
    "C++": "Bjarne Stroustrup",
    "C#": "Microsoft",
    "Java": "James Gosling",
    "Ruby": "Yukihiro Matsumoto"
}

print(prog_languages)

print(prog_languages.get("C++"))

prog_languages["Java"] = "Oracle"

prog_languages.pop("Java script")

print("Ruby:", prog_languages["Ruby"])