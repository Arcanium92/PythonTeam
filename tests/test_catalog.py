from library_app.book import Book
from library_app.catalog import Catalog


def test_find_by_isbn_returns_correct_book_for_known_isbn():
    # Arrange
    catalog = Catalog()
    book = Book("Sample Title", "Sample Author", "0000000000000", 3)
    catalog.add_book(book)

    # Act
    result = catalog.find_by_isbn("0000000000000")

    # Assert
    assert result is book


def test_find_by_isbn_returns_none_for_unknown_isbn():
    # Arrange
    catalog = Catalog()
    catalog.add_book(Book("Sample Title", "Sample Author", "0000000000000", 3))

    # Act
    result = catalog.find_by_isbn("9999999999999")

    # Assert
    assert result is None


def test_search_by_title_returns_matching_books():
    # Arrange
    catalog = Catalog()
    matching_book = Book("Clean Code", "Sample Author", "0000000000000", 3)
    other_book = Book("The DevOps Handbook", "Sample Author", "1111111111111", 2)
    catalog.add_book(matching_book)
    catalog.add_book(other_book)

    # Act
    results = catalog.search_by_title("clean")

    # Assert
    assert results == [matching_book]


def test_search_by_title_returns_empty_list_when_nothing_matches():
    # Arrange
    catalog = Catalog()
    catalog.add_book(Book("Clean Code", "Sample Author", "0000000000000", 3))

    # Act
    results = catalog.search_by_title("Nonexistent Title")

    # Assert
    assert results == []


def test_total_available_copies_returns_correct_total_across_all_books():
    # Arrange
    catalog = Catalog()
    first_book = Book("Sample Title One", "Sample Author", "0000000000000", 3)
    second_book = Book("Sample Title Two", "Sample Author", "1111111111111", 2)
    catalog.add_book(first_book)
    catalog.add_book(second_book)
    first_book.check_out()
    
    # Act
    total = catalog.total_available_copies()
    
    # Assert
    assert total == 4
