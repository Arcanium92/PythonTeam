from enum import Enum
from datetime import datetime
from library_app.book import Book
# import catalog later when implementing more methods

class ReservationStatus(Enum):
    """Class to set status for past/present reservations"""
    PENDING = "pending"
    COMPLETE = "complete"
    CANCELLED = "cancelled"
    AVAILABLE = "available"

class Reservation:
    """Override method for class constructor"""
    def __init__(self, isbn: str, customer_name: str):
        if not isbn or not isbn.strip():
            raise ValueError("Please enter a valid ISBN.")
        if not customer_name or not customer_name.strip():
            raise ValueError("Customer name can not be empty.")

        self.isbn = isbn
        self.customer_name = customer_name
        self.created_at = datetime.now()
        self.status = ReservationStatus.PENDING

    @property
    def is_pending(self) -> bool:
        """Compare status against ReservationStatus"""
        return self.status == ReservationStatus.PENDING

    def is_complete(self) -> None:
        """Set any available reservation to complete"""
        if not Book.is_available:
            raise RuntimeError("Only available reservations can be complete.")
        self.status = ReservationStatus.COMPLETE

    def cancel(self) -> None:
        """Cancel any pending reservation"""
        if not self.is_pending:
            raise RuntimeError("Only pending reservations can be cancelled.")
        self.status = ReservationStatus.CANCELLED

    def accept(self) -> None:
        """Accept reservations ready to be checked out"""
        if Book.is_available:
            self.status = ReservationStatus.COMPLETE
def view_reservations(reservations):

    """Prints every reservation made so far."""

    print()

    if not reservations:

        print("No reservations yet.")

        return

    for number, reservation in enumerate(reservations, start=1):

        print(f"{number}. ISBN# {reservation.isbn} | {reservation.customer_name} | "

            f"{reservation.status.value} | {reservation.created_at:%Y-%m-%d %H:%M}")





def make_reservation(catalog, reservations):

    """Asks for an ISBN and a name, then creates a Reservation."""
    print()
    isbn = input("Enter the ISBN to reserve: ").strip()
    if catalog.find_by_isbn(isbn) is None:
        print(f"No book found with ISBN '{isbn}'.")
        return
    name = input("Enter customer name: ").strip()
    try:
        reservations.append(Reservation(isbn, name))
    except ValueError as error:
        print(error)
        return
    print("Reservation created.")





def cancel_reservation(reservations):
    """Asks which reservation to cancel (by its number in the list)."""
    view_reservations(reservations)
    if not reservations:
        return
    choice = input("Enter the number of the reservation to cancel: ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(reservations):
        print("Invalid reservation number.")
        return
    try:
        reservations[int(choice) - 1].cancel()
    except RuntimeError as error:
        print(error)
        return
    print("Reservation cancelled.")





def reservation_menu(catalog, reservations):

    """Menu system for members to manage their reservations"""

    while True:

        print()
        print("  Reservation Manager  ")
        print("-----------------------")
        print("(1.) View Reservations")
        print("(2.) Make a Reservation")
        print("(3.) Cancel a Reservation")
        print("(4.) Return to Main Menu")
        print("-----------------------")
        choice = input("Select an option: ").strip()



        if choice == "1":
            view_reservations(reservations)
        elif choice == "2":
            make_reservation(catalog, reservations)
        elif choice == "3":
            cancel_reservation(reservations)
        elif choice == "4":
            return
        else:
            print("Invalid input. Please select 1-4.")


#     """Menu system for members to manage their reservations"""
#     @property
#     def reservation_menu(Reservation):
#         """Diplays menu to select different reservation options"""
#         while True:
#             print("  Reservation Manager  ")
#             print("-----------------------")
#             print("-")
#             print("(1.) View Reservations ")
#             print("-")
#             print("(2.)  ")
#             print("-")
#             print("(3.) Return to Catalog")
#             print("-")
#             print("(4.)")
#             print("-")
