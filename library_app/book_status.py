from datetime import datetime
from library_app.book import Book
from library_app.catalog import Catalog

class BookStatus:
    def __init__(self, book, user, checkout_date, due_date):
        self.book = book
        self.user = user
        self.checkout_date = checkout_date
        self.due_date = due_date
        self.return_date = None

    def is_overdue(self):
        if self.return_date is None:
            return datetime.now() > self.due_date

        return self.return_date > self.due_date

    def get_overdue_book_report(self) -> list[Book]:
        """ Returns overdue books """
        return [book for book in self._books if book.is_overdue()]

    def overdue_count(self) -> int:
        """ Returns int value of overdue books """
        return len(self.get_overdue_book_report())