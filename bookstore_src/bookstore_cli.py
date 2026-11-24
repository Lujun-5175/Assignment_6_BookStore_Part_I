import sqlite3

DB_NAME = "bookstore.db"


def show_rows(cursor):
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")


def view_categories(cursor):
    cursor.execute("SELECT * FROM category ORDER BY categoryId")
    show_rows(cursor)


def view_books(cursor):
    cursor.execute("SELECT * FROM book ORDER BY title")
    show_rows(cursor)


def view_books_in_category(cursor):
    category_id = int(input("Enter category id: "))
    cursor.execute("""
        SELECT book.bookId, book.title, book.author, book.price,
               category.categoryName
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE category.categoryId = ?
        ORDER BY book.title
    """, (category_id,))
    show_rows(cursor)


def search_by_title(cursor):
    keyword = input("Enter title keyword: ").strip()
    cursor.execute("""
        SELECT bookId, title, author, price
        FROM book
        WHERE title LIKE ?
        ORDER BY title
    """, ('%' + keyword + '%',))
    show_rows(cursor)


def add_book(cursor):
    category_id = int(input("Enter category id: "))
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN: ").strip()
    price = float(input("Enter price: "))
    image = input("Enter image filename: ").strip()
    read_now = int(input("Enter readNow (0 or 1): "))

    if not title or not author or not isbn or not image:
        print("Fields cannot be empty.")
        return

    cursor.execute("""
        INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (category_id, title, author, isbn, price, image, read_now))
    print("Book added.")


def update_price(cursor):
    book_id = int(input("Enter book id: "))
    price = float(input("Enter new price: "))
    cursor.execute("UPDATE book SET price = ? WHERE bookId = ?", (price, book_id))
    if cursor.rowcount == 0:
        print("Book not found.")
    else:
        print("Price updated.")


def delete_book(cursor):
    book_id = int(input("Enter book id: "))
    cursor.execute("DELETE FROM book WHERE bookId = ?", (book_id,))
    if cursor.rowcount == 0:
        print("Book not found.")
    else:
        print("Book deleted.")


def search_by_author(cursor):
    keyword = input("Enter author keyword: ").strip()
    cursor.execute("""
        SELECT bookId, title, author, price
        FROM book
        WHERE author LIKE ?
        ORDER BY title
    """, ('%' + keyword + '%',))
    show_rows(cursor)


def main():
    connection = sqlite3.connect(DB_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    print("Welcome to the Bookstore!")
    try:
        while True:
            print("\nBookstore Menu")
            print("1. View all categories")
            print("2. View all books")
            print("3. View books in a category")
            print("4. Search books by title")
            print("5. Add a new book")
            print("6. Update a book price")
            print("7. Delete a book")
            print("8. Quit")
            print("9. Search books by author")
            choice = input("Choose an option: ").strip()

            try:
                if choice == '1':
                    view_categories(cursor)
                elif choice == '2':
                    view_books(cursor)
                elif choice == '3':
                    view_books_in_category(cursor)
                elif choice == '4':
                    search_by_title(cursor)
                elif choice == '5':
                    add_book(cursor)
                elif choice == '6':
                    update_price(cursor)
                elif choice == '7':
                    delete_book(cursor)
                elif choice == '8':
                    print("Goodbye!")
                    break
                elif choice == '9':
                    search_by_author(cursor)
                else:
                    print("Invalid option.")
                connection.commit()
            except ValueError:
                connection.rollback()
                print("Invalid input.")
            except sqlite3.IntegrityError as error:
                connection.rollback()
                print("Database error:", error)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
