class User:
    def __init__(self, name):
        self.name = name
        self.checked_out = {}  # isbn → due_date
        self.fines = 0.0       # total outstanding fines

    def add_book(self, isbn, due_date):
        self.checked_out[isbn] = due_date

    def return_book(self, isbn, return_date):
        if isbn in self.checked_out:
            due_date = self.checked_out.pop(isbn)
            if return_date > due_date:
                days_late = (return_date - due_date).days
                self.fines += days_late * 0.50  # 50 cents per day
            return True
        return False

    def clear_fines_if_no_books(self):
        if not self.checked_out:
            self.fines = 0.0



