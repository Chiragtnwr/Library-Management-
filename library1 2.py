
# LIBRARY MANAGEMENT SYSTEM

library = {
    "Python Basics": {"author": "John", "available": True},
    "Learn Java": {"author": "David", "available": True},
    "Web Development": {"author": "Alex", "available": True}
}


def show_books():
    print("\n--- LIBRARY BOOKS ---")

    if not library:
        print("No books in the library.")
        return

    for book, details in library.items():
        status = "Available" if details["available"] else "Borrowed"
        print("Book:", book)
        print("Author:", details["author"])
        print("Status:", status)
        print("-" * 25)


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
    elif title in library:
        print("Book already exists!")
    else:
        library[title] = {
            "author": author,
            "available": True
        }
        print("Book added successfully!")


def borrow_book():
    title = input("Enter book title to borrow: ").strip()

    if title not in library:
        print("Book not found!")
    elif library[title]["available"]:
        library[title]["available"] = False
        print("You borrowed:", title)
    else:
        print("Sorry, this book is already borrowed.")


def return_book():
    title = input("Enter book title to return: ").strip()

    if title not in library:
        print("Book not found!")
    elif library[title]["available"]:
        print("This book was not borrowed.")
    else:
        library[title]["available"] = True
        print("Book returned successfully!")


def search_book():
    title = input("Enter book title to search: ").strip()

    if title in library:
        print("Book:", title)
        print("Author:", library[title]["author"])
        print("Available:", library[title]["available"])
    else:
        print("Book not found!")


while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Show all books")
    print("2. Add a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Search for a book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        show_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print("Thank you for visiting the library!")
        break
    else:
        print("Invalid choice! Please try again.")
