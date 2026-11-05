from library_app.reservation import (
    Reservation, ReservationStatus, view_reservations,
    make_reservation, cancel_reservation, reservation_menu
)

def test_new_reservation_starts_with_pending_status():
    # Arrange
    reservation = Reservation("0000000000000", "Sample Customer")

    # Act
    status = reservation.status

    # Assert
    assert status == ReservationStatus.PENDING

def test_cancel_sets_status_to_cancelled():
    # Arrange
    reservation = Reservation("0000000000000", "Sample Customer")

    # Act
    reservation.cancel()

    # Assert
    assert reservation.status == ReservationStatus.CANCELLED

def test_cancel_raises_error_when_reservation_is_not_pending():
    # Arrange
    reservation = Reservation("0000000000000", "Sample Customer")
    reservation.is_complete()

    error_raised = False

    # Act
    try:
        reservation.cancel()
    except RuntimeError:
        error_raised = True

    # Assert
    assert error_raised

def test_accept_sets_status_to_complete():
    # Arrange
    reservation = Reservation("0000000000000","Sample Customer")

    # Act
    reservation.accept()


    # Assert
    assert reservation.status == ReservationStatus.COMPLETE

class FakeCatalog:

    """Minimal stand-in for Catalog so these stay unit tests."""

    def __init__(self, isbns):
        self.isbns = isbns

    def find_by_isbn(self, isbn):
        return isbn if isbn in self.isbns else None





def feed_inputs(monkeypatch, answers):

    """Makes input() return each answer in order."""
    answer_iter = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answer_iter))





def test_view_reservations_says_none_when_list_is_empty(capsys):

    # Arrange
    reservations = []



    # Act
    view_reservations(reservations)
    output = capsys.readouterr().out



    # Assert
    assert "No reservations yet." in output





def test_view_reservations_shows_isbn_name_and_status(capsys):

    # Arrange
    reservations = [Reservation("111", "Alex")]



    # Act
    view_reservations(reservations)
    output = capsys.readouterr().out



    # Assert
    assert "111" in output
    assert "Alex" in output
    assert "pending" in output





def test_make_reservation_adds_reservation_when_isbn_exists(monkeypatch):

    # Arrange
    reservations = []
    feed_inputs(monkeypatch, ["111", "Alex"])



    # Act
    make_reservation(FakeCatalog(["111"]), reservations)



    # Assert
    assert len(reservations) == 1
    assert reservations[0].isbn == "111"
    assert reservations[0].customer_name == "Alex"





def test_make_reservation_rejects_unknown_isbn(monkeypatch, capsys):

    # Arrange
    reservations = []
    feed_inputs(monkeypatch, ["999"])



    # Act
    make_reservation(FakeCatalog(["111"]), reservations)
    output = capsys.readouterr().out



    # Assert
    assert reservations == []
    assert "No book found with ISBN '999'." in output





def test_make_reservation_rejects_empty_customer_name(monkeypatch, capsys):

    # Arrange
    reservations = []
    feed_inputs(monkeypatch, ["111", "   "])



    # Act
    make_reservation(FakeCatalog(["111"]), reservations)
    output = capsys.readouterr().out



    # Assert
    assert reservations == []
    assert "Customer name can not be empty." in output





def test_cancel_reservation_cancels_the_chosen_reservation(monkeypatch):

    # Arrange
    first = Reservation("111", "Alex")
    second = Reservation("222", "Sam")
    feed_inputs(monkeypatch, ["2"])



    # Act
    cancel_reservation([first, second])



    # Assert
    assert first.status == ReservationStatus.PENDING
    assert second.status == ReservationStatus.CANCELLED





def test_cancel_reservation_rejects_invalid_number(monkeypatch, capsys):

    # Arrange
    reservation = Reservation("111", "Alex")
    feed_inputs(monkeypatch, ["5"])



    # Act
    cancel_reservation([reservation])
    output = capsys.readouterr().out



    # Assert
    assert reservation.status == ReservationStatus.PENDING
    assert "Invalid reservation number." in output





def test_cancel_reservation_reports_error_when_already_cancelled(monkeypatch, capsys):

    # Arrange
    reservation = Reservation("111", "Alex")
    reservation.cancel()
    feed_inputs(monkeypatch, ["1"])



    # Act
    cancel_reservation([reservation])
    output = capsys.readouterr().out



    # Assert
    assert "Only pending reservations can be cancelled." in output





def test_reservation_menu_returns_when_option_four_is_chosen(monkeypatch, capsys):

    # Arrange
    feed_inputs(monkeypatch, ["4"])



    # Act
    reservation_menu(FakeCatalog([]), [])
    output = capsys.readouterr().out



    # Assert
    assert "Reservation Manager" in output





def test_reservation_menu_reprompts_after_invalid_choice(monkeypatch, capsys):

    # Arrange
    feed_inputs(monkeypatch, ["x", "4"])



    # Act
    reservation_menu(FakeCatalog([]), [])
    output = capsys.readouterr().out



    # Assert
    assert "Invalid input. Please select 1-4." in output

