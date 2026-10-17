"""
EXAMPLE TEST FILE — this is here as a working pattern to copy.
In Week 7 (Unit Testing) you'll add more tests like the one below.

To run these tests: open a terminal in the project root and run `pytest`.
"""
import pytest
from library_app.book import Book
from datetime import datetime, timedelta


def test_check_out_reduces_available_copies_by_one():
    # Arrange
    book = Book("Sample Title", "Sample Author", "0000000000000", 3)
    # Act
    book.check_out()
    # Assert
    assert book.available_copies == 2

def test_check_out_raises_error_when_no_copies_available():
    # Arrange
    book = Book("Title", "Author", "123", 0)
    # Act / Assert
    with pytest.raises(RuntimeError):
        book.check_out()

def test_return_book_increases_available_copies_by_one():
    # Arrange
    book = Book("Title", "Author", "123", 3)
    book.check_out() # now at 2
    # Act
    book.return_book()
    # Assert
    assert book.available_copies == 3

def test_is_available_returns_false_when_no_copies():
    # Arrange
    book = Book("Title", "Author", "123", 1)
    book.check_out()
    # Assert
    assert book.is_available == False

def test_book_raises_value_error_for_empty_title():
    with pytest.raises(ValueError):
        Book("", "Author", "123", 3)

def test_throw_error_on_checkout_when_avaiable_copies_is_0():
    # Arrange
    book = Book("Title", "Author", "123", 0)
    # Act / Assert
    with pytest.raises(RuntimeError):
        book.check_out()

def test_return_book_raises_error_when_all_copies_already_returned():
    # Arrange
    book = Book("Title", "Author", "123", 3)
    # Act / Assert
    with pytest.raises(RuntimeError):
        book.return_book()

def test_checkout_with_due_date_records_due_date():
    # Arrange
    book = Book("Clean Code", "Robert C. Martin", "9780132350884", 2)
    # Act
    book.check_out()
    # Assert
    assert book.due_date == book.checkout_date + timedelta(days=14)

def test_book_is_overdue_when_due_date_is_past():
    # Arrange
    book = Book("Title", "Author", "123", 2)
    book.due_date = datetime.now() - timedelta(days=1)
    # Assert
    assert book.is_overdue() == True

def test_book_is_not_overdue_when_due_date_is_future():
    # Arrange
    book = Book("Title", "Author", "123", 2)
    book.due_date = datetime.now() + timedelta(days=14)
    # Assert
    assert book.is_overdue() == False

