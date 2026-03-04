def InfoOfBook(bookID, Bookname, bookStock):
    return {
        "id": bookID,
        "name": Bookname,
        "stock": bookStock
    }

def AddBook(BookList):
    try:
        bookID = int(input("Enter Book ID: "))

        # Prevent duplicate ID (i listan)
        for book in BookList:
            if book["id"] == bookID:
                print("Book ID already exists.")
                return

        Bookname = input("Enter Book Name: ")
        bookStock = int(input("Enter Book Stock: "))

        book = InfoOfBook(bookID, Bookname, bookStock)
        BookList.append(book)

        print("Book added successfully.")

    except ValueError:
        print("Invalid input. Please enter correct values.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


# -----------------------------
# Remove Book
# -----------------------------
def RemoveBook(BookList):
    try:
        bookID = int(input("Enter the Book ID to remove: "))

        for book in BookList:
            if book["id"] == bookID:
                BookList.remove(book)
                print("Book removed successfully.")
                return

        print("Book not found.")

    except ValueError:
        print("Invalid input. Please enter a number.")


# -----------------------------
# Show Books
# -----------------------------
def Showbooks(BookList):
    if not BookList:
        print("No books in the library.")
        return

    print("\n===== LIBRARY BOOK LIST =====")
    print(f"{'ID':<10}{'NAME':<25}{'STOCK':<10}")
    print("-" * 45)

    for book in BookList:
        print(f"{book['id']:<10}{book['name']:<25}{book['stock']:<10}")

    print("-" * 45)


# -----------------------------
# Search Book
# -----------------------------
def SearchForBook(BookList):
    try:
        bookID = int(input("Enter the Book ID: "))

        for book in BookList:
            if book["id"] == bookID:
                print("\nBook Found:")
                print(f"ID: {book['id']}")
                print(f"Name: {book['name']}")
                print(f"Stock: {book['stock']}")
                return

        print("Book not found.")

    except ValueError:
        print("Invalid input. Please enter a number.")


# -----------------------------
# Main Program
# -----------------------------
def main():
    BookList = []

    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            AddBook(BookList)

        elif choice == "2":
            Showbooks(BookList)

        elif choice == "3":
            RemoveBook(BookList)
           
        elif choice == "4":
            SearchForBook(BookList)
            break

        elif choice == "5":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


main()