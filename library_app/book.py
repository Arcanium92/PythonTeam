"""
Represents a single book title in the library catalog.
One Book instance represents all copies of that title.
"""


class Book:
    """Defines book class constructor"""
    def __init__(self, title: str, author: str, isbn: str, total_copies: int):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")
        if not author or not author.strip():
            raise ValueError("Author cannot be empty.")
        if not isbn or not isbn.strip():
            raise ValueError("ISBN cannot be empty.")
        if total_copies < 0:
            raise ValueError("Total copies cannot be negative.")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    @property
    def is_available(self) -> bool:
        """Returns a true or false value if available copies falls below 0"""
        return self.available_copies > 0

    def check_out(self) -> None:
        """Reduces available copies by one"""
        if not self.is_available:
            raise RuntimeError(f"No available copies of '{self.title}' to check out.")
        self.available_copies -= 1

    def return_book(self) -> None:
        """Adds one to available copies for requested book"""
        if self.available_copies >= self.total_copies:
            raise RuntimeError(f"All copies of '{self.title}' are already returned.")
        self.available_copies += 1
