book_authors = {
    "Don Quixote": "Miguel de Cervantes",
    "1984": "George Orwell",
    "War and Peace": "Leo Tolstoy",
    "Fahrenheit 451": "Ray Bradbury",
    "The Grapes of Wrath": "John Steinbeck",
    "Brave New World": "Aldous Huxley",
    "Wuthering Heights": "Emily Bronte",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "One Hundred Years of Solitude": "Gabriel Garcia Marquez",
    "The Brothers Karamazov": "Fyodor Dostoevsky",
    "Crime and Punishment": "Fyodor Dostoevsky",
    "Bobby Fischer teaches Chess": "Bobby Fischer"
}

print(book_authors)

print(book_authors.get("One Hundred Years of Solitude"))

book_authors["The Grapes of Wrath"] = "James Lloyd"

book_authors.pop("War and Peace")

print("Bobby Fischer teaches Chess:", book_authors["Bobby Fischer teaches Chess"])