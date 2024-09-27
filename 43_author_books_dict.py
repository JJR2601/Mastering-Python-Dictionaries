author_books = {
    'J.K. Rowling': 'Harry Potter and the Sorcerers Stone',
    'J.R.R. Tolkien': 'The Hobbit',
    'George Orwell': '1984',
    'Jane Austen': 'Pride and Prejudice',
    'Mark Twain': 'The Adventures of Tom Sawyer',
    'F. Scott Fitzgerald': 'The Great Gatsby',
    'Harper Lee': 'To Kill a Mockingbird',
    'Gabriel García Márquez': 'One Hundred Years of Solitude'
}

print(author_books)

print(author_books.get('Mark Twain'))

author_books['Harper Lee'] = 'Go Set a Watchman'

author_books.pop('F. Scott Fitzgerald')

print('Gabriel García Márquez:', author_books['Gabriel García Márquez'])
