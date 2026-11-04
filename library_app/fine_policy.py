from datetime import datetime

class FinePolicy:
    def __init__(self, daily_rate=0.50, fine_threshold=10.00):
        self.daily_rate = daily_rate
        self.fine_threshold = fine_threshold

    def calculate_fine(self, due_date, return_date):
        if return_date <= due_date:
            return 0.0
        days_late = (return_date - due_date).days
        return days_late * self.daily_rate