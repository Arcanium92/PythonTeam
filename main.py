"""
Console app entry point demonstrating the library checkout system.
Run with: python main.py
"""

from library_app.book import Book
from library_app.catalog import Catalog
from library_app.reportsSubMenu import reports_menu
from library_app.reservation import reservation_menu
from library_app.user import User
from library_app.book_status import OverdueReport

def main():
    users = {}
    statuses = []


    print("=== Library Management System ===")
    print()

    # Account Menu
    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter your name: ").strip()

            if name in users:
                print("Account already exists.")
            else:
                users[name] = User(name)
                print(f"Account created for {name}!")

        elif choice == "2":
            name = input("Enter your name: ").strip()

            if name not in users:
                print("Account not found.")
                continue

            current_user = users[name]
            print(f"Welcome, {current_user.name}!")
            break

        elif choice == "3":
            print("Goodbye!")
            return

        else:
            print("Invalid selection.")

        reservations = []

    while True:

        print()
        print("  Library Main Menu  ")
        print("---------------------")
        print("(1.) Checkout Test")
        print("(2.) Manage Reservations")
        print("(3.) View reports")
        print("(4.) Exit")
        print("---------------------")
        choice = input("Select an option: ").strip()

        catalog = Catalog()

        catalog.add_book(Book("The Pragmatic Programmer", "David Thomas", "9780135957059", 3))
        catalog.add_book(Book("Clean Code", "Robert C. Martin", "9780132350884", 2))
        catalog.add_book(Book("The DevOps Handbook", "Gene Kim", "9781942788003", 1))


        if choice == "1":
            print()
            Catalog.check_out_book(catalog, input("Please enter the desired ISBN: ").strip())
        elif choice == "2":
            reservation_menu(catalog, reservations)
        elif choice == "3":
            report = OverdueReport(statuses)
            reports_menu(report, reservations)
        elif choice == "4":
            print()
            print("See you next time!")
            break
        else:
            print("Invalid input. Please select 1, 2, or 3.")


    # print("=== Library Catalog ===")
    # print()
    # selection = input("Would you like to view current book listings? (Y: view listings / N: exit): ")
    # while selection.strip().lower() not in "n":
    #     if selection.strip().lower() in "y":
    #         print()
    #         print("Current selections: ")
    #         print()
    #         for book in catalog.books:
    #             print(f"{book.title} by {book.author} \u2014 ISBN# {book.isbn} {book.available_copies}/{book.total_copies} available")
    #             print()

    #     else:
    #         print("Invalid input. Please select Y or N.")

    #     print()
    #     selection = input("Would you like to view current book listings? (Y/N): ")
    # print("Enter ISBN you want to check out:")
    # isbn = input()
    # try:
    #     catalog.check_out_book(isbn)
    # except RuntimeError as error:
    #     print(error)
    #     return

    # query = input("Search for a book by title: ").strip()
    # results = catalog.search_by_title(query)

    # if not results:
    #     print("No books found with that title.")
    # else:
    #     print("\nSearch Results:")
    #     for book in results:
    #         print(f"{book.title} by {book.author} \u2014 {book.available_copies}/{book.total_copies} available")

    # checked_out = catalog.find_by_isbn(isbn)
    # print(f"'{checked_out.title}' now has {checked_out.available_copies}/{checked_out.total_copies} available.")

if __name__ == "__main__":
    main()