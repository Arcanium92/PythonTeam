from library_app.catalog import Catalog
from library_app.book import Book
from datetime import timedelta

def test_book_checked_out_through_catalog_records_due_date():
    # Arrange
    catalog = Catalog()
    book = Book("Clean Code", "Martin", "111", 3)
    catalog.add_book(book)

    # Act
    catalog.check_out_book("111")

    # Assert
    assert book.due_date is not None
    
        
def test_checkout_assigns_due_date():
    # Arrange
    book = Book("Summer Knight", "Jim Butcher", "123", 2)

    # Act
    book.check_out()

    # Assert
    assert book.checkout_date is not None
    assert book.due_date == book.checkout_date + timedelta(days=14)
from library_app.book import Book
from library_app.catalog import Catalog
from library_app.reservation import (
    ReservationStatus, view_reservations,
    make_reservation, reservation_menu
)

def test_check_out_nonexistent_book_raises_error():
    # Arrange
    catalog = Catalog()
    catalog.add_book(Book("Clean Code", "Martin", "111", 3))

    error_raised = False

    # Act
    try:
        catalog.check_out_book("999")
    except RuntimeError:
        error_raised = True

    # Assert
    assert error_raised


def test_check_out_one_book_does_not_affect_other_books_count():
    # Arrange
    catalog = Catalog()
    first_book = Book("Clean Code", "Martin", "111", 3)
    second_book = Book("The DevOps Handbook", "Kim", "222", 2)
    catalog.add_book(first_book)
    catalog.add_book(second_book)

    # Act
    catalog.check_out_book("111")

    # Assert
    assert first_book.available_copies == 2
    assert second_book.available_copies == 2


def test_total_available_copies_is_correct_after_multiple_checkouts():
    # Arrange
    catalog = Catalog()
    first_book = Book("Clean Code", "Martin", "111", 3)
    second_book = Book("The DevOps Handbook", "Kim", "222", 2)
    catalog.add_book(first_book)
    catalog.add_book(second_book)

    # Act
    catalog.check_out_book("111")
    catalog.check_out_book("111")
    catalog.check_out_book("222")
    total = catalog.total_available_copies()

    # Assert
    assert total == 2


def test_add_book_rejects_duplicate_isbn_after_other_books_added():
    # Arrange
    catalog = Catalog()
    catalog.add_book(Book("Clean Code", "Martin", "111", 3))
    catalog.add_book(Book("The DevOps Handbook", "Kim", "222", 2))
    duplicate_book = Book("Different Title", "Different Author", "111", 1)

    error_raised = False

    # Act
    try:
        catalog.add_book(duplicate_book)
    except RuntimeError:
        error_raised = True

    # Assert
    assert error_raised
    assert len(catalog.books) == 2


def feed_inputs(monkeypatch, answers):

    """Makes input() return each answer in order."""
    answer_iter = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answer_iter))


def test_reservation_menu_full_flow_with_real_catalog(monkeypatch, capsys):

    # Arrange: real Catalog + real Reservation objects driven through the menu
    catalog = Catalog()
    catalog.add_book(Book("Clean Code", "Martin", "111", 2))
    reservations = []
    # make (isbn, name) -> view -> cancel #1 -> view -> return
    feed_inputs(monkeypatch, ["2", "111", "Alex", "1", "3", "1", "1", "4"])

    # Act
    reservation_menu(catalog, reservations)
    output = capsys.readouterr().out

    # Assert
    assert len(reservations) == 1
    assert reservations[0].status == ReservationStatus.CANCELLED
    assert "Reservation created." in output
    assert "Reservation cancelled." in output
    assert "cancelled | " in output





def test_reservation_only_accepted_for_books_that_exist_in_catalog(monkeypatch, capsys):

    # Arrange: reservation must agree with what Catalog actually holds
    catalog = Catalog()
    catalog.add_book(Book("Clean Code", "Martin", "111", 2))
    reservations = []
    feed_inputs(monkeypatch, ["111", "Alex", "222"])



    # Act
    make_reservation(catalog, reservations)   # ISBN in catalog
    make_reservation(catalog, reservations)   # ISBN not in catalog
    view_reservations(reservations)
    output = capsys.readouterr().out



    # Assert
    assert len(reservations) == 1
    assert reservations[0].isbn == "111"
    assert "No book found with ISBN '222'." in output
    assert "Alex" in output

