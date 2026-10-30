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