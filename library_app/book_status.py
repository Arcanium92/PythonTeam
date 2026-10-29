from datetime import datetime
from library_app.book import Book
from library_app.catalog import Catalog

class BookStatus:
    def __init__(self, book,checkout_date, return_date, over_due, members):
        self.book = book
        self.return_date = return_date
        self.over_due = over_due
        self.members = members
        self.checkout_date = checkout_date