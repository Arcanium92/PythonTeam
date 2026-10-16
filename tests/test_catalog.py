from library_app.book import Book
from library_app.catalog import Catalog

def test_find_by_isbn_returns_none_for_missing_isbn():
    catalog = Catalog()
    assert catalog.find_by_isbn("does-not-exist") is None

def test_search_by_title_returns_empty_for_whitespace_query():
    catalog = Catalog()
    assert catalog.search_by_title("    ") == []