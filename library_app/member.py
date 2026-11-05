from datetime import datetime

class Member:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = {}  # isbn → due_date
        self.outstanding_fines = 0.0

    def can_check_out(self, fine_policy):
        return self.outstanding_fines < fine_policy.fine_threshold

    def add_book(self, isbn, due_date):
        self.checked_out_books[isbn] = due_date

    def return_book(self, isbn, return_date, fine_policy):
        if isbn not in self.checked_out_books:
            return 0.0

        due_date = self.checked_out_books.pop(isbn)
        fine = fine_policy.calculate_fine(due_date, return_date)
        self.outstanding_fines += fine
        return fine

    def pay_fine(self, amount):
        self.outstanding_fines = max(0.0, self.outstanding_fines - amount)

    def get_balance(self):
        return self.outstanding_fines