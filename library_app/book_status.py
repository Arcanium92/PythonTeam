from datetime import datetime
class BookStatus:
    """ Tracks checkout status of a book """

    def __init__(self, book, user, checkout_date, due_date):
        self.book = book
        self.user = user
        self.checkout_date = checkout_date
        self.due_date = due_date
        self.return_date = None


    def is_overdue(self):
        """ Returns true if book is overdue """
        if self.return_date is None:
            return datetime.now() > self.due_date

        return self.return_date > self.due_date

class OverdueReport:
    """ Generates report for overdue books """
    def __init__(self, statuses):
        self.statuses = statuses

    def get_overdue_books(self):
        return [
            status.book
            for status in self.statuses
            if status.is_overdue()
        ]

    def overdue_count(self):
        """ Returns total number of overdue books """
        return len(self.get_overdue_books())

    def overdue_members(self):
        """ Lists names of members with overdue books """
        return {
            status.user.name
            for status in self.statuses
            if status.is_overdue()
        }