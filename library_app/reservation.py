from enum import Enum
from datetime import datetime

# import catalog later when implementing more methods

class ReservationStatus(Enum):
    """Class to set status for past/present reservations"""
    PENDING = "pending"
    COMPLETE = "complete"
    CANCELLED = "cancelled"

class Reservation:
    """Override method for class constructor"""
    def __init__(self, isbn: str, customer_name: str):
        if not isbn or not isbn.strip():
            raise ValueError("Please enter a valid ISBN.")
        if not customer_name or not customer_name.strip():
            raise ValueError("Customer name can not be empty.")

        self.isbn = isbn
        self.customer_name = customer_name
        self.created_at = datetime.now()
        self.status = ReservationStatus.PENDING

    @property
    def is_pending(self) -> bool:
        """Compare status against ReservationStatus"""
        return self.status == ReservationStatus.PENDING

    def is_complete(self) -> None:
        """Set any pending reservation to complete"""
        if not self.is_pending:
            raise RuntimeError("Only pending reservations can be complete.")
        self.status = ReservationStatus.COMPLETE

    def cancel(self) -> None:
        """Cancel any pending reservation"""
        if not self.is_pending:
            raise RuntimeError("Only pending reservations can be cancelled.")
        self.status = ReservationStatus.CANCELLED

# Going forward with this file I need to add a class for managing reservations
# That is where this class will gain some of its functionality and be ready for implementation into the app
